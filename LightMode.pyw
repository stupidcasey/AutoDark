import winreg
import pyautogui
import sys
import ctypes

pyautogui.FAILSAFE = False

sys.stdout = open('output_log.txt', 'w')
sys.stderr = open('error_log.txt', 'w')



def enable_dark_mode():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize',
                             0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'AppsUseDarkTheme', 0, winreg.REG_DWORD, 0)
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

def set_registry_value(key_path, value_name, value_data, value_type=winreg.REG_SZ):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, value_name, 0, value_type, value_data)
        winreg.CloseKey(key)
        print(f"Registry key updated: {key_path}\\{value_name}")
    except Exception as e:
        print(f"Error updating registry key: {e}")


# for changing AccentColor in HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent





def set_wallpaper(image_path):
    try:
        SPI_SETDESKWALLPAPER = 20
        # Set the wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

        error_code = ctypes.GetLastError()
        error_message = ctypes.FormatMessageW(ctypes.FormatMessageW, 0, error_code)
        print(f"Error {error_code}: {error_message}")


        print("Wallpaper changed successfully.")
    except Exception as e:
        print(f"Error: {e}")

import winreg

def set_registry_value(key_path, value_name, value_data, value_type=winreg.REG_SZ):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, value_name, 0, value_type, value_data)
        winreg.CloseKey(key)
        print(f"Registry key updated: {key_path}\\{value_name}")
    except Exception as e:
        print(f"Error updating registry key: {e}")


enable_light_mode()

# Example usage for changing AccentColor in HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent
accent_color_key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent"
set_registry_value(accent_color_key_path, "AccentColor", 0xFFFFFF, winreg.REG_DWORD)

color_prevalence_key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
set_registry_value(color_prevalence_key_path, "ColorPrevalence", 0xFFFFFF, winreg.REG_DWORD)

# Replace 'path/to/your/image.jpg' with the actual path to your image file
image_path = r'C:\Windows\Web\Wallpaper\Theme1\BlueNight.jpg'
set_wallpaper(image_path)


