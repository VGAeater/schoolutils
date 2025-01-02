#!/usr/bin/python3

import subprocess, random, time, os


def auto_type(text, delay=2, speed=150, speed_deviation=0.4, block_size=20, block_size_deviation=0.5, pause_chance=0.2, pause_length=2, pause_length_deviation=2):
    text = text.replace("’", "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('÷', '/');
    for i in range(delay, 0, -1):
        print(i)
        time.sleep(1)

    print("GO!")
    while not len(text) == 0:
        cur_speed = int(speed + speed * speed_deviation * (random.random() * 2 - 1))
        cur_block_size = int(block_size + block_size * block_size_deviation * (random.random() * 2 - 1))
        cur_text = text[:cur_block_size]
        text = text[cur_block_size:]
        if random.random() <= pause_chance:
            time.sleep(max(0, pause_length + pause_length * pause_length_deviation * (random.random() * 2 - 1)))
        ps = subprocess.Popen(('ydotool', 'type', '--key-delay', str(cur_speed), cur_text))
        ps.wait()


running = True

while running:
    command = input("$ ")
    command = command.split()
    match command[0]:
        case "help":
            print("""
exit            :       exit
gen_gpt         :       generate a chatgpt prompt
help            :       shows this screen
type            :       types in a realistic way
type_advanced   :       ^ but more options
""")
        case "exit":
            running = False
        case "type":
            print("Enter text: ", end="")
            text = ""
            try:
                while True:
                    text += input() + "\n"
            except KeyboardInterrupt:
                pass
            auto_type(text);

        case "type_advanced":
            print("Enter text: ", end="")
            text = ""
            try:
                while True:
                    text += input() + "\n"
            except KeyboardInterrupt:
                pass
            delay =                       int(input("Start delay (seconds)[5]: ").strip() or "5")
            speed =                     float(input("Text speed (millis)[120]: ").strip() or "120")
            speed_deviation =           float(input("Text speed deviation (percent)[40]: ").strip() or "40")/100
            block_size =                float(input("Speed block size (chars)[20]: ").strip() or "20")
            block_size_deviation =      float(input("Speed block size deviation (percent)[50]: ").strip() or "50")/100
            pause_chance =              float(input("Block size (percent)[10]: ").strip() or "20")/100
            pause_length =              float(input("Block size (seconds)[2]: ").strip() or "2")
            pause_length_deviation =    float(input("Block size (percent)[200]: ").strip() or "200")/100
            
            auto_type(text, delay, speed, speed_deviation, block_size, block_size_deviation, pause_chance, pause_length, pause_length_deviation)

        case "gen_gpt":
            materials = ""
            questions = ""
            print("paste all materials CTRL-C when done -> ")
            try:
                while True:
                    materials += input()
            except KeyboardInterrupt:
                pass
            print("paste all questions CTRL-C when done -> ")
            try:
                while True:
                    questions += input()
            except KeyboardInterrupt:
                pass

            print("-"*os.get_terminal_size().columns)
            print("Make all your responces with the following style of writing:\n")
            with open("sample.txt", "r") as file:
                print(file.read())
            print("-"*os.get_terminal_size().columns)
            print("Use the following material answer the questions in the next message:\n")
            print(materials)
            print("-"*os.get_terminal_size().columns)
            print(questions)
            print("-"*os.get_terminal_size().columns)


