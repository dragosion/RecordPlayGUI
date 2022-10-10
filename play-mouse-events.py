import pyautogui, time
time.sleep(5) # prep your env
pyautogui.click()
distance = 200

#sample dataset
#mhd = mouse history data
#test
mhd = {1: (1988, 'Button.left', 'm_lc_down_xy', 1173, 18), 2: (112, 'Button.left', 'm_lc_up_xy', 1173, 18), 5: (4096, 'Button.left', 'm_lc_down_xy', 800, 681), 6: (112, 'Button.left', 'm_lc_up_xy', 800, 681), 7: (287, 'Button.left', 'm_lc_down_xy', 800, 681), 8: (96, 'Button.left', 'm_lc_up_xy', 800, 681), 9: (208, 'Button.left', 'm_lc_down_xy', 800, 681), 10: (112, 'Button.left', 'm_lc_up_xy', 800, 681), 11: (208, 'Button.left', 'm_lc_down_xy', 800, 681), 12: (128, 'Button.left', 'm_lc_up_xy', 800, 681), 13: (336, 'Button.left', 'm_lc_down_xy', 800, 681), 14: (112, 'Button.left', 'm_lc_up_xy', 800, 681), 15: (288, 'Button.left', 'm_lc_down_xy', 800, 681), 16: (128, 'Button.left', 'm_lc_up_xy', 800, 681), 17: (321, 'Button.left', 'm_lc_down_xy', 800, 681), 18: (96, 'Button.left', 'm_lc_up_xy', 800, 681), 19: (448, 'Button.left', 'm_lc_down_xy', 800, 681), 20: (96, 'Button.left', 'm_lc_up_xy', 800, 681), 21: (7168, 'Button.left', 'm_lc_down_xy', 841, 220), 22: (128, 'Button.left', 'm_lc_up_xy', 841, 220), 23: (929, 'Button.left', 'm_lc_down_xy', 881, 294), 24: (112, 'Button.left', 'm_lc_up_xy', 881, 294), 25: (1263, 'Button.left', 'm_lc_down_xy', 1141, 380), 26: (112, 'Button.left', 'm_lc_up_xy', 1141, 380), 27: (2497, 'Button.left', 'm_lc_down_xy', 823, 203), 28: (128, 'Button.left', 'm_lc_up_xy', 823, 203), 29: (1917, 'Button.left', 'm_lc_down_xy', 1196, 1026), 30: (111, 'Button.left', 'm_lc_up_xy', 1196, 1026), 31: (1792, 'Button.left', 'm_lc_down_xy', 1215, 170), 32: (112, 'Button.left', 'm_lc_up_xy', 1215, 170), 33: (864, 'Button.left', 'm_lc_down_xy', 921, 351), 34: (112, 'Button.left', 'm_lc_up_xy', 921, 351), 35: (816, 'Button.left', 'm_lc_down_xy', 985, 411), 36: (112, 'Button.left', 'm_lc_up_xy', 985, 411), 37: (559, 'Button.left', 'm_lc_down_xy', 1134, 415), 38: (112, 'Button.left', 'm_lc_up_xy', 1134, 415), 39: (559, 'Button.left', 'm_lc_down_xy', 1248, 411), 40: (111, 'Button.left', 'm_lc_up_xy', 1248, 411), 41: (4863, 'Button.left', 'm_lc_down_xy', 937, 217), 42: (112, 'Button.left', 'm_lc_up_xy', 937, 217), 43: (880, 'Button.left', 'm_lc_down_xy', 1004, 289), 44: (112, 'Button.left', 'm_lc_up_xy', 1004, 289), 45: (3327, 'Button.left', 'm_lc_down_xy', 1024, 341), 46: (113, 'Button.left', 'm_lc_up_xy', 1024, 341), 47: (1646, 'Button.left', 'm_lc_down_xy', 1262, 448), 48: (112, 'Button.left', 'm_lc_up_xy', 1262, 448), 49: (1071, 'Button.left', 'm_lc_down_xy', 740, 288), 50: (128, 'Button.left', 'm_lc_up_xy', 740, 288), 51: (2495, 'Button.left', 'm_lc_down_xy', 768, 428), 52: (112, 'Button.left', 'm_lc_up_xy', 768, 429), 53: (3550, 'Button.left', 'm_lc_down_xy', 1338, 254), 54: (112, 'Button.left', 'm_lc_up_xy', 1338, 254), 55: (1808, 'Button.left', 'm_lc_down_xy', 935, 231), 56: (112, 'Button.left', 'm_lc_up_xy', 935, 231), 57: (2719, 'Button.left', 'm_lc_down_xy', 1119, 311), 58: (96, 'Button.left', 'm_lc_up_xy', 1119, 311), 59: (1600, 'Button.left', 'm_lc_down_xy', 1301, 486), 60: (112, 'Button.left', 'm_lc_up_xy', 1301, 486), 61: (864, 'Button.left', 'm_lc_down_xy', 961, 398), 62: (112, 'Button.left', 'm_lc_up_xy', 961, 398), 63: (1200, 'Button.left', 'm_lc_down_xy', 891, 504), 64: (80, 'Button.left', 'm_lc_up_xy', 891, 504), 65: (1792, 'Button.left', 'm_lc_down_xy', 1173, 358), 66: (112, 'Button.left', 'm_lc_up_xy', 1173, 358), 67: (1616, 'Button.left', 'm_lc_down_xy', 935, 251), 68: (112, 'Button.left', 'm_lc_up_xy', 935, 251), 69: (10667, 'Button.left', 'm_lc_down_xy', 1058, 323), 70: (112, 'Button.left', 'm_lc_up_xy', 1058, 323), 71: (2656, 'Button.left', 'm_lc_down_xy', 1242, 369), 72: (128, 'Button.left', 'm_lc_up_xy', 1242, 369), 73: (1024, 'Button.left', 'm_lc_down_xy', 895, 278), 74: (112, 'Button.left', 'm_lc_up_xy', 895, 278), 75: (4126, 'Button.left', 'm_lc_down_xy', 877, 412), 76: (112, 'Button.left', 'm_lc_up_xy', 877, 412), 77: (1582, 'Button.left', 'm_lc_down_xy', 1196, 239), 78: (127, 'Button.left', 'm_lc_up_xy', 1196, 239), 79: (2433, 'Button.left', 'm_lc_down_xy', 948, 253), 80: (96, 'Button.left', 'm_lc_up_xy', 948, 253), 81: (1152, 'Button.left', 'm_lc_down_xy', 934, 220), 82: (112, 'Button.left', 'm_lc_up_xy', 934, 220), 83: (2591, 'Button.left', 'm_lc_down_xy', 1019, 287), 84: (112, 'Button.left', 'm_lc_up_xy', 1019, 287), 85: (2544, 'Button.left', 'm_lc_down_xy', 1245, 404), 86: (111, 'Button.left', 'm_lc_up_xy', 1245, 404), 87: (1680, 'Button.left', 'm_lc_down_xy', 912, 385), 88: (176, 'Button.left', 'm_lc_up_xy', 912, 385), 89: (2928, 'Button.left', 'm_lc_down_xy', 886, 524), 90: (112, 'Button.left', 'm_lc_up_xy', 886, 524), 91: (2062, 'Button.left', 'm_lc_down_xy', 1177, 347), 92: (112, 'Button.left', 'm_lc_up_xy', 1177, 348), 93: (1505, 'Button.left', 'm_lc_down_xy', 1892, 213), 94: (143, 'Button.left', 'm_lc_up_xy', 1892, 213), 95: (1133, 'Button.left', 'm_lc_down_xy', 1813, 284), 96: (111, 'Button.left', 'm_lc_up_xy', 1813, 284), 97: (1214, 'Button.left', 'm_lc_down_xy', 1487, 402), 98: (111, 'Button.left', 'm_lc_up_xy', 1487, 402), 99: (816, 'Button.left', 'm_lc_down_xy', 999, 383), 100: (144, 'Button.left', 'm_lc_up_xy', 999, 383), 101: (1809, 'Button.left', 'm_lc_down_xy', 939, 494), 102: (64, 'Button.left', 'm_lc_up_xy', 942, 495), 103: (1344, 'Button.left', 'm_lc_down_xy', 1176, 346), 104: (96, 'Button.left', 'm_lc_up_xy', 1176, 347), 105: (7740, 'Button.left', 'm_lc_down_xy', 1831, 219), 106: (111, 'Button.left', 'm_lc_up_xy', 1831, 219), 107: (1615, 'Button.left', 'm_lc_down_xy', 949, 212), 108: (112, 'Button.left', 'm_lc_up_xy', 949, 212), 109: (1198, 'Button.left', 'm_lc_down_xy', 872, 221), 110: (128, 'Button.left', 'm_lc_up_xy', 872, 220), 111: (512, 'Button.left', 'm_lc_down_xy', 874, 233), 112: (80, 'Button.left', 'm_lc_up_xy', 874, 233), 113: (431, 'Button.left', 'm_lc_down_xy', 872, 251), 114: (95, 'Button.left', 'm_lc_up_xy', 872, 251), 115: (816, 'Button.left', 'm_lc_down_xy', 948, 242), 116: (96, 'Button.left', 'm_lc_up_xy', 948, 242), 117: (768, 'Button.left', 'm_lc_down_xy', 873, 217), 118: (96, 'Button.left', 'm_lc_up_xy', 873, 216), 119: (1008, 'Button.left', 'm_lc_down_xy', 779, 216), 120: (128, 'Button.left', 'm_lc_up_xy', 779, 217), 121: (1328, 'Button.left', 'm_lc_down_xy', 909, 280), 122: (96, 'Button.left', 'm_lc_up_xy', 909, 280)}


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
