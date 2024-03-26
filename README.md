# air-pollution-monitoring-system-using-iot
# Gas Sensor Monitoring System

This Arduino project is designed to monitor air quality using MQ135 and MQ6 gas sensors. It displays real-time sensor readings on an LCD screen, triggers an alarm if the air quality surpasses predefined thresholds, and allows users to adjust these thresholds using a keypad.

## Features

- Readings of MQ135 and MQ6 sensors displayed on an LCD screen.
- Alarm triggered (LED flashing and buzzer sounding) when sensor readings exceed predefined thresholds.
- Threshold adjustment functionality using a keypad.
- Log sensor data to the serial monitor for debugging.

## Components Used

- Arduino Uno
- MQ135 Gas Sensor
- MQ6 Gas Sensor
- 16x2 LCD Display with I2C Backpack
- LED and Buzzer for Alarm
- 4x4 Keypad

## Installation

1. Clone this repository to your local machine.
2. Open the Arduino IDE.
3. Include the necessary libraries (`Wire`, `LiquidCrystal_I2C`, `MQ135`, `MQ6`, `Keypad`).
4. Upload the code to your Arduino board.

## Usage

1. Connect the sensors, LCD, LED, buzzer, and keypad according to the schematic.
2. Power up the Arduino board.
3. Monitor the air quality readings displayed on the LCD.
4. If the readings exceed the predefined thresholds, an alarm will be triggered.
5. Use the keypad to adjust the thresholds if necessary.



## Contributors

- [jithendra](https://github.com/jithendra)


