echo "Enter input rate: "
read rate 
xrandr --output HDMI-0 --mode 1920x1080 --rate $rate 
echo "Current refesh rate: " $rate 
echo close 
