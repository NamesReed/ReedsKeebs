# Follow these instructions if you want a gui to change your keymap!

### This installation will provide you the ability to change your keymap on the fly without reflashing with the use of VIA.

Save the [reedskeebs_alish_via.hex](https://github.com/NamesReed/ReedsKeebs/raw/main/Alish%2040/Alish%2040%20GB%20(V1.3%2B)%20Firmware/reedskeebs_alish_via.hex) to your computer. Remember where you put it.

## Windows/MacOS
1. Download and install [the latest release of QMK Toolbox using this link](https://github.com/qmk/qmk_toolbox/releases).
2. Find the latest release, the file should look something like "qmk_toolbox.exe"
3. Now, plug your pro micro into your computer, DO NOT USE A USB HUB.
4. Find the reedskeebs_alish_via.hex within QMK toolbox under the Local Files section.
5. Check the "Auto Flash" button.
6. Select the MCU as "atmega32u4" if it is not already.
7. At this point, QMK Toolbox should be properly configured, and look like this
![image](https://user-images.githubusercontent.com/36281259/158075587-73514396-c388-4b16-8fe6-5bac3371947a.png)
8. Now, locate the RST and GND pins on the pro micro.


![image](https://user-images.githubusercontent.com/36281259/158075737-5598f20d-7a2c-446b-86c6-a1aa1082fef9.png)


9. Short the RST and GND pins using a paperclip, tweezers, or something similiar.
10. This puts the Pro Micro into bootloader mode, and automatically starts flashing the firmware.
11. It should now look like this if flashed successfully 


![image](https://user-images.githubusercontent.com/36281259/158075867-bb88d0c1-fb34-4a25-b287-4ce76df80d88.png)

12. If it did not flash, retry shorting the pins, sometimes it takes a few tries.
## Linux
1. Follow steps 2 and 3 of [the QMK setup instructions linked here](https://docs.qmk.fm/#/newbs_getting_started) to install all prerequisites and flashing tools.
2. Plug your pro micro into your computer, DO NOT USE A USB HUB.
3. Run the command `qmk flash /path/to/reedskeebs_alish_via.hex`.
4. When prompted, short the RST and GND pins using a paperclip, tweezers, or something similiar.
