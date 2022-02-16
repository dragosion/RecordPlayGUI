from pynput import mouse

#wtf is this variable name explained?
#m_lc_ = mouse left click
#mch_  = mouse click history

is_m_lc_down = False
is_m_lc_up = False

#mouse left click pressed vars
m_lc_down_x = 0
m_lc_down_y = 0

#mouse left click released vars
m_lc_up_x = 0
m_lc_up_y = 0

# store recorded events in dict
mch = {}

def on_click(x, y, button, pressed):
    global m_lc_down_x
    global m_lc_down_y

    global m_lc_up_x
    global m_lc_up_y

    global is_m_lc_down
    global is_m_lc_up

    if pressed:
        is_m_lc_down = True
        m_lc_down_x = x
        m_lc_down_y = y
        print('Event triggered down:', m_lc_down_x, m_lc_down_y)
    else:        
        is_m_lc_up = True
        m_lc_up_x = x
        m_lc_up_y = y
        print('Event triggered up:', m_lc_up_x, m_lc_up_y)


print('Press Ctrl-C to quit.')

listener = mouse.Listener(on_click=on_click)
listener.start()


try:
    event_id = 0
    while True:
        if is_m_lc_down:
            event_id += 1 
            print('In Loop: m_lc_down:', m_lc_down_x, m_lc_down_y, " event_id: ", event_id)
            mch[event_id] = 'm_lc_down_xy', m_lc_down_x, m_lc_down_y
            is_m_lc_down = False
                        
        if is_m_lc_up:
            event_id += 1 
            print('In Loop: m_lc_up:', m_lc_up_x, m_lc_up_y, " event_id: ", event_id)
            mch[event_id] = 'm_lc_up_xy', m_lc_up_x, m_lc_up_y
            is_m_lc_up = False

except KeyboardInterrupt:
    # end it gracefully
    listener.stop()            
    listener.join()
    print("RESULT:")
    print(mch)
    input('\nDone. Press enter to exit program...')

    



