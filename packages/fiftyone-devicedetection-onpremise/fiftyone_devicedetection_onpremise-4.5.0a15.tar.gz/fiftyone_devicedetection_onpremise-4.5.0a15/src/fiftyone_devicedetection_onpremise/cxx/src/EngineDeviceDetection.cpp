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

#include "EngineDeviceDetection.hpp"

using namespace FiftyoneDegrees::DeviceDetection;

string EngineDeviceDetection::defaultElementDataKey = "device";

EngineDeviceDetection::EngineDeviceDetection(
	ConfigDeviceDetection *config,
	RequiredPropertiesConfig *requiredProperties) 
	: EngineBase(config, requiredProperties) {}

void EngineDeviceDetection::init(
	fiftyoneDegreesDataSetDeviceDetection *dataSet) {
	initHttpHeaderKeys(dataSet->b.uniqueHeaders);
	initOverrideKeys(dataSet->b.overridable);
	addKey("query.51D_deviceId");
	addKey("query.51D_gethighentropyvalues");
	addKey("query.51D_structureduseragent");
	addKey("cookie.51D_gethighentropyvalues");
	addKey("cookie.51D_structureduseragent");
}

ResultsDeviceDetection*
EngineDeviceDetection::processDeviceDetection(
	string &userAgent) const {
	return processDeviceDetection(userAgent.c_str());
}
