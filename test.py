import network
import time
from machine import Pin, PWM

ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid='ESP-AP') # set the ESSID of the access point
ap_if.active(True)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)


pwm0 = PWM(Pin(0), freq=1000, duty=0) # create and configure in one go

print("sta statue: {}".format(sta_if.active()))
print("ap statue: {}".format(ap_if.active()))


def scan():
    start = time.ticks_ms()
    networks = sta_if.scan()
    print("Scan Time (s): {:0.3f}".format(time.ticks_diff(time.ticks_ms(), start)/1000))
    return networks

def print_networks(networks):
    for l in networks:
        print("Name: {}, Strength: {}".format(l[0], l[3]))

def closeness(networks):
    brightness = 0
    for l in networks:
        if "ESP-AP" in l[0]:
            #algorithm for how bright the led should be
            #for now it is very simple. 
            brightness += 100 + l[3]
    #for testing there are 2 ap's. this means the range of brightness is 0 - 200. 
    #for the pwm function it needs to be mapped from 0 to 1023
    #brightness = brightness * 10 - 400
    print ("Brightness: {}".format(brightness))
    return brightness

'''
ap = network.WLAN(network.AP_IF) # create access-point interface
ap.active(True)         # activate the interface
ap.config(essid='ESP-AP') # set the ESSID of the access point
'''


if __name__ == "__main__":
    print_networks(scan())
    while(1):
        pwm0.duty(closeness(scan()))
    '''
    duty=0
    direction=1
    while(1):
        time.sleep(0.01)
        pwm0.duty(duty)
        duty+=direction
        if(duty < 0 or duty > 1023): direction = -direction
   ''' 
