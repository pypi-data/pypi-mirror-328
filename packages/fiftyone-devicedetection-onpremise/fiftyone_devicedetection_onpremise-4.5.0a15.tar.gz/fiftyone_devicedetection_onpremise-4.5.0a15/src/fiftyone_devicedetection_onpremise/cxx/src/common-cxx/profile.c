/* *********************************************************************
 * This Original Work is copyright of 51 Degrees Mobile Experts Limited.
 * Copyright 2023 51 Degrees Mobile Experts Limited, Davidson House,
 * Forbury Square, Reading, Berkshire, United Kingdom RG1 3EU.
 *
 * This Original Work is licensed under the European Union Public Licence
 * (EUPL) v.1.2 and is subject to its terms as set out below.
 *
 * If a copy of the EUPL was not distributed with this file, You can obtain
 * one at https://opensource.org/licenses/EUPL-1.2.
 *
 * The 'Compatible Licences' set out in the Appendix to the EUPL (as may be
 * amended by the European Commission) shall be deemed incompatible for
 * the purposes of the Work and the provisions of the compatibility
 * clause in Article 5 of the EUPL shall not apply.
 *
 * If using the Work as, or as part of, a network application, by
 * including the attribution notice(s) required under Article 5 of the EUPL
 * in the end user terms of the application under an appropriate heading,
 * such notice(s) shall fulfill the requirements of that article.
 * ********************************************************************* */

#include "profile.h"
#include "fiftyone.h"

MAP_TYPE(Collection)

static uint32_t getFinalProfileSize(void *initial) {
	Profile *profile = (Profile*)initial;
	return sizeof(Profile) +
		(profile->valueCount * sizeof(uint32_t));
}

static Profile* getProfileByOffset(
	Collection *profilesCollection,
	uint32_t offset,
	Item *item,
	Exception *exception) {
	return (Profile*)profilesCollection->get(
		profilesCollection,
		offset,
		item,
		exception);
}

#ifdef _MSC_VER
#pragma warning (push)
#pragma warning (disable: 4100)
#endif
static int compareProfileId(
	void *profileId, 
	Item *item,
	long curIndex,
	Exception *exception) {
	const unsigned int a = ((ProfileOffset*)item->data.ptr)->profileId;
	const unsigned int b = *(uint32_t*)profileId;
	if (a < b) return -1;
	if (a > b) return 1;
	return 0;
}
#ifdef _MSC_VER
#pragma warning (pop)
#endif

static int compareValueToProperty(const void *p, const void *v) {
	Property *property = (Property*)p;
	uint32_t valueIndex = *(uint32_t*)v;
	if (valueIndex < property->firstValueIndex) {
		return 1;
	}
	if (valueIndex > property->lastValueIndex) {
		return -1;
	}
	return 0;
}

static uint32_t* getFirstValueForProfileAndProperty(
	fiftyoneDegreesProfile *profile,
	fiftyoneDegreesProperty *property) {

	// Search to find a value that is equal to or between the first and last
	// value indexes for the property.
	uint32_t *valueIndex = (uint32_t*)bsearch(
		property,
		profile + 1,
		profile->valueCount,
		sizeof(uint32_t),
		compareValueToProperty);

	if (valueIndex != NULL) {

		// Move back through the values until the first one for the property is 
		// found.
		while ((void*)valueIndex > (void*)(profile + 1) &&
			*(valueIndex - 1) >= property->firstValueIndex) {
			valueIndex--;
		}
	}

	return valueIndex;
}

/**
 * Starting at the value index pointed to by valIndexPtr iterates over the 
 * value indexes checking that they relate to the property. maxValIndexPtr is
 * used to prevent overrunning the memory used for values associated with the 
 * profile. The value items are passed to the callback method which is 
 * responsible for freeing these items.
 */
static uint32_t iterateValues(
	Collection *values,
	Property *property,
	void *state,
	ProfileIterateMethod callback,
	uint32_t *valIndexPtr,
	uint32_t *maxValIndexPtr,
	Exception *exception) {
	Item valueItem;
	uint32_t count = 0;
	bool cont = true;

	// Loop through until the last value for the property has been returned
	// or the callback doesn't need to continue.
	while (cont == true &&
        // Check the address validity, before dereferencing to prevent 
		// potential memory fault on dereference.
        valIndexPtr < maxValIndexPtr &&
		// Check that the value index could relate to the property. Saves 
		// having to retrieve the value item if it will never relate to the
		// property.
        *valIndexPtr <= property->lastValueIndex &&
		EXCEPTION_OKAY) {

		// Reset the items as they should never share the same memory.
		DataReset(&valueItem.data);

		// Get the value from the value index and call the callback. Do not 
		// free the item as the calling function is responsible for this.
		if (values->get(values, *valIndexPtr, &valueItem, exception) != NULL &&
			EXCEPTION_OKAY) {
			cont = callback(state, &valueItem);
			count++;
		}

		// Move to the next value index pointer as this might relate to another
		// value for the property.
		valIndexPtr++;
	}

	return count;
}

