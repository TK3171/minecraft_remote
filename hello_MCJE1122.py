# Hello World for Minecraft Java Edition 1.12.2 or earlier
from mcpi.minecraft import Minecraft
import param_MCJE1122 as param

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello Minecraft Java Edition 1.12.2')
mc.setBlocks(320, 10, -750,  330, 15, -770,  param.GOLD_BLOCK)
