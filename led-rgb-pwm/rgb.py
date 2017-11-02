#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Set up a color table in Hexadecimal
COLORS = [0xFF0000, 0x00FF00, 0x0000FF, 0x00FFFF, 0xFF00FF, 0xFFFF00, 0xFFFFFF, 0xB695C0]
# Set pins' channels with dictionary
pins = {'Red': 22, 'Green': 17, 'Blue': 27}

# Define a MAP function for mapping values.
# Like from 0~255 to 0~100
def MAP(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Define a function to set up colors 
# input color should be Hexadecimal with 
# red value, blue value, green value.
def setColor(color, p_R, p_G, p_B):
	# Devide colors from 'color' veriable
	R_val = (color & 0xFF0000) >> 16
	G_val = (color & 0x00FF00) >> 8
	B_val = (color & 0x0000FF) >> 0

	# Map color value from 0~255 to 0~100
	R_val = MAP(R_val, 0, 255, 0, 100)
	G_val = MAP(G_val, 0, 255, 0, 100)
	B_val = MAP(B_val, 0, 255, 0, 100)

	# Change the colors
	p_R.ChangeDutyCycle(R_val)
	p_G.ChangeDutyCycle(G_val)
	p_B.ChangeDutyCycle(B_val)

	print("R_val = %s, G_val = %s, B_val = %s"%(R_val, G_val, B_val))

def setColor2(color):
     # Devide colors from 'color' veriable
     R_val = (color & 0xFF0000) >> 16
     G_val = (color & 0x00FF00) >> 8
     B_val = (color & 0x0000FF) >> 0

     # Map color value from 0~255 to 0~1
     R_val = int(MAP(R_val, 0, 255, 0, 1))
     G_val = int(MAP(G_val, 0, 255, 0, 1))
     B_val = int(MAP(B_val, 0, 255, 0, 1))

     GPIO.output(pins['Red'], R_val)
     GPIO.output(pins['Green'], G_val)
     GPIO.output(pins['Blue'], B_val)

     print("R_val = %s, G_val = %s, B_val = %s"%(R_val, G_val, B_val))


def main2():
	try:
		GPIO.setmode(GPIO.BCM)
		for i in pins:
			GPIO.setup(pins[i], GPIO.OUT, initial=GPIO.HIGH)

		# Set all led as pwm channel,
		#  and frequece to 2KHz
		p_R = GPIO.PWM(pins['Red'], 2000)
		p_G = GPIO.PWM(pins['Green'], 2000)
		p_B = GPIO.PWM(pins['Blue'], 2000)

		# Set all begin with value 0
		p_R.start(0)
		p_G.start(0)
		p_B.start(0)

		while True:
			for color in COLORS:
				setColor(color, p_R, p_G, p_B)
				time.sleep(2)

		# Stop all pwm channel
		p_R.stop()
		p_G.stop()
		p_B.stop()
		# Turn off all LEDs
		GPIO.output(pins, GPIO.HIGH)
		# Release resource

	except Exception as e:
		print(e)
	finally:
		# Release resource
		GPIO.cleanup()

def reset():
        for i in pins:
                GPIO.output(pins[i], 0)
def main():
        try:
                GPIO.setmode(GPIO.BCM)
                for i in pins:
                        GPIO.setup(pins[i], GPIO.OUT, initial=GPIO.HIGH)
		# Reseteado de valores
                while True:
                        for color in COLORS:
                                setColor2(color)
                                time.sleep(2)
                                reset()
        except Exception as e:
                print(e)
        finally:
                # Release resource
                GPIO.cleanup()


if __name__ == '__main__':
	main2()
