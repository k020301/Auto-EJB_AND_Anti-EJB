import utime, machine, gc
from machine import Pin, Timer
from time import sleep_ms, sleep

## ANTI-EJB AND AUTO-EJB BY TOTALMK http://www.youtube.com/totalmk & http://www.github.com/totalmk ##

##----------EJB KODES----------##
##[BL :P1|P2|P1|P2|P1|P2|P1|P2]##
##[MK1:05|10|02|01|02|03|04|  ]##
##[MK2:05|10|02|08|02|        ]##
##[MK3:05|10|03|01|02|02|03|04]##

######################## MODE SWITCH ###############################

switch01 = Pin(10, Pin.IN, Pin.PULL_UP) #Switch Pos: Auto EJB
switch02 = Pin(11, Pin.IN, Pin.PULL_UP) #Switch Pos: Anti EJB

####################################################################

######################## USER CONFIGURATION ########################

#AUTO EJB
# Button Press Delay (in mili seconds) default = 45
# Example MK1 each press is 45ms * 2 = 90ms by default

mk1delay = 45 # MK1 Time Delay Between Button Push Signals
mk2delay = 45 # MK2 Time Delay Between Button Push Signals
mk3delay = 45 # MK3 Time Delay Between Button Push Signals

# GPIO Buttons (Set Your Buttons Here)

mk1_button = Pin(14, Pin.IN, Pin.PULL_UP) #MK1 BUTTON
mk2_button = Pin(15, Pin.IN, Pin.PULL_UP) #MK2 BUTTON
mk3_button = Pin(26, Pin.IN, Pin.PULL_UP) #MK3 BUTTON

# GPIO Outputs (Set Your BL Outputs Here)

ejbp1bl = Pin(27, Pin.OUT, Pin.PULL_UP) #P1 BLOCK BUTTON
ejbp2bl = Pin(12, Pin.OUT, Pin.PULL_UP) #P2 BLOCK BUTTON
ejbp1bl.value(1)
ejbp2bl.value(1)

#ANTI EJB:
p2_bl_button = Pin(28, Pin.IN, Pin.PULL_UP) #P2 BL

#GPIO Devices Config#
ejbkodestop = Pin(12, Pin.OUT, Pin.PULL_UP) #SEND SABOTAGE SIGNAL
ejbkodestop.value(1)

#EJB Kode Intensity /10
ledbar0 = Pin(9, Pin.OUT)
ledbar1 = Pin(8, Pin.OUT)
ledbar2 = Pin(7, Pin.OUT)
ledbar3 = Pin(6, Pin.OUT)
ledbar4 = Pin(5, Pin.OUT)
ledbar5 = Pin(4, Pin.OUT)
ledbar6 = Pin(3, Pin.OUT)
ledbar7 = Pin(2, Pin.OUT)
ledbar8 = Pin(1, Pin.OUT)
ledbar9 = Pin(0, Pin.OUT)

ledbar0.value(0)
ledbar1.value(0)
ledbar2.value(0)
ledbar3.value(0)
ledbar4.value(0)
ledbar5.value(0)
ledbar6.value(0)
ledbar7.value(0)
ledbar8.value(0)
ledbar9.value(0)

#Stop EJB LED
stopejb = Pin(29, Pin.OUT)
stopejb.value(0)

######################## END CONFIGURATION #########################

####################################################################
##DO NOT CHANGE ANYTHING BELOW UNLESS YOU KNOW WHAT YOU ARE DOING!!#

# P1 / P2 BL Counter DO NOT CHANGE!

DEFAULT_COUNTER_VALUE = 0
COUNTER_CHANGE = 1
p1bl_value = DEFAULT_COUNTER_VALUE
p2bl_value = DEFAULT_COUNTER_VALUE
counter_p2bl = DEFAULT_COUNTER_VALUE
print('PLAYER 2 BL COUNTER IS CURRENTY: {}.'.format(counter_p2bl))

####################################################################

def reset(source):
    global baroff
    global counter_p2bl
    print('')
    counter_p2bl = DEFAULT_COUNTER_VALUE
    print('RESETING PLAYER 2 BL COUNTER=' + str(counter_p2bl))
    baroff()
    reset_timer.deinit()

def baroff():
    ledbar0.value(0)
    ledbar1.value(0)
    ledbar2.value(0)
    ledbar3.value(0)
    ledbar4.value(0)
    ledbar5.value(0)
    ledbar6.value(0)
    ledbar7.value(0)
    ledbar8.value(0)
    ledbar9.value(0)

