import webbrowser
import win32clipboard
import keyboard
import pyautogui

KEY = '`'
get_search_url = lambda keyword: f"https://google.com/search?q={keyword}"

def get_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    return data

def copy():
    pyautogui.hotkey('ctrl','c')

def google_it(keyword):
    webbrowser.open(get_search_url(keyword))

def on_press(_):
    copy()
    copied = get_clipboard()
    google_it(copied)

keyboard.on_press_key(key, on_press)

