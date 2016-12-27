import network
import time


def start_station():
    global sta_if
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)



def scan():
    time_start = time.time()
    networks = sta_if.scan()
    #print out how long it takes to update
    print ( "Run time: {:.3f}".format(time.time()-time_start) )
    return networks

def print_networks(networks):
    for l in networks:
        print("Name: {}, Strength: {}".format(l[0], l[3]))


'''
ap = network.WLAN(network.AP_IF) # create access-point interface
ap.active(True)         # activate the interface
ap.config(essid='ESP-AP') # set the ESSID of the access point
'''


if __name__ == "__main__":
    
    start_station()
    
    print_networks(scan())

