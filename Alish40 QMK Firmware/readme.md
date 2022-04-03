# Follow these instructions if you want a gui to change your keymap!

# Use the .hex if you have a pro micro, use the uf2 if you have a kb2040
Scroll to the bottom for KB2040 Vial firmware instructions

### This installation will provide you the ability to change your keymap on the fly without reflashing with the use of Vial, a VIA alternative.

1. Download this repository by going back to the main page, and clicking the green "Code" button, then downloading as .zip.
2. Unzip the file using whatever software you like, 7ZIP, WinRar, ect.
3. Download QMK Toolbox at this link, https://github.com/qmk/qmk_toolbox/releases 
4. Find the latest release, the file should look something like "qmk_toolbox.exe"
5. Now, plug your pro micro into your computer, DO NOT USE A USB HUB.
6. Find the reedskeebs_alish_vial.hex within QMK toolbox under the Local Files section.
7. Check the "Auto Flash" button.
8. Select the MCU as "atmega32u4" if it is not already.
9. At this point, QMK Toolbox should be properly configured, and look like this
![image](https://user-images.githubusercontent.com/36281259/158075587-73514396-c388-4b16-8fe6-5bac3371947a.png)
9. Now, locate the RST and GND pins on the pro micro.


![image](https://user-images.githubusercontent.com/36281259/158075737-5598f20d-7a2c-446b-86c6-a1aa1082fef9.png)


10. Short the RST and GND pins using a paperclip, tweezers, or something similiar.
11. This puts the Pro Micro into bootloader mode, and automatically starts flashing the firmware.
12. It should now look like this if flashed successfully 


![image](https://user-images.githubusercontent.com/36281259/158075867-bb88d0c1-fb34-4a25-b287-4ce76df80d88.png)

13. If it did not flash, retry shorting the pins, sometimes it takes a few tries.
15. Congrats! You can now continue with the rest of the build.

## KB2040 Vial Firmware Instructions

If you have a KB2040 and would like Vial, read this guide

Download the Vial_Alish_KB2040 ONLY IF YOU HAVE A KB2040 Hold down the BOOT button on your KB2040, then press the Reset button. This puts the board into bootloader, you should see a new "drive" on your computer labeled something like "UF2 Bootloader" Drag the Vial_Alish_KB2040.uf2 file to the new drive.

Wait a few moments, now your KB2040 is flashed with Vial firmware, easily change your keymap by downloading the Vial gui.
