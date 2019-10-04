from tuning import Tuning
from pixel_ring import pixel_ring
import usb.core
import usb.util
import time



dev = usb.core.find(idVendor = 0x2886, idProduct = 0x0018)
#print dev
if dev:
        Mic_tuning = Tuning(dev)
       # print Mic_tuning.is_voice(), Mic_tuning.direction
	i = Mic_tuning.is_voice()
	j = Mic_tuning.direction
        while True:
		Mic_tuning.set_vad_threshold(1.5)
#		pixel_ring.set_brightness(0x00)	#turn off LED to conserve power
                try:
			#if (Mic_tuning.is_voice == True): #Attempting to refine code to only show when Mic_tuning.is_voice is 1 
                        	print Mic_tuning.is_voice(), Mic_tuning.direction	#Displays values 0 for noise or 1 for 
											# human voice and Degrees 
                        	time.sleep(1)
                except KeyboardInterrupt:
                        break
