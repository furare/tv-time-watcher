from time import sleep
import pyautogui
import PySimpleGUI as sg 
import random
from datetime import datetime
import os

# 一桁同士の計算を作成する関数
def create_drill():
    return random.randint(1, 9), random.randint(1, 9)

# マウス操作でブラウザで再生している動画を一時停止/再生する関数
def pause_video():
    pyautogui.moveTo(200, 200)
    #pyautogui.click()
    pyautogui.moveTo(201, 201)
    pyautogui.click()

def active_drill():
    pyautogui.moveTo(600,400)
    pyautogui.click()

def close_browser():
    defalut_font = ('Helvetica', 25)

    layout = [
        [sg.Text('きょうはもうおしまいだよ', font=defalut_font)],
        [sg.Text('またあした　おやすみなさい', font=defalut_font)],
    ]
    window = sg.Window('おやすみなさい', layout=layout, keep_on_top=True).finalize()
    window.bring_to_front()
    sleep(2)
    os.system("taskkill /im chrome.exe /f")
    sleep(2)
    pyautogui.hotkey('win', 'l')

def main():
    if datetime.now().hour >= 21 and datetime.now().minute <= 30:
        close_browser()
        return
    elif datetime.now().hour >= 21 and datetime.now().hour < 5:
        return

    pause_video()
    x,y = create_drill()
    sg.theme('lightblue')
    defalut_font = ('Helvetica', 25)
    quiz_font = ('Helvetica', 50)
    submit_button = sg.Button('こたえる', font=defalut_font)
    submit_button.BindReturnKey = True

    layout = [
        [sg.Text('けいさんしてね', font=defalut_font)],
        [sg.Text('けいさんできたらテレビの続きがみれるよ', font=defalut_font)],
        [sg.Text(f'{x}', font=quiz_font ),
        sg.Text('+', font=quiz_font),
        sg.Text(f'{y}', font=quiz_font),
        sg.Text('=', font=quiz_font),
        sg.InputText(key='answer', font=quiz_font, size=(5, 1))
        ],
        [submit_button],
        [sg.Text('', key='result', font=defalut_font, text_color='pink')],
    ]
    window = sg.Window('かんいつーる', layout=layout, keep_on_top=True).finalize()
    window.bring_to_front()
    # window.maximize()
    active_drill()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, '終了'):
            break
        elif event == 'こたえる':
            answer = values['answer']
            if answer == '':
                window['result'].update('こたえをにゅうりょくしてね')
                continue
            if int(answer) == x + y:
                window['result'].update('せいかい！！！')
                window.refresh()
                sleep(1)
                pause_video()
                break
            else:
                window['result'].update('ちがうよ')


main()