import pyautogui, time
time.sleep(5) # prep your env
pyautogui.click()
distance = 200

#sample dataset
#mhd = mouse history data
mhd = {1: ('m_lc_down_xy', 1077, 1058), 2: ('m_lc_up_xy', 1077, 1058), 3: ('m_lc_down_xy', 1095, 1058), 4: ('m_lc_up_xy', 1095, 1058)}

action_string = ""
x = -1
y = -1

is_down = 'm_lc_down_xy'
is_up = 'm_lc_up_xy'
print('Press Ctrl-C to quit.')
print("start loop")

try:
    for key, item in mhd.items():
        #print(item)
        action_string, x, y = item
        #print(action_string, x, y)

        if action_string == is_down:
            #print("down",x,y)
            pyautogui.mouseDown(x,y)
        elif action_string == is_up:
            #print("UP",x,y)
            pyautogui.mouseUp(x,y)
        time.sleep(120)
except KeyboardInterrupt:
    print('\nDone.')

input("Finished. Press enter to exit...")
