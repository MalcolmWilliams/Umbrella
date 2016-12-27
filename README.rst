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

The program will be written in microPython. 

Uploading Code
**************

The board first needs to have the microPython bootloader installed. Instructions are located `here <https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266:q>`_
The following commands can be used to upload the firmware. 

.. code-block::

    esptool.py --port /path/to/ESP8266 erase_flash
    esptool.py --port /path/to/ESP8266 --baud 460800 write_flash --flash_size=detect 0 firmware.bin

Then code can be ran with the following `guide <https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy>`_

or with the shortcut script ``./run.sh``