static bool isAvailableProperty(
	PropertiesAvailable* available, 
	uint32_t propertyIndex) {
	for (uint32_t i = 0; i < available->count; i++) {
		if (available->items[i].propertyIndex == propertyIndex) {
			return true;
		}
	}
	return false;
}

uint32_t* fiftyoneDegreesProfileGetOffsetForProfileId(
	fiftyoneDegreesCollection *profileOffsets,
	const uint32_t profileId,
	uint32_t *profileOffset,
	fiftyoneDegreesException *exception) {
	long index;
	Item profileOffsetItem;
	DataReset(&profileOffsetItem.data);

	if (profileId == 0) {
		EXCEPTION_SET(PROFILE_EMPTY);
	}
	else {
		
		// Get the index in the collection of profile offsets for the required
		// profile id.
		index = CollectionBinarySearch(
			profileOffsets,
			&profileOffsetItem,
			0,
			CollectionGetCount(profileOffsets) - 1,
			(void*)&profileId,
			compareProfileId,
			exception);

		// If the profile id is present then return the offset for it otherwise
		// set the offset to NULL.
		if (index >= 0 && EXCEPTION_OKAY) {
			*profileOffset = 
				((ProfileOffset*)profileOffsetItem.data.ptr)->offset;
		}
		else {
			profileOffset = NULL;
		}

		// Release the item that contains the list profile offset found.
		COLLECTION_RELEASE(profileOffsets, &profileOffsetItem);
	}

	return profileOffset;
}

fiftyoneDegreesProfile* fiftyoneDegreesProfileGetByProfileId(
	fiftyoneDegreesCollection *profileOffsets, 
	fiftyoneDegreesCollection *profiles,
	const uint32_t profileId,
	fiftyoneDegreesCollectionItem *item,
	fiftyoneDegreesException *exception) {
	uint32_t profileOffset;
	Profile* profile = NULL;
	if (fiftyoneDegreesProfileGetOffsetForProfileId(
			profileOffsets,
			profileId,
			&profileOffset,
			exception) != NULL && EXCEPTION_OKAY) {
		profile = getProfileByOffset(
			profiles,
			profileOffset,
			item,
			exception);
	}
	return profile;
}

fiftyoneDegreesProfile* fiftyoneDegreesProfileGetByIndex(
	fiftyoneDegreesCollection *profileOffsets,
	fiftyoneDegreesCollection *profiles,
	uint32_t index,
	fiftyoneDegreesCollectionItem *item,
	fiftyoneDegreesException *exception) {
	Profile *profile = NULL;
	Item offset;
	DataReset(&offset.data);

	// Get the profile offset for the profile at the index provided using
	// the offset collection item as the handle.
	ProfileOffset *profileOffset = (ProfileOffset*)profileOffsets->get(
		profileOffsets,
		index,
		&offset,
		exception);
	if (profileOffset != NULL && EXCEPTION_OKAY) {
		profile = (fiftyoneDegreesProfile*)profiles->get(
			profiles,
			profileOffset->offset,
			item,
			exception);
		COLLECTION_RELEASE(profileOffsets, &offset);
	}
	return profile;
}

#ifndef FIFTYONE_DEGREES_MEMORY_ONLY

void* fiftyoneDegreesProfileReadFromFile(
	const fiftyoneDegreesCollectionFile *file,
	uint32_t offset,
	fiftyoneDegreesData *data,
	fiftyoneDegreesException *exception) {
	Profile profile = { 0, 0, 0 };
	return CollectionReadFileVariable(
		file,
		data,
		offset,
		&profile,
		sizeof(Profile),
		getFinalProfileSize,
		exception);
}

#endif

uint32_t fiftyoneDegreesProfileIterateValuesForProperty(
	fiftyoneDegreesCollection *values,
	fiftyoneDegreesProfile *profile,
	fiftyoneDegreesProperty *property,
	void *state,
	fiftyoneDegreesProfileIterateMethod callback,
	fiftyoneDegreesException *exception) {
	uint32_t *firstValueIndex  = getFirstValueForProfileAndProperty(
		profile, 
		property);
	uint32_t count = 0;
	if (firstValueIndex != NULL) {
		count = iterateValues(
			values, 
			property, 
			state, 
			callback, 
			firstValueIndex,
			((uint32_t*)(profile + 1)) + profile->valueCount,
			exception);
	}
	return count;
}

