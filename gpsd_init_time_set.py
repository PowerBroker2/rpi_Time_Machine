'''
Mostly copied from: https://wb4son.com/wpblog/?p=1635
'''

import os
import sys

from gps import *


GNSS_PORT = r'/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00'


if __name__ == '__main__':
    os.system('sudo gpsd {port} -F /var/run/gpsd.sock'.format(port=GNSS_PORT))
    
    try:
        gpsd = gps(mode=WATCH_ENABLE)
    except:
        print('ERROR: No GPS Present, time not set!!')
        sys.exit()

    i = 0

    while i < 10:
        gpsd.next()
        
        if gpsd.utc != None and gpsd.utc != '':
            year  = gpsd.utc[0:4]
            month = gpsd.utc[5:7]
            day   = gpsd.utc[8:10]
            time  = gpsd.utc[11:19]
            
            gpsutc     = year + month + day + ' ' + time
            update_str = 'sudo date -u --set="%s"' % gpsutc
            
            print(update_str)
            os.system(update_str)
            
            i = i + 1
