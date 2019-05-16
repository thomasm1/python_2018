/*
*  Matthew Richardson
*  matthewrichardson37<at>gmail.com
*  http://mattallen37.wordpress.com/
*  Initial date: May 28, 2013
*  Last updated: June 7, 2013
*
*  You may use this code as you wish, provided you give credit where it's due.
*
*  This library is specifically to be used with the BrickPi.
*
*  This is a library for reading the Lego Color sensor.
*/

#ifndef __BrickPiCS_h_
#define __BrickPiCS_h_

#include "Arduino.h"
#include "BrickPiA.h"

#define PORT_1 0
#define PORT_2 1

#define BLACK 1
#define BLUE 2
#define GREEN 3
#define YELLOW 4
#define RED 5
#define WHITE 6

#define RED_INDEX 0
#define GREEN_INDEX 1
#define BLUE_INDEX 2
#define BLANK_INDEX 3

#define TYPE_COLORFULL 13
#define TYPE_COLORRED 14
#define TYPE_COLORGREEN 15
#define TYPE_COLORBLUE 16
#define TYPE_COLORNONE 17

#define ADVOLTS 3300
#define ADMAX 1023
#define SENSORMAX ADMAX
#define MINBLANKVAL (214 / (ADVOLTS / ADMAX))

#define CAL_COLUMNS 4
#define CAL_ROWS 3
#define CAL_LIMITS 2

#define CS_SET_CLOCK_INPUT             \
(DDRC &= (~(0x04 << CS_PORT)))

#define CS_SET_CLOCK_OUTPUT            \
(DDRC |= (0x04 << CS_PORT))

#define CS_SET_CLOCK_HIGH              \
CS_SET_CLOCK_OUTPUT;                   \
PORTC |= (0x04 << CS_PORT);

#define CS_SET_CLOCK_LOW               \
CS_SET_CLOCK_OUTPUT;                   \
PORTC &= (~(0x04 << CS_PORT));

#define CS_SET_CLOCK(state)            \
CS_SET_CLOCK_OUTPUT;                   \
if(state){PORTC |= (0x04 << CS_PORT);} \
else{PORTC &= (~(0x04 << CS_PORT));}

#define CS_SET_DATA_INPUT              \
(DDRC &= (~(0x01 << CS_PORT)))

#define CS_SET_DATA_OUTPUT             \
DDRC |= (0x01 << CS_PORT);

#define CS_SET_DATA_HIGH               \
CS_SET_DATA_OUTPUT;                    \
PORTC |= (0x01 << CS_PORT);

#define CS_SET_DATA_LOW                \
CS_SET_DATA_OUTPUT;                    \
PORTC &= (~(0x01 << CS_PORT));

#define CS_SET_DATA(state)             \
CS_SET_DATA_OUTPUT;                    \
if(state){PORTC |= (0x01 << CS_PORT);} \
else{PORTC &= (~(0x01 << CS_PORT));}

inline uint8_t CS_GET_DATA();
inline uint16_t CS_READ_DATA();

// Access from user program
void     CS_Begin(uint8_t port, uint8_t modetype);
uint16_t CS_Update(uint8_t port);
void     CS_KeepAlive(uint8_t port);   // Simulate reading the sensor, so that it doesn't time-out.
extern uint16_t CS_Values[2][4];

// Only for use by this library
void     CS_Reset();
void     CS_SendMode(uint8_t mode);
char     CS_ReadByte();
uint16_t CS_CalcCRC(uint16_t crc, uint16_t val);
bool     CS_ReadCalibration();
int      CS_Calibrate();
uint8_t  CS_CalToColor();

static uint32_t calData[2][CAL_ROWS][CAL_COLUMNS];
static int32_t  calLimits[2][CAL_LIMITS];
static uint16_t raw_values[2][4];
static uint16_t cal_values[2][4];
static uint16_t type[2];

static uint8_t CS_PORT;           // The port currently being used

#endif