uint32_t fiftyoneDegreesProfileIterateValuesForPropertyWithIndex(
	fiftyoneDegreesCollection* values,
	fiftyoneDegreesIndicesPropertyProfile* index,
	uint32_t availablePropertyIndex,
	fiftyoneDegreesProfile* profile,
	fiftyoneDegreesProperty* property,
	void* state,
	fiftyoneDegreesProfileIterateMethod callback,
	fiftyoneDegreesException* exception) {
	uint32_t i = IndicesPropertyProfileLookup(
		index,
		profile->profileId,
		availablePropertyIndex);
	if (i < profile->valueCount) {
		uint32_t* firstValueIndex = (uint32_t*)(profile + 1) + i;
		return iterateValues(
			values,
			property,
			state,
			callback,
			firstValueIndex,
			((uint32_t*)(profile + 1)) + profile->valueCount,
			exception);
	}
	return 0;
}

uint32_t fiftyoneDegreesProfileIterateProfilesForPropertyAndValue(
	fiftyoneDegreesCollection *strings,
	fiftyoneDegreesCollection *properties,
	fiftyoneDegreesCollection *values,
	fiftyoneDegreesCollection *profiles,
	fiftyoneDegreesCollection *profileOffsets,
	const char *propertyName,
	const char* valueName,
	void *state,
	fiftyoneDegreesProfileIterateMethod callback,
	fiftyoneDegreesException *exception) {
	uint32_t i, count = 0;
	Item propertyItem, offsetItem, profileItem;
	uint32_t *profileValueIndex, *maxProfileValueIndex;
	Property *property;
	Profile *profile;
	ProfileOffset *profileOffset;
	DataReset(&propertyItem.data);
	property = PropertyGetByName(
		properties, 
		strings,
		propertyName, 
		&propertyItem,
		exception);
	if (property != NULL && EXCEPTION_OKAY) {
		const long valueIndex = fiftyoneDegreesValueGetIndexByName(
			values,
			strings,
			property, 
			valueName,
			exception);
		if (valueIndex >= 0 && EXCEPTION_OKAY) {
			DataReset(&offsetItem.data);
			DataReset(&profileItem.data);
			uint32_t profileOffsetsCount = CollectionGetCount(profileOffsets);
			for (i = 0; i < profileOffsetsCount; i++) {
				profileOffset = (ProfileOffset*)profileOffsets->get(
					profileOffsets,
					i,
					&offsetItem, 
					exception);
				if (profileOffset != NULL && EXCEPTION_OKAY) {
					profile = getProfileByOffset(
						profiles,
						profileOffset->offset,
						&profileItem,
						exception);
					if (profile != NULL && EXCEPTION_OKAY) {
						profileValueIndex = getFirstValueForProfileAndProperty(
							profile,
							property);
						if (profileValueIndex != NULL) {
							maxProfileValueIndex = ((uint32_t*)(profile + 1)) +
								profile->valueCount;
							while (*profileValueIndex <=
								property->lastValueIndex &&
								profileValueIndex < maxProfileValueIndex) {
								if ((uint32_t)valueIndex ==
									*profileValueIndex) {
									callback(state, &profileItem);
									count++;
									break;
								}
								profileValueIndex++;
							}
						}
						COLLECTION_RELEASE(profileOffsets, &profileItem);
					}
					COLLECTION_RELEASE(profileOffsets, &offsetItem);
				}
			}
		}
		COLLECTION_RELEASE(properties, &propertyItem);
	}
	return count;
}

uint32_t fiftyoneDegreesProfileIterateValueIndexes(
	fiftyoneDegreesProfile* profile,
	fiftyoneDegreesPropertiesAvailable* available,
	fiftyoneDegreesCollection* values,
	void* state,
	fiftyoneDegreesProfileIterateValueIndexesMethod callback,
	fiftyoneDegreesException* exception) {
	Item valueItem;
	Value* value;
	bool cont = true;
	uint32_t count = 0;
	const uint32_t* valueIndexes = (const uint32_t*)(profile + 1);
	uint32_t valueIndex;
	DataReset(&valueItem.data);

	// For all the possible values associated with the profile.
	for (uint32_t i = 0; cont && i < profile->valueCount; i++) {

		// Get the value to check if it relates to a required property.
		valueIndex = *(valueIndexes + i);
		value = values->get(values, valueIndex, &valueItem, exception);
		if (value == NULL || EXCEPTION_FAILED) {
			return count;
		}

		// If the value does relate to an available property then call the 
		// callback.
		if (isAvailableProperty(available, (uint32_t)value->propertyIndex)) {
			cont = callback(state, valueIndex);
			count++;
		}

		COLLECTION_RELEASE(values, &valueItem);
	}
	return count;
}
