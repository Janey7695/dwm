#!/bin/bash

while true
do
		python3 ~/.local/share/dwm/pic_build.py > ~/.local/share/dwm/log3
		feh --bg-fill ~/Pictures/eva-wallpaper/pic2.png
		sleep 300 
done
