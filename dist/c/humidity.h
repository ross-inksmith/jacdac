// Autogenerated C header file for Humidity
#ifndef _JACDAC_SPEC_HUMIDITY_H
#define _JACDAC_SPEC_HUMIDITY_H 1

#define JD_SERVICE_CLASS_HUMIDITY  0x16c810b8

/**
 * Read-only %RH u22.10 (uint32_t). The relative humidity in percentage of full water saturation.
 */
#define JD_HUMIDITY_REG_HUMIDITY JD_REG_READING

/**
 * Read-only %RH u22.10 (uint32_t). The real humidity is between `humidity - humidity_error` and `humidity + humidity_error`.
 */
#define JD_HUMIDITY_REG_HUMIDITY_ERROR JD_REG_READING_ERROR

#endif
