# ttyUtil
writes one line to serial port, then reads, and prints a one line response

Usage:

ttyUtil.py --string=<string> [--port=<port> default:COM1] [--baud=<baud> default:9600]

  Sends the specified string to the serial port, followed by line feed, and prints any immediate, one line response message.
  Use double quotes if the string contains spaces.
  
<br><br>  
Instructions for compiling with pyinstaller using Python 2.7.18 on Windows 10:
  
  pip install pyserial==3.5<br>
  pip install pyinstaller==3.6<br> 
  pyinstaller --onefile ttyUtil.py<br>
<br><br> 
Instructions for compiling with pyinstaller using Python 3.10.5 on Windows 10:
  
  pip install pyserial==3.5<br>
  pip install pyinstaller==5.2<br> 
  pyinstaller --onefile ttyUtil.py<br>
 
