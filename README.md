# Proyecto Noria con ESP32, Motor y NeoPixel

Este proyecto implementa una **noria controlada con un motor** y un **anillo NeoPixel**, mostrando además información en un **display**.  
El objetivo es sincronizar el motor con los LEDs de NeoPixel para simular el movimiento de la noria iluminada.

---

## 📂 Estructura del proyecto

├── main.py # Archivo principal, coordina todos los módulos
├── motorNoria.py # Control del motor de la noria
├── neoPixelNoria.py # Control del anillo NeoPixel
├── display.py # Control del display (demo_display)

---

## ⚙️ Dependencias

Este proyecto utiliza **MicroPython** en una **ESP32**.  
Asegúrate de tener instalados los siguientes módulos en tu firmware:

- `machine`
- `time`
- `neopixel`

---

## 🧰 Materiales utilizados

- **ESP32** con MicroPython cargado  
- **Motor paso a paso (28BYJ-48 + driver ULN2003)** → mueve la noria  
- **Motor DC** → ventilador para dar aire a los pasajeros  
- **Driver/transistor + diodo de protección** → para controlar el motor DC desde la ESP32  
- **Anillo NeoPixel WS2812B (16 LEDs)** → iluminación sincronizada con la noria  
- **Display TM1637 de 4 dígitos** → muestra mensajes y números  
- **Protoboard** para conexiones  
- **Cables macho-macho**  
- **Cables macho-hembra**  
- **Fuente de alimentación externa** (5V, suficiente corriente para motor paso a paso, DC y NeoPixel)  

---

## 🔌 Conexiones

- **Motor DC** → Controlado desde `motorNoria.py` con pines GPIO.  
- **NeoPixel** → Conectado a un pin de datos de la ESP32 (configurado en `neoPixelNoria.py`).  
- **Display** → Controlado desde `display.py`.  

---

## ▶️ Ejecución

1. Sube los archivos al ESP32 con **Thonny** o **ampy**.  
2. Ejecuta `main.py`.  
3. El sistema:
   - Enciende y controla el **motor de la noria**.  
   - Enciende el **NeoPixel** en sincronía con el motor.  
   - Muestra información en el **display** mediante `demo_display()`.

---

## 📌 Uso de los módulos

- **`motorNoria.py`** → Contiene la clase `MotorNoria` para manejar el motor.  
- **`neoPixelNoria.py`** → Contiene la clase `NeoPixelNoria` para manejar el anillo LED.  
- **`display.py`** → Contiene varias funciones, pero la principal para el proyecto es `demo_display()`.  
- **`main.py`** → Importa los módulos y coordina la ejecución conjunta.

🎯 Objetivo
El propósito del proyecto es sincronizar el movimiento del motor con el encendido de los NeoPixel, logrando que la noria se ilumine en armonía con su giro.
