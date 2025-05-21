import pyautogui
import time
import pyperclip

print("Hazırlan, Firefox başlatılıyor ve pencere büyütülüyor...")
time.sleep(0.2)

pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(1)
pyautogui.press('enter')

pyautogui.write('firefox --new-window --start-maximized', interval=0.01)
pyautogui.press('enter')

time.sleep(2)

pyautogui.hotkey('Ctrl', 'l')
time.sleep(0.12)
pyperclip.copy('https://visa.vfsglobal.com/tur/tr/aut/login')
pyautogui.hotkey('Ctrl', 'v')
time.sleep(0.13)
pyautogui.press('enter')
time.sleep(10)

for _ in range(3):
    pyautogui.press('tab')

pyperclip.copy('ersnozturkk@gmail.com')
pyautogui.hotkey('Ctrl', 'v')  

pyautogui.press('tab')

time.sleep(0.17)

pyperclip.copy('Newpass123*')
pyautogui.hotkey('Ctrl', 'v')

for _ in range(3):
    pyautogui.press('tab')

pyautogui.press('Space')


time.sleep(5)

for _ in range(4):
    pyautogui.press('tab')

pyautogui.press('enter')

time.sleep(5)

pyautogui.hotkey('Ctrl', 'a')  
pyautogui.hotkey('Ctrl', 'c')  
print(pyperclip.paste())


##pyautogui.hotkey('Alt', 'F4')
##time.sleep(1)
##pyautogui.hotkey('Alt', 'F4')


