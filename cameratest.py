import mcpi.minecraft as minecraft

a = minecraft.Minecraft.create()
while True:
    print a.player.getRotation()

