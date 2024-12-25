import pyautogui
from pynput import keyboard
import json
import time

# Load configuration from the JSON file
with open("config.json", "r") as f:
    config = json.load(f)

hotkeys = config["hotkeys"]
delay = config["delay"]

# Shared state to communicate between threads
state = {'mode': 'idle', 'running': True, 'released': False}

def on_press(key):
    try:
        char = key.char
        if char == hotkeys['right_click']:
            state.update({'mode': 'right_click', 'released': False})
            print("Mode switched to: Hold Right Click")
        elif char == hotkeys['left_click']:
            state.update({'mode': 'left_click', 'released': False})
            print("Mode switched to: Hold Left Click")
        elif char == hotkeys['idle']:
            state.update({'mode': 'idle', 'released': False})
            print("Mode switched to: Idle")
        elif char == hotkeys['quit']:
            state['running'] = False
            print("Exiting program.")
    except AttributeError:
        pass

def main():
    print(f"Hotkeys: {hotkeys}")
    print("Press the configured keys to control the script. Refer to 'config.json' for settings.")

    with keyboard.Listener(on_press=on_press) as listener:
        while state['running']:
            if state['mode'] == 'right_click':
                pyautogui.mouseUp(button='left')
                pyautogui.mouseDown(button='right')
                state['released'] = False
            elif state['mode'] == 'left_click':
                pyautogui.mouseUp(button='right')
                pyautogui.mouseDown(button='left')
                state['released'] = False
            elif state['mode'] == 'idle' and not state['released']:
                pyautogui.mouseUp(button='left')
                pyautogui.mouseUp(button='right')
                state['released'] = True
            time.sleep(delay)

if __name__ == "__main__":
    main()