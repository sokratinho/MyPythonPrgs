
2016 Released
Copy right to Manson Engineering Industical Limited.  

This library supports for NTP and HCS series.

This library supports python2 and python3.



Example in Windows:

1.build python develop enviroment:
	1.1 install python2 or python3 into windows.https://www.python.org/downloads/ choose one for windows.

	1.2 In Windows,bring up a command prompt and type "python -m pip install pyserial=='version'".
	('version' might be '2.7' or '3.1.1' ,it depends on python2 or python3).Then pyserial is installed.
		
2. using mansonlib to program HCS:
	2.1 Navigate to the mansonlib file path,type "python" in the command line.
	
	Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit Intel)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>>import mansonlib
	>>>hcs=mansonlib.HCS()
	>>> hcs.OpenPort('com6')
	True
	>>> hcs.GetModel()
	'HCS-3402\r'
	>>> hcs.GetOutputVoltage()
	12.53
	>>>hcs.SetOutputVoltage(5.5))
	'OK\r'
	>>>hcs.GetOutputMode()
	'CV'
	
2. using mansonlib to program NTP:
   	Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:30:22) [MSC v.1500 32 bit Intel)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>>import mansonlib
	>>>ntp=mansonlib.NTP()
	>>>ntp.OpenPort('com6')
	True
	>>>ntp.GetOutputVoltage()
	12.53
	

Example in Linux:

	1.Ubuntu System 

	install python3:

		sudo apt-get install python3

	install serial :

		sudo apt-get install python3-serial



	2.Fedora System

	install python3:

		yum install python3

	install serial:

		curl -O https://bootstrap.pypa.io/get-pip.py

		sudo python3 get-pip.py

		
NTP Control Method:

1.	OpenPort(serial_port)     ==>"initialize the serial port before starting communicate with NTP"
	parameter[in]: serial port 
	return value:True (Open port success)
				 False (Open port failed)
	Example:
 	OpenPort('/dev/ttyUSB0')  ==> "open linux port" 
	OpenPort('com6')		  ==> "open windows port"
	
2.	OutputOff()           	  ==>"set output off"
	parameter[in]:None
	return: OK (setting output off success)
			False (setting output off failed)
			
3.	OutputOn()			      ==>"set output on"
	parameter[in]:None
	return: OK (setting output off success)
			False (setting output off failed)
	
4.	GetOutputVoltage()		  ==>"get output voltage"
	parameter[in]:None
	return:Output voltage (get output voltage success)
		   False (get output voltage failed)
		   
5.	GetOutputCurrent()		  ==>"get output current"
	parameter[in]:None
	return:Output current (get output current success)
		   False (get output current failed)
		   
6.	GetOutputMode()			  ==>"get output mode"
	parameter[in]:None
	return:Output mode (get output mode success)
		   False (get output mode failed)
		   		   
7.	SetOutputVoltage(votalge) ==>"set the NTP output output voltage"    
	parameter[in]:votalge
	return: OK (Setting NTP output voltage success)
			False (Setting NTP output voltage failed)
	Example:
	SetOutputVoltage(5.5) 	  ==>uint:V
	
8.	SetOutputCurrent(current) ==>"set the NTP output output voltage"   
	parameter[in]:current
	return: OK (Setting NTP output current success)
			False (Setting NTP output current failed)
	Example:
	ntp.SetOutputCurrent(0.5) ==>uint:A		

10.	ClosePort()				==>"close serial port"	

	
HCS Control Method:

1.	OpenPort(serial_port)     ==>"initialize the serial port before starting communicate with HCS"
	parameter[in]: serial port 
	return value:True (Open port success)
				 False (Open port failed)
	Example:
 	OpenPort('/dev/ttyUSB0')  ==> "open linux port" 
	OpenPort('com6')		  ==> "open windows port"
	
2.	OutputOff()           	  ==>"set output off"
	parameter[in]:None
	return: OK (setting output off success)
			False (setting output off failed)
			
3.	OutputOn()			      ==>"set output on"
	parameter[in]:None
	return: OK (setting output off success)
			False (setting output off failed)
			
