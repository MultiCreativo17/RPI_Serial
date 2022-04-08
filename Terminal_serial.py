import pygame
import serial
pygame.init()

Rpi= serial.Serial(port = "COM3", baudrate=115200)

try:
    Rpi.Open()
    print("Conectado")
except:
 #   Rpi.close()
    if(Rpi.isOpen()):
        print("Conectado")
    else:
        print("No conectado")

white = (255, 255, 255)

X = 400
Y = 400
  

display_surface = pygame.display.set_mode((X, Y ))
  
pygame.display.set_caption('Terminal Serial')

#Aquí se puede modificar la dirección para cambiar de imagen de fondo
image = pygame.image.load(r'Laberinto.png')



green = (0, 255, 0)
blue = (0, 0, 255)
red=(255,0,0)
 

font = pygame.font.Font('freesansbold.ttf', 20)
text_x = font.render('Datos X', True, green, blue)

textRect_x = text_x.get_rect()
textRect_x.center = (X // 4, 10)

font = pygame.font.Font('freesansbold.ttf', 20)
text_y = font.render('Datos Y', True, green, blue)
textRect_y = text_y.get_rect()
textRect_y.center = ((X // 4)*3, 10)

Rx=""
Ry=""
btn=""

display_surface.fill(white)
display_surface.blit(pygame.transform.scale(image, (400, 400)), (0, 0))

while True :
    if (Rpi.isOpen()):
        dt=Rpi.readline() #Esto se recibe en bytes.
        Dt_s = dt.decode('UTF-8') #Conversión de Byte a String
        
        if (Dt_s[0]=="&"):
            Rx=Dt_s[1:-1]
            #print (Rx)
        if (Dt_s[0]=="$"):
            Ry=(Dt_s[1:-1])
            #print (Ry)
        if (Dt_s[0]=="%"):
            btn=(Dt_s[1:-1])
            #print (btn)
            
    text_x = font.render('Datos X '+Rx, True, green, blue)
    text_y = font.render('Datos Y '+Ry, True, green, blue)

    display_surface.blit(text_x, textRect_x)
    display_surface.blit(text_y, textRect_y)
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            Rpi.close()
            quit() 
    pygame.display.update() 
             
