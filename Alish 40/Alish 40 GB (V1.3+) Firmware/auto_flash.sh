file=`mktemp XXXXXXX.hex` 
curl "https://raw.githubusercontent.com/NamesReed/ReedsKeebs/main/Alish%2040/Alish%2040%20GB%20(V1.3%2B)%20Firmware/reedskeebs_alish_via.hex" -o $file
ls /dev/tty* > /tmp/1
echo -n "Listening for Pro Micro port, reset your Pro Micro now."
while [ -z $USB ]; do
    sleep 0.1
    ls /dev/tty* > /tmp/2
    USB=`diff /tmp/1 /tmp/2 | grep -o '/dev/tty.*'`
done;
echo ""
echo "Detected Pro Micro port at $USB"
sleep 0.5
sudo avrdude -p atmega32u4 -c avr109 -P $USB -U flash:w:$file
