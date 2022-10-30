#!/bin/bash

exec wmname LG3D & 
exec picom -b &
exec slstatus &
exec fcitx &
/bin/bash ~/.local/share/dwm/autolock.sh &
/bin/bash ~/.local/share/dwm/autofeh.sh &


