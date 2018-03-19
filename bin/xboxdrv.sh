#!/bin/sh
sudo /opt/retropie/supplementary/xboxdrv/bin/xboxdrv \
        --evdev /dev/input/event15 \
        --silent \
        --detach-kernel-driver \
        --force-feedback \
        --deadzone-trigger 15% \
        --deadzone 4000 \
        --mimic-xpad \
        --evdev-absmap ABS_X=x1,ABS_Y=y1,ABS_HAT0X=x2,ABS_HAT0Y=y2,ABS_Z=lt,ABS_RZ=rt,ABS_HAT0X=dpad_x,ABS_HAT0Y=dpad_y \
        --evdev-keymap BTN_SOUTH=a,BTN_EAST=b,BTN_NORTH=x,BTN_WEST=y,BTN_TL=lb,BTN_TR=rb,BTN_THUMBL=tl,BTN_THUMBR=tr,BTN_MODE=guide,BTN_SELECT=back,BTN_START=start \
        &


