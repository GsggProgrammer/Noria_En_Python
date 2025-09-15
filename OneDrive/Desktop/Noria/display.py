from tm1637 import TM1637
from machine import Pin
import time

class DisplayNoria:
    def __init__(self, clk=2, dio=5):
        self.tm = TM1637(clk=Pin(clk), dio=Pin(dio))

    def demo_display(self):
        self.tm.number(12)
        time.sleep(1)
        self.tm.show("PEPE")
        time.sleep(1)
        self.tm.scroll("Bienvenidos a la Noria")