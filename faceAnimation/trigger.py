import queue, sys

events = queue.Queue()

def trigger(name):
    """
    Public API to trigger an animation.
    Can be called from anywhere.
    """
    events.put(name)

def start_listener():
    """
    Temporary ENTER listener.
    Replace later with GPIO / audio / AI.
    """
    print("Press ENTER to say NO")
    while True:
        sys.stdin.readline()
        events.put("no")
