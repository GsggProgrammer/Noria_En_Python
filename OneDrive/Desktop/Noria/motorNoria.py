from machine import Pin
from utime import sleep

class MotorNoria:
    def __init__(self, p1=15, p2=2, p3=4, p4=5):
        self.m1 = Pin(p1, Pin.OUT)
        self.m2 = Pin(p2, Pin.OUT)
        self.m3 = Pin(p3, Pin.OUT)
        self.m4 = Pin(p4, Pin.OUT)
        self.apagar()

    def salida(self, a, b, c, d, delay=0.01):
        self.m1.value(a)
        self.m2.value(b)
        self.m3.value(c)
        self.m4.value(d)
        sleep(delay)

    def apagar(self):
        self.salida(0, 0, 0, 0)

    def giro_simplei(self, pasos, debug=False):
        for i in range(pasos):
            self.salida(0, 0, 0, 1)
            self.salida(0, 0, 1, 0)
            self.salida(0, 1, 0, 0)
            self.salida(1, 0, 0, 0)
            if debug:
                print(f"Paso {i+1}/{pasos} izquierda")

    def giro_simpled(self, pasos, debug=False):
        for i in range(pasos):
            self.salida(1, 0, 0, 0)
            self.salida(0, 1, 0, 0)
            self.salida(0, 0, 1, 0)
            self.salida(0, 0, 0, 1)
            if debug:
                print(f"Paso {i+1}/{pasos} derecha")

    def _ciclo(self, metodo, texto):
        print(f"Primera cabina {texto} sin movimiento previo")
        for i in range(8):
            metodo(6)
            sleep(1)
            print(f"Cabina número {i+2} {texto}")

    def carga(self):
        self._ciclo(self.giro_simpled, "cargada")

    def descarga(self):
        self._ciclo(self.giro_simplei, "descargada")