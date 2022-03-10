# ReedsKeebs
This repository contains all working firmware for my boards and design files I have made public.  

If you have a KB2040 and an Alish board, follow these instructions for installation of KMK firmware.  

1. Plug KB2040 DIRECTLY into your computer, USB hubs can cause issues.  
2. Download the CircuitPython installer, a .UF2 file, from https://circuitpython.org/board/adafruit_kb2040/
3. Enter Bootloader mode on the KB2040 by pressing and holding the BOOT button then pressing the RST button. 
4. The KB2040 should reboot. You will then find it in your storage devices labeled RP2 BOOT / RPI-RP2.
5. Copy and paste the .UF2 file from earlier into the RPI-RP2 device.
6. The device should reboot and will appear in your storage devices as CIRCUITPY.
7. Download this repository by clicking the green "Code" button in the top right, then downloading as a .zip.
8. Unzip the folder using you're preferred program. 
9. Drag all contents from the Alish KMK Firmware folder (not the folder itself) to the CIRCUITPY drive.
10. Verify that there is not a red blinking light on the KB2040. 
11. Congratulations, you now have a fully functional KB2040.



I do not take credit for the files within this repository, I haven't coded anything beyond the code.py file, everything else is from the official kmk_firmware repository.

You can find the kmk_firmware repository HERE: https://github.com/KMKfw/kmk_firmware
I have only included all files necessary to help provide a trouble free installation. 