4.	GetModel()			      ==>"get the HCS model"
	parameter[in]:None
	return: HCS model (get model success)
			False (get model success)
	
5.	GetOutputVoltage()		  ==>"get output voltage"
	parameter[in]:None
	return:Output voltage (get output voltage success)
		   False (get output voltage failed)
		   
6.	GetOutputCurrent()		  ==>"get output current"
	parameter[in]:None
	return:Output current (get output current success)
		   False (get output current failed)
		   
7	GetOutputMode()			  ==>"get output mode"
	parameter[in]:None
	return:Output mode (get output mode success)
		   False (get output mode failed)
		   		   
8.	SetOutputVoltage(votalge) ==>"set the HCS output output voltage"    
	parameter[in]:votalge
	return: OK (Setting HCS output voltage success)
			False (Setting HCS output voltage failed)
	Example:
	SetOutputVoltage(5.5) 	  ==>uint:V
	
9.	SetOutputCurrent(current) ==>"set the HCS output output voltage"   
	parameter[in]:current
	return: OK (Setting HCS output current success)
			False (Setting HCS output current failed)
	Example:
	hcs.SetOutputCurrent(0.5) ==>uint:A			   
		   	   
10.	GetOutputReading('A')     ==>"get the HCS output reading"
	GetOutputReading('V')
	GetOutputReading('C')
	GetOutputReading('S')
	parameter = 'A', return voltage,current,cc|cv
	parameter = 'V', return voltage
	parameter = 'C', return current
	parameter = 'S', return cc|cv
		
11.	GetMaxSet('A')			  ==>"get maximun voltage and current"
	GetMaxSet('V')
	GetMaxSet('C')
	parameter = 'A', return MAX voltage,MAX current
	parameter = 'V', return MAX voltage
	parameter = 'C', return MAX current
	
12.	GetOutputSetting('A')	 ==>"get maximun voltage and current"
	GetOutputSetting('V')
	GetOutputSetting('C')
	if parameter = 'A', return setting voltage,setting current
	if parameter = 'V', return setting voltage
	if parameter = 'C', return setting current
	
13.	SetPrest(index,volt,current) ==> index = (0~2) 
	Example:
	SetPreset(0,0.9,0.1)     ==>"setting the first preset voltage and current"
	SetPreset(1,1.2,1.9)     ==>"setting the second preset voltage and current"
	SetPreset(2,12.8,15)	 ==>"setting the third preset voltage and current"
	 
14.	GetPreset(index,option)
	parameter[in]:index(0~2),option('A'or'V'or'C')
	parameter = (0,'A') ,return the first preset voltage,setting current
	parameter = (0,'V') ,return the first preset voltage
	parameter = (0,'C') ,return the first preset current
	Example:
	GetPreset(0,'A')
	GetPreset(0,'V')
	GetPreset(0,'C')
	GetPreset(1,'A')
	GetPreset(1,'V')
	GetPreset(1,'C')
	GetPreset(2,'A')
	GetPreset(2,'V')
	GetPreset(2,'C')
	
15.	RunPreset(0)			==>"run the first preset voltage and current"	
	RunPreset(1)			==>"run the second preset voltage and current"
	RunPreset(2)			==>"run the third preset voltage and current"
	
16.	ClosePort()				==>"close serial port"


Test File in linux：

NTP:

test1.py
#################################################################################
#!/usr/bin/python

import mansonlib

def test1():
	ntp = mansonlib.NTP() 
	ntp.OpenPort('/dev/ttyUSB0')
#	ntp.OpenPort('com6')
	print(ntp.OutputOn())
	ntp.ClosePort()
	
	
if __name__ == '__main__':	
	test1()

#################################################################################

HCS:

test2.py
#################################################################################
#!/usr/bin/python

import mansonlib

def test2():
	hcs = mansonlib.HCS() 
	hcs.OpenPort('/dev/ttyUSB0')
#	hcs.OpenPort('com6')
	print(hcs.GetModel())
	hcs.ClosePort()
	
	
if __name__ == '__main__':	
	test2()

#################################################################################










