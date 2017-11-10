#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Define los colores en modo hexadecimal
COLORS = [0xFF0000, 0x00FF00, 0x0000FF, 0x00FFFF, 0xFF00FF, 0xFFFF00, 0xFFFFFF,
          0xB695C0]
# Establece los pines conforme a GPIO
pins = {'Red': 22, 'Green': 17, 'Blue': 27}


def mapea(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def set_color(color, p_R, p_G, p_B):
    # calcula el valor para cada canal R, G, B
    R_val = (color & 0xFF0000) >> 16
    G_val = (color & 0x00FF00) >> 8
    B_val = (color & 0x0000FF) >> 0

    # Convierte el color de 0~255 a un valor de 0 a 100 (entero)
    R_val = mapea(R_val, 0, 255, 0, 100)
    G_val = mapea(G_val, 0, 255, 0, 100)
    B_val = mapea(B_val, 0, 255, 0, 100)

    # Change the colors
    p_R.ChangeDutyCycle(R_val)
    p_G.ChangeDutyCycle(G_val)
    p_B.ChangeDutyCycle(B_val)

    print("R_val = %s, G_val = %s, B_val = %s" % (R_val, G_val, B_val))


# quita la tensión en cada uno de los pines
def reset():
    for i in pins:
        GPIO.output(pins[i], 0)


class Led(object):

    def __init__(self, pin_red, pin_green, pin_blue):
        # Establecemos los LED como canales PWM a una frecuencia de 2 kHz
        self.led = {}
        self.led['red'] = GPIO.PWM(pin_red, 2000)
        self.led['green'] = GPIO.PWM(pin_green, 2000)
        self.led['blue'] = GPIO.PWM(pin_blue, 2000)

        # Iniciamos todos los led con el valor 0
        for color in self.led:
            self.led[color].start(0)

    def stop(self):
        for color in self.led:
            self.led[color].stop()

    def set_color(self, color):
        # calcula el valor para cada canal R, G, B
        R_val = (color & 0xFF0000) >> 16
        G_val = (color & 0x00FF00) >> 8
        B_val = (color & 0x0000FF) >> 0

        # Convierte el color de 0~255 a un valor de 0 a 100 (entero)
        R_val = mapea(R_val, 0, 255, 0, 100)
        G_val = mapea(G_val, 0, 255, 0, 100)
        B_val = mapea(B_val, 0, 255, 0, 100)

        # Change the colors
        self.led['red'].ChangeDutyCycle(R_val)
        self.led['green'].ChangeDutyCycle(G_val)
        self.led['blue'].ChangeDutyCycle(B_val)

        print("R_val = %s, G_val = %s, B_val = %s" % (R_val, G_val, B_val))


def main():
    try:
        GPIO.setmode(GPIO.BCM)
        for i in pins:
            GPIO.setup(pins[i], GPIO.OUT, initial=GPIO.HIGH)

        led = Led()

        while True:
            for color in COLORS:
                led.set_color(color)
                time.sleep(2)
        led.stop()
        GPIO.output(pins, GPIO.HIGH)
    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
