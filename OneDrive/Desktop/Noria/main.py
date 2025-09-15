from motorNoria import MotorNoria
from neoPixelNoria import NeoPixelNoria
from display import DisplayNoria
from utime import sleep

# Inicializar motor
motor = MotorNoria(15, 2, 4, 5)

# Inicializar NeoPixel
neopixel = NeoPixelNoria(12, 16)

# Inicializar Display
display = DisplayNoria(2, 5)

print("Bienvenidos a la Noria más grande y exclusiva de la ciudad!")
sleep(2.5)

# Cargar cabinas
motor.carga()
sleep(1)

print("Listos!!?? Empezamos en:")
for i in range(5, 0, -1):
    print(i)
    display.tm.number(i)  # mostrar countdown en display
    sleep(1)
print("FUERA!")

# Girar la noria 15 vueltas (750 pasos)
motor.giro_simplei(750)
sleep(1)

print("Que tal estuvo???. Tranquilos... Pueden Reposar")
display.tm.show("REST")
sleep(3)

print("Empieza la descarga en:")
for i in range(5, 0, -1):
    print(i)
    display.tm.number(i)
    sleep(1)

motor.descarga()

# Demo del display
display.demo_display()

# Animación NeoPixel (2 ciclos de ida y vuelta)
neopixel.animacion(vueltas=2)