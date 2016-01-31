# -*- coding: utf-8 -*- 
import serial
#import com_appConst
import time


#com_Uart
class uartClass:
    #define
    mCount=0
    def __init__(self):
        print ""
    
    def send_7seg(self, sSend, ser):
    	ser.write(sSend)
    	ser.write("\r\n" )

    def send_subw(self, sPay ,ser):
    	self.mCount=0
    	self.send_matrix("011", ser)
    	for idx in range(len(sPay)):
    		char_code = ord(sPay[idx])
    		#sCode= str(char_code)
    		sHcode= str( hex(char_code) )
    		sBuf = sHcode.replace('0x', '')
    		print sBuf
    		self.send_matrix(sBuf, ser)
    	self.send_matrix("\r\n", ser)
