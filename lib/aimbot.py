import ctypes
import cv2
import json
import math
import mss
import os
import sys
import time
import torch
import numpy as np
import uuid
import win32api
import random
import string  # Import string module for generating random strings
from termcolor import colored
from ultralytics import YOLO

# Auto Screen Resolution
screensize = {'X': ctypes.windll.user32.GetSystemMetrics(0), 'Y': ctypes.windll.user32.GetSystemMetrics(1)}

# If you use stretched res, hardcode the X and Y. For example: screen_res_x = 1234
screen_res_x = screensize['X']
screen_res_y = screensize['Y']

# Divide screen_res by 2
screen_x = int(screen_res_x / 2)
screen_y = int(screen_res_y / 2)

aim_height = 10  # The lower the number, the higher the aim_height. For example: 2 would be the head and 100 would be the feet.

confidence = 0.45  # How confident the AI needs to be for it to lock on to the player. Default is 45%

use_trigger_bot = True  # Will shoot if crosshair is locked on the player

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

class Aimbot:
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    screen = mss.mss()
    pixel_increment = 1  # controls how many pixels the mouse moves for each relative movement
    with open("lib/config/config.json") as f:
        sens_config = json.load(f)
    aimbot_status = colored("ENABLED", 'green')

    def __init__(self, box_constant=350, collect_data=False, mouse_delay=0.0009):
        self.box_constant = box_constant  # controls the size of the detection box (equaling the width and height)

        print("[INFO] Loading the neural network model")
        self.model = YOLO('lib/best.pt')
        if torch.cuda.is_available():
            print(colored("CUDA ACCELERATION [ENABLED]", "green"))
        else:
            print(colored("[!] CUDA ACCELERATION IS UNAVAILABLE", "red"))
            print(colored("[!] Check your PyTorch installation, else performance will be poor", "red"))

        self.conf = confidence  # base confidence threshold (or base detection (0-1)
        self.iou = 0.80  # NMS IoU (0-1)
        self.collect_data = collect_data
        self.mouse_delay = mouse_delay

        print("\n[INFO] PRESS 'F1' TO TOGGLE AIMBOT\n[INFO] PRESS 'F2' TO QUIT")

    def update_status_aimbot(self):
        if Aimbot.aimbot_status == colored("ENABLED", 'green'):
            Aimbot.aimbot_status = colored("DISABLED", 'red')
        else:
            Aimbot.aimbot_status = colored("ENABLED", 'green')
        sys.stdout.write("\033[K")
        print(f"[!] AIMBOT IS [{Aimbot.aimbot_status}]", end="\r")

    def left_click(self):
        ctypes.windll.user32.mouse_event(0x0002)  # left mouse down
        Aimbot.sleep(0.0001)
        ctypes.windll.user32.mouse_event(0x0004)  # left mouse up

    def sleep(self, duration):
        if duration == 0: return
        time.sleep(duration)

    def random_delay(self, min_delay=0.0005, max_delay=0.0015):
        return random.uniform(min_delay, max_delay)

    def is_aimbot_enabled(self):
        return Aimbot.aimbot_status == colored("ENABLED", 'green')

    def is_shooting(self):
        return win32api.GetKeyState(0x01) in (-127, -128)
    
    def is_targeted(self):
        return win32api.GetKeyState(0x02) in (-127, -128)

    def is_target_locked(self, x, y):
        # plus/minus 5 pixel threshold
        threshold = 5
        return screen_x - threshold <= x <= screen_x + threshold and screen_y - threshold <= y <= screen_y + threshold

    def ease_in_out_quad(self, t):
        if t < 0.5:
            return 2 * t * t
        else:
            return -1 + (4 * t) - (2 * t * t)

    def move_crosshair(self, x, y):
        if not Aimbot.is_targeted():
            return

        scale = Aimbot.sens_config["targeting_scale"]
        target_x = (x - screen_x) * scale
        target_y = (y - screen_y) * scale

        distance = int(math.dist((0, 0), (target_x, target_y)))
        steps = max(1, distance // 5)  # Determine the number of steps
        for i in range(steps + 1):
            t = self.ease_in_out_quad(i / steps)  # Eased time parameter
            eased_x = int(target_x * t)
            eased_y = int(target_y * t)

            Aimbot.ii_.mi = MouseInput(eased_x, eased_y, 0, 0x0001, 0, ctypes.pointer(Aimbot.extra))
            input_obj = Input(ctypes.c_ulong(0), Aimbot.ii_)
            ctypes.windll.user32.SendInput(1, ctypes.byref(input_obj), ctypes.sizeof(input_obj))
            Aimbot.sleep(self.random_delay())  # Use random delay

    def start(self):
        print("[INFO] Beginning screen capture")
        Aimbot.update_status_aimbot()
        half_screen_width = ctypes.windll.user32.GetSystemMetrics(0) / 2
        half_screen_height = ctypes.windll.user32.GetSystemMetrics(1) / 2
        detection_box = {'left': int(half_screen_width - self.box_constant // 2),  # x1 coord (for top-left corner of the box)
                         'top': int(half_screen_height - self.box_constant // 2),  # y1 coord (for top-left corner of the box)
                         'width': int(self.box_constant),  # width of the box
                         'height': int(self.box_constant)}  # height of the box

        while True:
            start_time = time.perf_counter()
            frame = np.array(Aimbot.screen.grab(detection_box))
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            boxes = self.model.predict(source=frame, verbose=False, conf=self.conf, iou=self.iou, half=True)
            result = boxes[0]
            if len(result.boxes.xyxy) != 0:  # player detected
                least_crosshair_dist = closest_detection = player_in_frame = False
                for box in result.boxes.xyxy:  # iterate over each player detected
                    x1, y1, x2, y2 = map(int, box)
                    x1y1 = (x1, y1)
                    x2y2 = (x2, y2)
                    height = y2 - y1
                    relative_head_X, relative_head_Y = int((x1 + x2) / 2), int((y1 + y2) / 2 - height / aim_height)  # offset to roughly approximate the head using a ratio of the height
                    own_player = x1 < 15 or (x1 < self.box_constant / 5 and y2 > self.box_constant / 1.2)  # helps ensure that your own player is not regarded as a valid detection

                    # calculate the distance between each detection and the crosshair at (self.box_constant/2, self.box_constant/2)
                    crosshair_dist = math.dist((relative_head_X, relative_head_Y), (self.box_constant / 2, self.box_constant / 2))

                    if not least_crosshair_dist: least_crosshair_dist = crosshair_dist  # initialize least crosshair distance variable first iteration

                    if crosshair_dist <= least_crosshair_dist and not own_player:
                        least_crosshair_dist = crosshair_dist
                        closest_detection = {"x1y1": x1y1, "x2y2": x2y2, "relative_head_X": relative_head_X, "relative_head_Y": relative_head_Y}

                    if own_player:
                        own_player = False
                        if not player_in_frame:
                            player_in_frame = True

                if closest_detection:  # if valid detection exists
                    cv2.circle(frame, (closest_detection["relative_head_X"], closest_detection["relative_head_Y"]), 5, (115, 244, 113), -1)  # draw circle on the head

                    # draw line from the crosshair to the head
                    cv2.line(frame, (closest_detection["relative_head_X"], closest_detection["relative_head_Y"]), (self.box_constant // 2, self.box_constant // 2), (244, 242, 113), 2)

                    absolute_head_X, absolute_head_Y = closest_detection["relative_head_X"] + detection_box['left'], closest_detection["relative_head_Y"] + detection_box['top']
                    x1, y1 = closest_detection["x1y1"]

                    if Aimbot.is_target_locked(absolute_head_X, absolute_head_Y):
                        if use_trigger_bot and not Aimbot.is_shooting():
                            Aimbot.left_click()

                        cv2.putText(frame, "LOCKED", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (115, 244, 113), 2)  # draw the confidence labels on the bounding boxes
                    else:
                        cv2.putText(frame, "TARGETING", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (115, 113, 244), 2)  # draw the confidence labels on the bounding boxes

                    if Aimbot.is_aimbot_enabled():
                        Aimbot.move_crosshair(absolute_head_X, absolute_head_Y)

            cv2.putText(frame, f"FPS: {int(1 / (time.perf_counter() - start_time))}", (5, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (113, 116, 244), 2)
            cv2.imshow("Lunar Vision", frame)
            if cv2.waitKey(1) & 0xFF == ord('0'):
                break

    def clean_up(self):
        print("\n[INFO] F2 WAS PRESSED. QUITTING...")
        Aimbot.screen.close()
        os._exit(0)

def generate_random_string(length=45):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("You are in the wrong directory and are running the wrong file; you must run lunar.py")

    # Generate a new random string
    new_string = generate_random_string()

    # Append the new string to the bottom of the code file
    filename = __file__
    with open(filename, 'a') as file:
        file.write(f'\n# New String: {new_string}\n')

    # Start the aimbot if needed
    aimbot = Aimbot()
    aimbot.start()
