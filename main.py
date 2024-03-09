import winreg
import time
import pyautogui
import subprocess


def enable_dark_mode():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize',
                             0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'AppsUseLightTheme', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Error: {e}")


def enable_light_mode():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize',
                             0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'AppsUseLightTheme', 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Error: {e}")


# Example: Toggle between light and dark mode
enable_dark_mode()


# Uncomment the line below to switch back to light mode
# enable_light_mode()


def set_registry_value(key_path, value_name, value_data, value_type=winreg.REG_SZ):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, value_name, 0, value_type, value_data)
        winreg.CloseKey(key)
        print(f"Registry key updated: {key_path}\\{value_name}")
    except Exception as e:
        print(f"Error updating registry key: {e}")


# Example usage for changing AccentColor in HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent
accent_color_key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent"
set_registry_value(accent_color_key_path, "AccentColor", 0x00FF00, winreg.REG_DWORD)

# Example usage for changing ColorPrevalence in HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize
color_prevalence_key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
set_registry_value(color_prevalence_key_path, "ColorPrevalence", 1, winreg.REG_DWORD)





def open_edge():
    time.sleep(2)
    # Replace 'msedge' with 'msedge.exe' if needed
    subprocess.Popen(['C:\Program Files (x86)\Microsoft\Edge\Application\msedge'])

def enable_dark_mode():
    # Adjust sleep time based on your system's responsiveness
    time.sleep(2)

    # Open Microsoft Edge
    open_edge()
    time.sleep(1)

    # Simulate pressing the hotkey to enable Dark Mode in Dark Reader
    pyautogui.hotkey('alt', 'shift', 'd')  # Replace 'your_custom_hotkey' with the actual hotkey

# Call the function to enable Dark Mode in Edge
enable_dark_mode()

