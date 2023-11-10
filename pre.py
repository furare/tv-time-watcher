from time import sleep
import pyautogui
import PySimpleGUI as sg 
import random
from datetime import datetime
import os

def notice(minute: int):
    defalut_font = ('Helvetica', 25)

    layout = [
        [sg.Text('そろそろおわりだよ', font=defalut_font)],
        [sg.Text(f'あと {minute} でテレビはおしまいだよ', font=defalut_font)],
    ]
    window = sg.Window('ねるじゅんびをはじめよう', layout=layout, keep_on_top=True).finalize()
    window.bring_to_front()
    sleep(5)

def main():
    if datetime.now().hour >= 20 and datetime.now().hour < 21:
        notice(datetime.now().minute)
    else:
        pass

main()