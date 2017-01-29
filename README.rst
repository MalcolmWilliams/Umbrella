========
Umbrella
========

ESP8266 based smart umbrella for art show


Hardware
========

Prototyping is done on the `Adafruit HUZZAH ESP8266 Breakout <https://www.adafruit.com/product/2471>`_
The adafruit documentation is available here: https://learn.adafruit.com/adafruit-huzzah-esp8266-breakout/overview


Software
========

The program is written in Arduino with the help of platformio. 

Code written in microPython and Lua were also tested, but deemed to be less advantageous.

Uploading Code
**************

The board needs to be put in bootloader mode and then can be uploaded in a similar fashion to other arduino boards.
To put the board into bootloader mode:

1. Hold down reset button
2. Reset the board

To upload code, the script ``upload.sh`` can be run. Or the command ``platformio run -t upload`` can be run. 


PCB
===

The design was done in Altium 16. The project is located in ``./PCB/Smart_Umbrella_Altium/Smart_Umbrella/``.
Several of the board features include: LiPo battery charging, LED's, automatic bootloader mode, battery level sensing and IO breakouts. 
