from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

while 1:
    starttime = time.time()
    with open("output", "r") as f:
        for line in f.readlines():
            command = line.strip().split("\t")
            time.sleep(max(0,float(command[0])-time.time()+starttime))
            key = command[2]
            if key == "<space>":
                key = Key.space
            elif key == "<tab>":
                key = Key.tab
            elif key == "<enter>":
                key = Key.enter
            elif key == "<esc>":
                key = Key.esc
            print(command)
            if command[1] == "P":
                keyboard.press(key)
            else:
                keyboard.release(key)
    time.sleep(3)
