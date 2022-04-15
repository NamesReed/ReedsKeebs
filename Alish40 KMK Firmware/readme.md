## If you have a KB2040 and an Alish board, follow these instructions for installation of KMK firmware.

1. Plug KB2040 DIRECTLY into your computer, USB hubs can cause issues.
2. Download the CircuitPython installer, a .UF2 file, from https://circuitpython.org/board/adafruit_kb2040/
3. Enter Bootloader mode on the KB2040 by pressing and holding the BOOT button then pressing the RST button.
4. The KB2040 should reboot. You will then find it in your storage devices labeled RP2 BOOT / RPI-RP2.
5. Copy and paste the .UF2 file from earlier into the RPI-RP2 device.
6. The device should reboot and will appear in your storage devices as CIRCUITPY.
7. Download the kmk_firmware repository, found here: https://github.com/KMKfw/kmk_firmware by clicking the green "Code" button, and downloading the .zip.
8. Unzip the folder using your preferred program.
9. Drag the folder titled "kmk", NOT THE ENTIRE MASTER DIRECTORY, to the CIRCUITPY drive.
10. Drag the "boot.py" file to the CIRCUITPY drive.
11. Download this repository just like you did the kmk_firmware repo, and proceed to unzip the folder.
12. Drag the "main.py" file located within the AlishKMKFirmware folder to the CIRCUITPY drive, this should be on the same level as the boot.py file, not within the kmk folder.
13. Congratulations, you now have a fully functional KB2040.

Github won't allow me to just upload the files you need, so unfortunately you need to download the entire KMK repo.
