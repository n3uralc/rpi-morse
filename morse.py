import RPi.GPIO as GPIO
from time import *
from sys import *
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
led_pin = 8
GPIO.setup(led_pin, GPIO.OUT)
# Setup the text we are going to translate to morse code
# and add an SK at the end signaling End of Transmission
text=argv[1].upper() + " SK"

# Define all of our letters and numbers
# as morse code
mA=".-"
mB="-..."
mC="-.-."
mD="-.."
mE="."
mF="..-."
mG="--."
mH="...."
mI=".."
mJ=".---"
mK="-.-"
mL=".-.."
mM="--"
mN="-."
mO="---"
mP=".--."
mQ="--.-"
mR=".-."
mS="..."
mT="-"
mU="..-"
mV="...-"
mW=".--"
mX="-..-"
mY="-.--"
mZ="--.."
m1=".----"
m2="..---"
m3="...--"
m4="....-"
m5="....."
m6="-...."
m7="--..."
m8="---.."
m9="----."
m0="-----"

# Does the light for a dit '.'
def dit():
  GPIO.output(led_pin, True)
  sleep(0.5)
  GPIO.output(led_pin, False)
  sleep(0.5)
  
 # Does the light for a dah '-'
def dah():
  GPIO.output(led_pin, True)
  sleep(1.0)
  GPIO.output(led_pin, False)
  sleep(0.5)
  
# this function translates '.'s and '-'s to dit and dah 
def showCode( mCode ):
	print ( mCode )
	for c in mCode:
		if c == '.':
			dit()
		if c == '-':
			dah()
	sleep(1.0)

# the main loop for our program that parses the text from the command line
for x in text: 
	print (x)
	if x == 'A': showCode( mA )
	if x == 'B': showCode( mB )
	if x == 'C': showCode( mC )
	if x == 'D': showCode( mD )
	if x == 'E': showCode( mE )
	if x == 'F': showCode( mF )
	if x == 'G': showCode( mG )
	if x == 'H': showCode( mH )
	if x == 'I': showCode( mI )
	if x == 'J': showCode( mJ )
	if x == 'K': showCode( mK )
	if x == 'L': showCode( mL )
	if x == 'M': showCode( mK )
	if x == 'N': showCode( mN )
	if x == 'O': showCode( mO )
	if x == 'P': showCode( mP )
	if x == 'Q': showCode( mQ )
	if x == 'R': showCode( mR )
	if x == 'S': showCode( mS )
	if x == 'T': showCode( mT )
	if x == 'U': showCode( mU )
	if x == 'V': showCode( mV )
	if x == 'W': showCode( mW )
	if x == 'X': showCode( mX )
	if x == 'Y': showCode( mY )
	if x == 'Z': showCode( mZ )
	if x == '1': showCode( m1 )
	if x == '2': showCode( m2 )
	if x == '3': showCode( m3 )
	if x == '4': showCode( m4 )
	if x == '5': showCode( m5 )
	if x == '6': showCode( m6 )
	if x == '7': showCode( m7 )
	if x == '8': showCode( m8 )
	if x == '9': showCode( m9 )
	if x == '0': showCode( m0 )
	if x == ' ': sleep(1.5)
				
			
