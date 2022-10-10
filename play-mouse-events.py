import pyautogui, time
time.sleep(5) # prep your env
pyautogui.click()
distance = 200

#sample dataset
#mhd = mouse history data
#TEST DATA, REPLACE mhd VARIABLE with output from the mouse record scipt in this project!
mhd = {1: (1988, 'Button.left', 'm_lc_down_xy', 1173, 18), 2: (112, 'Button.left', 'm_lc_up_xy', 1173, 18), 5: (4096, 'Button.left', 'm_lc_down_xy', 800, 681), 6: (112, 'Button.left', 'm_lc_up_xy', 800, 681)}

button_type = ""
action_string = ""
x = -1
y = -1
sleep_time = 0 # recorded time between events

is_down = 'm_lc_down_xy'
is_up = 'm_lc_up_xy'
btn_left_action_text = "Button.left"
btn_right_action_text = "Button.right"
print('Press Ctrl-C to quit.')
#print("start loop")

try:
    for key, item in mhd.items():
        #print(item)
        sleep_time,button_type,action_string, x, y = item
        #print(button_type,action_string, x, y)

        sleep_time = sleep_time/1000

        if button_type == btn_left_action_text:
            if action_string == is_down:
                print("left_down",x,y)
                pyautogui.mouseDown(x=x,y=y)
            elif action_string == is_up:
                print("LEFT_UP",x,y)
                pyautogui.mouseUp(x=x,y=y)
                
        elif button_type == btn_right_action_text:
            if action_string == is_down:
                print("right_down",x,y)
                pyautogui.mouseDown(button='right',x=x,y=y)
            elif action_string == is_up:
                print("RIGHT_UP",x,y)
                pyautogui.mouseUp(button='right',x=x,y=y)
                
        time.sleep(sleep_time) # give some time to respond
        #print("Sleep {0}".format(sleep_time))

except KeyboardInterrupt:
    print('\nDone.')

#input("Finished. Press enter to exit...")
print("Finished. Press enter to exit...")
