from machine import Pin
import utime
import _thread
import sys
import time
import machine

pot_x = machine.ADC(28)
pot_y= machine.ADC(27)
btn=machine.ADC(26)

conversion_factor = 3.3 / (65535)

led = Pin(25, Pin.OUT)
x=""

def Lectura():
    while True:
        global x
        data=str(sys.stdin.readline())
        x=data
        utime.sleep(1)
        
_thread.start_new_thread(Lectura, ())

while True:
    Dx="&"+str(pot_x.read_u16())
    Dy="$"+str(pot_y.read_u16())
    D_btn="%"+str(btn.read_u16())
    
    sys.stdout.write(Dx+"\r\n")
    sys.stdout.write(Dy+"\r\n")
    sys.stdout.write(D_btn+"\r\n")
    #sys.stdout.write("Sistema On \r\n")
    utime.sleep(0.5)
    try:
        a=int(x[0])
        if a == 1:
            led.on()
            sys.stdout.write("Led prendido \r\n")
            
        else:
            led.off()
            sys.stdout.write("Led apagado \r\n")
        x=""
        
    except:
        pass
    