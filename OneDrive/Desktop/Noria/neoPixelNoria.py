from machine import Pin
from utime import sleep
from neopixel import NeoPixel

class NeoPixelNoria:
    def __init__(self, pin=12, num_leds=16):
        self.num_leds = num_leds
        self.pixels = NeoPixel(Pin(pin), num_leds)
        self.rainbow = [
            (255, 0, 0), (255, 127, 0), (255, 255, 0),
            (0, 255, 0), (0, 0, 255), (75, 0, 130),
            (148, 0, 211), (255, 0, 127),
            (255, 20, 147), (0, 255, 255), (127, 255, 0),
            (255, 69, 0), (0, 128, 128), (139, 0, 139),
            (0, 255, 127), (128, 0, 0),
        ]

    def animacion(self, vueltas=1, delay=0.1):
        for _ in range(vueltas):
            # Efecto hacia un lado
            for _ in range(self.num_leds):
                self.rainbow = self.rainbow[-1:] + self.rainbow[:-1]
                for i in range(self.num_leds):
                    self.pixels[i] = self.rainbow[i]
                self.pixels.write()
                sleep(delay)
            # Efecto hacia el otro lado
            for _ in range(self.num_leds):
                self.rainbow = self.rainbow[1:] + self.rainbow[:1]
                for i in range(self.num_leds):
                    self.pixels[i] = self.rainbow[i]
                self.pixels.write()
                sleep(delay)