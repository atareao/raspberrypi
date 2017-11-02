#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Define los colores en modo hexadecimal
COLORS = [0xFF0000, 0x00FF00, 0x0000FF, 0x00FFFF, 0xFF00FF, 0xFFFF00, 0xFFFFFF, 0xB695C0]
# Establece los pines conforme a GPIO
pins = {'Red': 22, 'Green': 17, 'Blue': 27}

def mapea(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def set_color(color):
    # calcula el valor para cada canal R, G, B
    R_val = (color & 0xFF0000) >> 16
    G_val = (color & 0x00FF00) >> 8
    B_val = (color & 0x0000FF) >> 0

    # Convierte el color de 0~255 a 0 ó 1 (entero)
    R_val = int(mapea(R_val, 0, 255, 0, 1))
    G_val = int(mapea(G_val, 0, 255, 0, 1))
    B_val = int(mapea(B_val, 0, 255, 0, 1))

    # asigna a cada pin el valor calculado
    GPIO.output(pins['Red'], R_val)
    GPIO.output(pins['Green'], G_val)
    GPIO.output(pins['Blue'], B_val)

    # imprime los resultados
    print("R_val = %s, G_val = %s, B_val = %s"%(R_val, G_val, B_val))

# quita la tensión en cada uno de los pines
def reset():
    for i in pins:
        GPIO.output(pins[i], 0)

def main():
    try:
        # Establece el modo, en este caso a los valores GPIO
        GPIO.setmode(GPIO.BCM)
            for i in pins:
                # configura los pines como de salida
                GPIO.setup(pins[i], GPIO.OUT, initial=GPIO.HIGH)
            reset()
            while True:
                for color in COLORS:
                    set_color(color)
                    time.sleep(2)
                    reset()
    except Exception as e:
        print(e)
    finally:
        # Release resource
        reset()
        GPIO.cleanup()


if __name__ == '__main__':
	main()
