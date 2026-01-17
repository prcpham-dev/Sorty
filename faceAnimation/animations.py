from PIL import Image, ImageSequence

OLED_SIZE = (128, 64)

def load_gif(path):
    gif = Image.open(path)
    frames = []

    for frame in ImageSequence.Iterator(gif):
        f = frame.convert("L")
        f = f.resize(OLED_SIZE)
        f = f.point(lambda x: 0 if x > 180 else 255)
        f = f.convert("1")
        frames.append(f)
    return frames

class Animation:
    def __init__(self, frames, loop=True):
        self.frames = frames
        self.index = 0
        self.loop = loop

    def reset(self):
        self.index = 0

    def next_frame(self):
        frame = self.frames[self.index]
        self.index += 1

        if self.index >= len(self.frames):
            if self.loop:
                self.index = 0
            else:
                return None
            
        return frame
    
class Animator:
    def __init__(self, animations, default="idle"):
        self.animations = animations
        self.default = default
        self.current = animations[default]
        self.current_name = default

    def switch(self, name):
        self.current_name = name
        self.current = self.animations[name]
        self.current.reset()

    def update(self):
        frame = self.current.next_frame()
        if frame is None:
            self.switch(self.default)
            frame = self.current.next_frame()
        return frame
    