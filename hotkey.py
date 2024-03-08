import pygetwindow as gw
import pyautogui
import time

def toggle_dark_mode():
    # Open Settings
    settings_window = gw.getWindowsWithTitle('Settings')[0]
    settings_window.activate()

    # Wait for Settings to open
    time.sleep(1)

    # Navigate to Personalization -> Colors
    pyautogui.hotkey('alt', 'e')
    pyautogui.press('c')

    # Wait for Colors page to load
    time.sleep(1)

    # Toggle between Light and Dark mode
    pyautogui.press('tab')
    pyautogui.press('space')

# Example: Toggle between light and dark mode
toggle_dark_mode()
