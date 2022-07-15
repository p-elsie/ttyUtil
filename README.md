# ttyUtil
read/write one line to serial port

Usage:

ttyUtil.py --string=<string> [--port=<port> default:COM1] [--baud=<baud> default:9600]

  Sends the specified string to the serial port, followed by line feed, and prints any immediate, one line response message.
  Use double quotes if the string contains spaces.
  
  
Instructions for compiling with pyinstaller using Python 2.7 on Windows 10:
  
  pip install pyserial
  pip install pyinstaller 
  pyinstaller --onefile ttyUtil.py
 
