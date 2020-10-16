
mode = input("Press 1 for sleep and 0 for alarm : ")
if mode == '1':
     exec(open('Sleep.py').read())
else  :
     exec(open('Alarm.py').read())
     