while True:
    
    #Auto EJB:
    if switch01.value()==0:
        
        if mk1_button.value()==0: # MK1 EJB KODE:
            print('')
            print('-----------MK1 EJB KODE-----------')
            for i in range(5):
                ejbp1bl.value(0)
                sleep_ms(mk1delay)
                ejbp1bl.value(1)
                sleep_ms(mk1delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK1 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            for i in range(10):
                ejbp2bl.value(0)
                sleep_ms(mk1delay)
                ejbp2bl.value(1)
                sleep_ms(mk1delay)
                p2bl_value = p2bl_value + COUNTER_CHANGE
            print('> P2 MK1 BL Button Pushed {} Times.'.format(p2bl_value))
            p2bl_value = DEFAULT_COUNTER_VALUE
            for i in range(2):
                ejbp1bl.value(0)
                sleep_ms(mk1delay)
                ejbp1bl.value(1)
                sleep_ms(mk1delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK1 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            for i in range(1):
                ejbp2bl.value(0)
                sleep_ms(mk1delay)
                ejbp2bl.value(1)
                sleep_ms(mk1delay)
                p2bl_value = p2bl_value + COUNTER_CHANGE
            print('> P2 MK1 BL Button Pushed {} Times.'.format(p2bl_value))
            p2bl_value = DEFAULT_COUNTER_VALUE
            for i in range(2):
                ejbp1bl.value(0)
                sleep_ms(mk1delay)
                ejbp1bl.value(1)
                sleep_ms(mk1delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK1 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            for i in range(3):
                ejbp2bl.value(0)
                sleep_ms(mk1delay)
                ejbp2bl.value(1)
                sleep_ms(mk1delay)
                p2bl_value = p2bl_value + COUNTER_CHANGE
            print('> P2 MK1 BL Button Pushed {} Times.'.format(p2bl_value))
            p2bl_value = DEFAULT_COUNTER_VALUE
            for i in range(4):
                ejbp1bl.value(0)
                sleep_ms(mk1delay)
                ejbp1bl.value(1)
                sleep_ms(mk1delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK1 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            print('-----------AUTOMATIC EJB----------')
            print('----------KODE BY TOTALMK---------')
            print('--------YOUTUBE.COM/TOTALMK-------')
                
        if mk2_button.value()==0: # MK2 EJB KODE:
            print('')
            print('-----------MK2 EJB KODE-----------')
            for i in range(5):
                ejbp1bl.value(0)
                sleep_ms(mk2delay)
                ejbp1bl.value(1)
                sleep_ms(mk2delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK2 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            for i in range(10):
                ejbp2bl.value(0)            
                sleep_ms(mk2delay)
                ejbp2bl.value(1)
                sleep_ms(mk2delay)
                p2bl_value = p2bl_value + COUNTER_CHANGE
            print('> P2 MK2 BL Button Pushed {} Times.'.format(p2bl_value))
            p2bl_value = DEFAULT_COUNTER_VALUE
            for i in range(2):
                ejbp1bl.value(0)            
                sleep_ms(mk2delay)
                ejbp1bl.value(1)
                sleep_ms(mk2delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK2 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            for i in range(8):
                ejbp2bl.value(0)            
                sleep_ms(mk2delay)
                ejbp2bl.value(1)
                sleep_ms(mk2delay)
                p2bl_value = p2bl_value + COUNTER_CHANGE
            print('> P2 MK2 BL Button Pushed {} Times.'.format(p2bl_value))
            p2bl_value = DEFAULT_COUNTER_VALUE
            for i in range(2):
                ejbp1bl.value(0)           
                sleep_ms(mk2delay)
                ejbp1bl.value(1)
                sleep_ms(mk2delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK2 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            print('-----------AUTOMATIC EJB----------')
            print('----------KODE BY TOTALMK---------')
            print('--------YOUTUBE.COM/TOTALMK-------')

        if mk3_button.value()==0: # MK3/UMK3 EJB KODE:
            print('')
            print('-----------MK3 EJB KODE-----------')
            for i in range(5):
                ejbp1bl.value(0)
                sleep_ms(mk3delay)
                ejbp1bl.value(1)
                sleep_ms(mk3delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK3 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            for i in range(10):
                ejbp2bl.value(0)
                sleep_ms(mk3delay)
                ejbp2bl.value(1)
                sleep_ms(mk3delay)
                p2bl_value = p2bl_value + COUNTER_CHANGE
            print('> P2 MK3 BL Button Pushed {} Times.'.format(p2bl_value))
            p2bl_value = DEFAULT_COUNTER_VALUE
            for i in range(3):
                ejbp1bl.value(0)
                sleep_ms(mk3delay)
                ejbp1bl.value(1)
                sleep_ms(mk3delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK3 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            for i in range(1):
                ejbp2bl.value(0)
                sleep_ms(mk3delay)
                ejbp2bl.value(1)
                sleep_ms(mk3delay)
                p2bl_value = p2bl_value + COUNTER_CHANGE
            print('> P2 MK3 BL Button Pushed {} Times.'.format(p2bl_value))
            p2bl_value = DEFAULT_COUNTER_VALUE
            for i in range(2):
                ejbp1bl.value(0)
                sleep_ms(mk3delay)
                ejbp1bl.value(1)
                sleep_ms(mk3delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK3 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            for i in range(2):
                ejbp2bl.value(0)
                sleep_ms(mk3delay)
                ejbp2bl.value(1)
                sleep_ms(mk3delay)
                p2bl_value = p2bl_value + COUNTER_CHANGE
            print('> P2 MK3 BL Button Pushed {} Times.'.format(p2bl_value))
            p2bl_value = DEFAULT_COUNTER_VALUE
            for i in range(3):
                ejbp1bl.value(0)
                sleep_ms(mk3delay)
                ejbp1bl.value(1)
                sleep_ms(mk3delay)
                p1bl_value = p1bl_value + COUNTER_CHANGE
            print('> P1 MK3 BL Button Pushed {} Times.'.format(p1bl_value))
            p1bl_value = DEFAULT_COUNTER_VALUE
            for i in range(4):
                ejbp2bl.value(0)
                sleep_ms(mk3delay)
                ejbp2bl.value(1)
                sleep_ms(mk3delay)
                p2bl_value = p2bl_value + COUNTER_CHANGE
            print('> P2 MK3 BL Button Pushed {} Times.'.format(p2bl_value))
            p2bl_value = DEFAULT_COUNTER_VALUE
            print('-----------AUTOMATIC EJB----------')
            print('----------KODE BY TOTALMK---------')
            print('--------YOUTUBE.COM/TOTALMK-------')
    
    #Anti EJB:
    if switch02.value()==0:        

        #Empty Cache
        gc.collect()
        
        if  p2_bl_button.value()==0 and counter_p2bl <=10:
            print('P2 BL PUSHED')
            counter_p2bl = counter_p2bl + COUNTER_CHANGE
            print('> PLAYER 2 BL COUNTER IS CURRENTY: {}.'.format(counter_p2bl))
            print('')
            sleep(0.1)
            
        #Reset LEDs when Kode hits 10
        if  counter_p2bl >=10:
            baroff()
            
        #Start an encapsulation timer when Kode hits '2' 3 seconds pass and counter is reset
        if counter_p2bl == 1:
            reset_timer = Timer(period=3000, mode=Timer.PERIODIC, callback=reset)
        
        #Display Kode Intensity LEDs
        if counter_p2bl == 1: #1/10 LEDS ON
            ledbar0.value(1)
        if counter_p2bl == 2: #2/10 LEDS ON
            ledbar0.value(1)
            ledbar1.value(1)
        if counter_p2bl == 3: #3/10 LEDS ON
            ledbar0.value(1)
            ledbar1.value(1)
            ledbar2.value(1)
        if counter_p2bl == 4: #4/10 LEDS ON
            ledbar0.value(1)
            ledbar1.value(1)
            ledbar2.value(1)
            ledbar3.value(1)
        if counter_p2bl == 5: #5/10 LEDS ON
            ledbar0.value(1)
            ledbar1.value(1)
            ledbar2.value(1)
            ledbar3.value(1)
            ledbar4.value(1)
        if counter_p2bl == 6: #6/10 LEDS ON
            ledbar0.value(1)
            ledbar1.value(1)
            ledbar2.value(1)
            ledbar3.value(1)
            ledbar4.value(1)
            ledbar5.value(1)
        if counter_p2bl == 7: #7/10 LEDS ON
            ledbar0.value(1)
            ledbar1.value(1)
            ledbar2.value(1)
            ledbar3.value(1)
            ledbar4.value(1)
            ledbar5.value(1)
            ledbar6.value(1)
        if counter_p2bl == 8: #8/10 LEDS ON
            ledbar0.value(1)
            ledbar1.value(1)
            ledbar2.value(1)
            ledbar3.value(1)
            ledbar4.value(1)
            ledbar5.value(1)
            ledbar6.value(1)
            ledbar7.value(1)
        if counter_p2bl == 9: #9/10 LEDS ON
            ledbar0.value(1)
            ledbar1.value(1)
            ledbar2.value(1)
            ledbar3.value(1)
            ledbar4.value(1)
            ledbar5.value(1)
            ledbar6.value(1)
            ledbar7.value(1)
            ledbar8.value(1)

    # EJB Kode Kancel when P2 BL Kode hits '10'

        if counter_p2bl == 10: #10/10 LEDS ON
            ledbar0.value(1)
            ledbar1.value(1)
            ledbar2.value(1)
            ledbar3.value(1)
            ledbar4.value(1)
            ledbar5.value(1)
            ledbar6.value(1)
            ledbar7.value(1)
            ledbar8.value(1)
            ledbar9.value(1)  
            print('P2 BL X 10 EJB KODE FRAGMENT DETECTED')
            print('SABOTAGING EJB KODE!')
            ejbkodestop.value(0)
            sleep_ms(50)
            ejbkodestop.value(1)
            sleep_ms(50)
            ejbkodestop.value(0)
            sleep_ms(50)
            ejbkodestop.value(1)
            print('DONE!')
            print('NO FREE PLAY FOR YOU!!')
            print('HIGH SCORES PROTECTED!!')
            print('')
            print('-------------ANTI EJB-------------')
            print('----------KODE BY TOTALMK---------')
            print('--------YOUTUBE.COM/TOTALMK-------')
            counter_p2bl = DEFAULT_COUNTER_VALUE
            stopejb.value(1)
            sleep(0.5)
            stopejb.value(0)
            baroff()
            
##############################################################################
################## ## AUTOMATIC EJB KODE & ANTI EJB KODE ## ##################
########################## ##    ©TotalMK 2024   ## ##########################
##############################################################################