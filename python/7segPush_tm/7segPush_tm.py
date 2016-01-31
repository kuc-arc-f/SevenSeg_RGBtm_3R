# -*- coding: utf-8 -*- 
#------------------------------------
# @calling
# @purpose : 
# @date : 2016/01/31
# @Author : Kouji Nakashima / kuc-arc-f.com
#------------------------------------
import datetime
import serial
import time
import sys
import traceback
import com_Uart

mTimeMax=5
mDevice = "/dev/ttyAMA0"

if __name__ == "__main__":
	clsUart = com_Uart.uartClass()
	ser=serial.Serial(mDevice ,9600)
	#time.sleep(3.0)
	from datetime import datetime
	tmBef = datetime.now()
	
	while True:
		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		iSpan = tmSpan.total_seconds()
#		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		sTime = datetime.now().strftime("%H%M")
		sTemp=""		
		if iSpan >= mTimeMax:
			tmBef = datetime.now()
			try:
				print("time=" +sTime)
				sSend="tmp=00"+ sTime
				clsUart.send_7seg(sSend ,ser)
				time.sleep(1.0)
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"
	


