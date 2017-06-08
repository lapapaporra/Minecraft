
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc = Minecraft.create()

# Esto hace tal cosa
#while True:
#	time.sleep(5)
#	mc.postToChat(mc.player.getPos())

pos = mc.player.getPos()
pepito = 0
while True:
	time.sleep(1)
	mc.setBlocks(pos.x, pos.y, pos.z, pos.x+10, pos.y, pos.z+10, block.WOOL.id, pepito)
	pepito = pepito + 1




