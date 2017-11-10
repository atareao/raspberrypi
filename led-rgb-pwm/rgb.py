#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Define los colores en modo hexadecimal
COLORS = [0xFF0000, 0x00FF00, 0x0000FF, 0x00FFFF, 0xFF00FF, 0xFFFF00, 0xFFFFFF,
          0xB695C0]
COLORS = {
    'Blanco': 0xFFFFFF,
    'Azur': 0xF0FFFF,
    'Crema': 0xF5FFFA,
    'Nieve': 0xFFFAFA,
    'Marfil': 0xFFFFF0,
    'Blanco fantasma': 0xF8F8FF,
    'Blanco floral': 0xFFFAF0,
    'Azul alicia': 0xF0F8FF,
    'Cian claro': 0xE0FFFF,
    'Melón verde': 0xF0FFF0,
    'Amarillo claro': 0xFFFFE0,
    'Concha': 0xFFF5EE,
    'Sonrojo lavanda': 0xFFF0F5,
    'Humo blanco': 0xF5F5F5,
    'Encaje antiguo': 0xFDF5E6,
    'Seda de maíz': 0xFFF8DC,
    'Lino': 0xFAF0E6,
    'Amarillo alambre dorado claro': 0xFAFAD2,
    'Gasa limón': 0xFFFACD,
    'Beige': 0xF5F5DC,
    'Lavanda': 0xE6E6FA,
    'Batido de papaya': 0xFFEFD5,
    'Rosa brumosa': 0xFFE4E1,
    'Blanco antiguo': 0xFAEBD7,
    'Blanco almendra': 0xFFEBCD,
    'Sopa': 0xFFE4C4,
    'Turquesa pálido': 0xAFEEEE,
    'Mocasín': 0xFFE4B5,
    'Gainsboro': 0xDCDCDC,
    'Soplido melocotón': 0xFFDAB9,
    'Blanco navajo': 0xFFDEAD,
    'Dorado alambre pálido': 0xEEE8AA,
    'Trigo': 0xF5DEB3,
    'Polvo azul': 0xB0E0E6,
    'Aguamarina': 0x7FFFD4,
    'Gris claro': 0xD3D3D3,
    'Rosa': 0xFFC0CB,
    'Azul claro': 0xADD8E6,
    'Cardo': 0xD8BFD8,
    'Rosa claro': 0xFFB6C1,
    'Azul cielo claro': 0x87CEFA,
    'Verde pálido': 0x98FB98,
    'Azul acero claro': 0xB0C4DE,
    'Caqui': 0xF0D58C,
    'Azul cielo': 0x87CEEB,
    'Agua': 0x00FFFF,
    'Cian': 0x00FFFF,
    'Plata': 0xC0C0C0,
    'Ciruela': 0xDDA0DD,
    'Gris': 0xBEBEBE,
    'Verde claro': 0x90EE90,
    'Violeta': 0xEE82EE,
    'Amarillo': 0xFFFF00,
    'Turquesa': 0x40E0D0,
    'Madera fornida': 0xDEB887,
    'Amarillo verde': 0xADFF2F,
    'Bronceado': 0xD2B48C,
    'Turquesa medio': 0x48D1CC,
    'Salmón claro': 0xFFA07A,
    'Aguamarina medio': 0x66CDAA,
    'Gris oscuro': 0xA9A9A9,
    'Orquídea': 0xDA70D6,
    'Verde mar intenso': 0x8FBC8F,
    'Azul cielo intenso': 0x00BFFF,
    'Marrón arena': 0xF4A460,
    'Dorado': 0xFFD700,
    'Verde primavera medio': 0x00FA9A,
    'Caqui oscuro': 0xBDB76B,
    'Aciano azul': 0x6495ED,
    'Rosa caliente': 0xFF69B4,
    'Salmón oscuro': 0xE9967A,
    'Turquesa oscuro': 0x00CED1,
    'Verde primavera': 0x00FF7F,
    'Coral claro': 0xF08080,
    'Marrón rosado': 0xBC8F8F,
    'Salmón': 0xFA8072,
    'Chartreuse': 0x7FFF00,
    'Púrpura medio': 0x9370DB,
    'Verde césped': 0x7CFC00,
    'Azul dodger': 0x1E90FF,
    'Verde amarillo': 0x9ACD32,
    'Violeta rojo pálido': 0xDB7093,
    'Azul pizarra medio': 0x7B68EE,
    'Orquídea medio': 0xBA55D3,
    'Coral': 0xFF7F50,
    'Azul cadete': 0x5F9EA0,
    'Verde mar claro': 0x20B2AA,
    'Dorado alambre': 0xDAA520,
    'Naranja': 0xFFA500,
    'Gris pizarra claro': 0x778899,
    'Fucsia': 0xFF00FF,
    'Magenta': 0xFF00FF,
    'Verde mar medio': 0x3CB371,
    'Perú': 0xCD853F,
    'Azul acero': 0x4682B4,
    'Azul real': 0x4169E1,
    'Gris pizarra': 0x708090,
    'Tomate': 0xFF6347,
    'Naranja oscuro': 0xFF8C00,
    'Azul pizarra': 0x6A5ACD,
    'Verde lima': 0x32CD32,
    'Lima': 0x00FF00,
    'Rojo indio': 0xCD5C5C,
    'Orquídea oscuro': 0x9932CC,
    'Azul violeta': 0x8A2BE2,
    'Rosa intenso': 0xFF1493,
    'Dorado alambre oscuro': 0xB8860B,
    'Chocolate': 0xD2691E,
    'Cian oscuro': 0x008B8B,
    'Gris difuso': 0x696969,
    'Gris aceituna': 0x6B8E23,
    'Verde mar': 0x2E8B57,
    'Verde cerceta': 0x008080,
    'Violeta oscuro': 0x9400D3,
    'Violeta rojo medio': 0xC71585,
    'Naranja rojo': 0xFF4500,
    'Aceituna': 0x808000,
    'Siena': 0xA0522D,
    'Azul pizarra oscuro': 0x483D8B,
    'Verde aceituna oscuro': 0x556B2F,
    'Verde bosque': 0x228B22,
    'Carmesí': 0xDC143C,
    'Azul': 0x0000FF,
    'Magenta oscuro': 0x8B008B,
    'Gris pizarra oscuro': 0x2F4F4F,
    'Marrón montura': 0x8B4513,
    'Marrón': 0xA52A2A,
    'Ladrillo refractario': 0xB22222,
    'Púrpura': 0x800080,
    'Verde': 0x008000,
    'Rojo': 0xFF0000,
    'Azul medio': 0x0000CD,
    'Índigo': 0x4B0082,
    'Azul medianoche': 0x191970,
    'Verde oscuro': 0x006400,
    'Azul oscuro': 0x00008B,
    'Azul marino': 0x000080,
    'Rojo oscuro': 0x8B0000,
    'Granate': 0x800000,
    'Negro': 0x000000
}
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

        led = Led(pins['Red'], pins['Green'], pins['Blue'])

        while True:
            for nombre, color in COLORS.items():
                print('Color: {0}'.format(nombre))
                led.set_color(color)
                time.sleep(2)
                reset()
                # led.set_color(0x000000)
        led.stop()
        GPIO.output(pins, GPIO.HIGH)
    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
