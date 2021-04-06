import pynput

from pynput.keyboard import Key, Listener

keysPressed = []


def on_press(key):
    try:
        keysPressed.append(key.char)
    except AttributeError:
        keysPressed.append(f'\n{str(key).upper()}\n')


def on_release(key):
    if key == Key.esc:
        print(f"Keys pressed:\n{''.join(keysPressed)}")
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
