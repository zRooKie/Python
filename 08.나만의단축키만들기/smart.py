from pynput.keyboard import Key, Listener, KeyCode
# pip install pypiwin32
import win32api

MY_HOT_KEYS = [
 #   {"function1": {Key.ctrl_l, Key.alt_l, KeyCode(char="n")}},   # left ctrl + left alt + 'n' 누르면 함수 실행
 #   {"function2": {Key.shift, Key.ctrl_l, KeyCode(char="b")}},
 #   {"function3": {Key.alt_l, Key.ctrl_l, KeyCode(char="g")}}

    {"function1": {Key.ctrl_l, Key.alt_l, KeyCode(78)}},   # left ctrl + left alt + 'n' 누르면 함수 실행
    {"function2": {Key.shift, Key.ctrl_l, KeyCode(char="\x02")}},
    {"function3": {Key.alt_l, Key.ctrl_l, KeyCode(71)}}

]    
    
# 계속해서 눌러진 키가 있다면 중복을 없애기 위해 집합으로 생성 : 집합은 중복을 없앤다.
current_keys = set()

def function1():
    # print("함수1 호출")
    win32api.WinExec("calc.exe")
    
def function2():
    print("함수2 호출")
    win32api.WinExec("notepad.exe")

def function3():
    print("함수2 호출")
    win32api.WinExec("c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

def key_pressed(key):
    print("Pressed {}".format(key))
    for data in MY_HOT_KEYS:
        FUNCTION = list(data.keys())[0]
        KEYS = list(data.values())[0]
        
        if key in KEYS:
            current_keys.add(key)

            # checker = True
            # for k in KEYS:
            #     if k not in current_keys:
            #         checker = False
            #         break
            # if checker:
            #     function = eval(FUNCTION)
            #     function()

            if all(k in current_keys for k in KEYS):
                function = eval(FUNCTION)
                function()

def key_released(key):
    print("Released {}".format(key))

    if key in current_keys:
        current_keys.remove(key)

    if key == Key.esc:
        return False

with Listener(on_press=key_pressed, on_release=key_released) as listener:
    listener.join()
