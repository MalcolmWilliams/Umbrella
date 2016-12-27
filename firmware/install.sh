#!/bin/bash
read -p "Put the esp8266 into bootloader mode. Press 'Enter' when ready..." temp
esptool.py --port /dev/ttyUSB0 erase_flash
read -p "Restart the esp8266 and put it back into bootloader mode. Press 'Enter' when ready..." temp
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20161110-v1.8.6.bin

