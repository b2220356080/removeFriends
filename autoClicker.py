import pyautogui
import keyboard


def on_key(event):
    if event.name == "q":
        exit()


def removeFriend(amount):
    for i in range(amount):
        pyautogui.moveTo(1479, 382, duration=0.8)  # Move the mouse smoothly to the target area
        pyautogui.click(button='right')
        pyautogui.moveTo(1387, 569, duration=0.1)  # Move the mouse smoothly to the target area
        pyautogui.click()
        pyautogui.moveTo(883, 446, duration=0.1)  # Move the mouse smoothly to the target area
        pyautogui.click()


removeFriend(1)
keyboard.on_press(on_key)
keyboard.wait('q')
