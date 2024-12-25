#Just a silly autoclicker with hotkey configuration

## About This Project

This project is being documented as part of my practice in writing clean code and creating readable documentation. Its a simple script that I originally created mainly to automate some clicking in Minecraft. While it’s not complex, it’s a good way for me to get used to structuring small projects and making them easy for others (and future me) to read lol.
---

## Features

- **Customizable Hotkeys**: Configure keys for actions like right-click, left-click, idle mode, and quit.
- **Adjustable Delay**: Set the time interval between mouse actions.
- **Idle Mode**: Automatically releases mouse buttons when idle.
- **Easy Configuration**: All settings can be modified in the `config.json` file.

---

## Prerequisites

Before running the script make sure you have the following installed:

- Python 3.7 or higher
- Required Python libraries (`pyautogui`, `pynput`)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/autoclicker.git
   cd autoclicker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Edit the `config.json` file to set your desired hotkeys and delay (if needed).

---


## Usage

1. Run the script:
   ```bash
   python autoclicker.py
   ```

2. Use the configured hotkeys to control the script:
   - Press the hotkey for **Right Click** to hold down the right mouse button.
   - Press the hotkey for **Left Click** to hold down the left mouse button.
   - Press the hotkey for **Idle** to release all buttons.
   - Press the hotkey for **Quit** to exit the program.

---


## Packages Used

- [PyAutoGUI](https://pyautogui.readthedocs.io/) for automating mouse interactions.
- [Pynput](https://pynput.readthedocs.io/) for handling keyboard input.

