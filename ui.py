import time, threading
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1309

from faceAnimation.animations import *
from trigger import events, responses, start_listener

serial = i2c(port=1, address=0x3C)
device = ssd1309(serial, width=128, height=64)

idle = Animation(load_gif("assets/idle.gif"), loop=True)
no = Animation(load_gif("assets/no.gif"), loop=True)

animator = Animator(
    {
        "idle": idle,
        "no": no
    },
    default="idle"
)

threading.Thread(
    target=start_listener,
    daemon=True
).start()

FPS = 25
FRAME_DELAY = 1 / FPS
last_frame = None

while True:
    while not events.empty():
        animator.switch(events.get_nowait())

    while not responses.empty():
        response = responses.get_nowait()
        print(response)

    frame = animator.update()

    if frame is not last_frame:
        device.display(frame)
        last_frame = frame

    time.sleep(FRAME_DELAY)
