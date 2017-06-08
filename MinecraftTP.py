from mcpi.minecraft import Minecraft
import time
import picamera
from mcpi import block
camera = picamera.PiCamera()
mc = Minecraft.create()
wool = 35
while True:
    #time.sleep(1)
    #x, y, z = mc.player.getPos()
    #mc.setBlock(x-1, y, z, 2)
    #mc.setBlock(x-1, y+1, z, wool, 1)
    #mensaje = raw_input("Hello") 
    #if mensaje == "o":
    #   mc.setBlock(x, y-1, z, wool)

    #x, y, z = mc.player.getTilePos()
    #print x, y, z
    #if x == 1 and y == 1 and z == 1:
    #   	camera.capture("/home/pi/Desktop/Maincra.jpg")
    #time.sleep(10)
    #mc.setBlocks(x,y,z,x+2000,y+2000,z+2000,12)
    #mc.postToChat("Bueno, como todos nuestros intentos de greifear son client based, vamos a spammear el chat")
    #mc.postToChat("-.-.-.-.")    


    entityIds = mc.getPlayerEntityIds()
    stEntityId = entityIds[0]
    ndEntityId = entityIds[1]



    ellos = mc.entity.getTilePos(ndEntityId)
    #ellos.y = ellos.y
    mc.player.setPos(ellos)

    



