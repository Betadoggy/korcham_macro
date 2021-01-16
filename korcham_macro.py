import pyautogui as pag
import urllib.request
import time

# SSN
SSN_left, SSN_right = "", ""

# server
url = "https://license.korcham.net"
date = urllib.request.urlopen(url).headers['Date']

# button pos
safe_pos = {'x' : 1700, 'y' : 800}

gcu_radio_pos = {'x' : 715, 'y' : 543} 
next_button_pos = {'x' : 1070, 'y' : 660}

agree_check_pos = {'x' : 1020, 'y' : 370}
agree_button_pos = {'x' : 1060, 'y' : 770}

grade_radio_pos = {'x' : 1015, 'y' : 232}
program_radio_pos = {'x' : 1247, 'y' : 241}

SSN_left_pos = {'x' : 910, 'y' : 557}
SSN_right_pos = {'x' : 982, 'y' : 557}
SSN_check_pos = {'x' : 1136, 'y' : 557}
verif_button_pos = {'x' : 1135, 'y' : 165}

locafind_button_pos = {'x' : 1085, 'y' : 615}
incheon_radio_pos = {'x' : 700, 'y' : 330}
locanext_button_pos = {'x' : 1160, 'y' : 780}

def myClick(pos):
    pag.moveTo(pos['x'], pos['y'])
    pag.click()

def myEnd():    # 페이지 맨 아래로
    myClick(safe_pos)
    pag.press('end') 

# print server time
def printStime():
    print("Korcham GCU Macro v.1.0")
    print("server time: " + date)

# SSN input
def SSN_input():
    SSN = input("INSERT SSN : ")
    global SSN_left, SSN_right
    SSN_left = SSN.split('-')[0]
    SSN_right = SSN.split('-')[1]
    print(SSN_left + '-' + SSN_right)

# STEP 01
def select_phase():
    myClick(safe_pos)
    myClick(gcu_radio_pos)
    myClick(next_button_pos)

# STEP 02
def agree_phase():
    myEnd()
    myClick(agree_check_pos)
    myClick(agree_button_pos)

# STEP 03
def subject_phase():
    myEnd()
    myClick(grade_radio_pos)
    myClick(program_radio_pos)
    myClick(agree_button_pos)

# STEP 04
def personal_phase():
    myEnd()
    myClick(SSN_left_pos)
    for _ in range(6): 
        pag.press('backspace')
    pag.typewrite(SSN_left)
    myClick(SSN_right_pos)
    for _ in range(7): 
        pag.press('backspace')
    pag.typewrite(SSN_right)
    myClick(SSN_check_pos)

    time.sleep(0.5)   # 0.5초 대기
    myClick(verif_button_pos)
    myClick(agree_button_pos)

# STEP 05
def location_phase():
    myClick(locafind_button_pos)
    time.sleep(2.5)   # 2.5초 대기
    myEnd()
    myClick(incheon_radio_pos)
    myClick(locanext_button_pos)

# STEP 06
def time_phase():
    time.sleep(2.5)
    for _ in range(5):
        pag.press('down')

def main():
    printStime()
    SSN_input()
    select_phase()
    agree_phase()
    subject_phase()
    personal_phase()
    location_phase()
    time_phase()

if __name__ == "__main__":
    main()