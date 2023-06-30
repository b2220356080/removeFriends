import pyautogui
import keyboard


def on_key(event):
    if event.name == 'space':
        current_x, current_y = pyautogui.position()
        print(f"Current Mouse Position: X={current_x}, Y={current_y}")

    elif event.name == "q":
        exit()


keyboard.on_press(on_key)
keyboard.wait('q')
