#!/usr/bin/python

import sys
import getopt
import serial

def main(argv):
   port = 'COM1'
   baud = '9600'
   commandStr = ''
   commandsPos = 1
   verbose = False
   try:
      opts, args = getopt.getopt(argv,"h:vd",["help","verbose","debug","port=","baud=","string="])
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h", "--help"):
         usage()
         sys.exit()
      elif opt in ("-d", "-v", "--debug", "--verbose"):
         verbose = True
         commandsPos += 1
      elif opt == "--port":
         port = arg
         commandsPos += 1
      elif opt == "--baud":
         baud = arg
         commandsPos += 1
      elif opt == "--string":
         commandStr = arg
         commandsPos += 1
      else:
         print('arg is', arg)  
   ser = serial.Serial(port, int(baud), timeout=1)
   ser.write(str.encode(commandStr + '\n'))
   response = ser.readline().decode().rstrip()
   if verbose:
      print('port is {}'.format(port))
      print('baud is {}'.format(baud))
      print('string is \"{}\"'.format(commandStr))
      for x in range(commandsPos, len(sys.argv)):
         print('command =', sys.argv[x])    
      print('response is \"{}\"'.format(response))
   else:
      print(response)
   ser.close()
     
   
def usage():
   print('Usage:')
   print
   print(sys.argv[0] + ' --string=<string> [--port=<port> default:COM1] [--baud=<baud> default:9600]')
   print
   print('  Sends the specified string to the serial port, followed by line feed, and prints any immediate, one line response message.')
   print('  Use double quotes if the string contains spaces. ')

if __name__ == "__main__":
   main(sys.argv[1:])