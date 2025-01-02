from pynput.keyboard import Key, Listener, KeyCode
import time, sys

pressed = []

f = open("output", "w")

starttime = time.time()

recording = False


def on_press(key):
    global recording, starttime, pressed, f

    if key == Key.f10:
        if recording:
            print("stoping")
            f.close()
            sys.exit(0)
        else:
            starttime = time.time()
            recording = True
            print("starting")
    elif recording:
        try:
            if not key.char in pressed:
                f.write(str(time.time()-starttime) + "\tP\t" + key.char + "\n")
                pressed.append(key.char)
        except AttributeError:
            if key == Key.space:
                f.write(str(time.time()-starttime) + "\tP\t<space>\n")
                pressed.append("<space>")
            elif key == Key.tab:
                f.write(str(time.time()-starttime) + "\tP\t<tab>\n")
                pressed.append("<tab>")
            elif key == Key.enter:
                f.write(str(time.time()-starttime) + "\tP\t<enter>\n")
                pressed.append("<enter>")
            elif key == Key.esc:
                f.write(str(time.time()-starttime) + "\tP\t<esc>\n")
                pressed.append("<esc>")

def on_release(key):
    global recording, starttime, pressed, f

    if recording:
        try:
            f.write(str(time.time()-starttime) + "\tR\t" + key.char + "\n")
            pressed.remove(key.char)
        except AttributeError:
            if key == Key.space:
                f.write(str(time.time()-starttime) + "\tR\t<space>\n")
                pressed.remove("<space>")
            elif key == Key.tab:
                f.write(str(time.time()-starttime) + "\tR\t<tab>\n")
                pressed.remove("<tab>")
            elif key == Key.enter:
                f.write(str(time.time()-starttime) + "\tR\t<enter>\n")
                pressed.remove("<enter>")
            elif key == Key.esc:
                f.write(str(time.time()-starttime) + "\tR\t<esc>\n")
                pressed.remove("<esc>")

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
