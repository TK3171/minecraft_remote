# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Editio
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello Minecraft Java Edition 1.16.5')
mc.setBlocks(65, 4, 65,  71, 4, 71,  param.GOLD_BLOCK)
mc.setBlocks(66, 5, 66,  70, 5, 70,  param.GOLD_BLOCK)
mc.setBlocks(67, 6, 67,  69, 6, 69,  param.GOLD_BLOCK)
mc.setBlocks(68, 7, 68,  68, 7, 68,  param.GOLD_BLOCK)

mc.setBlocks(50, 4, 50,  50, 4, 50,  param.GOLD_BLOCK)

mc.setBlocks(57, 4, 57,  57, 64, 57,  param.GOLD_BLOCK)

mc.setBlocks(55, 4, 58,  55, 10, 58,  param.GOLD_BLOCK)
mc.setBlocks(55, 4, 56,  55, 10, 56,  param.GOLD_BLOCK)
mc.setBlocks(55, 4, 54,  55, 10, 54,  param.GOLD_BLOCK)

mc.setBlocks(52, 10, 55,  52, 10, 60,  param.GOLD_BLOCK)

mc.setBlocks(70, 4, 55,  75, 10, 55,  param.GOLD_BLOCK)

mc.setBlocks(55, 4, 70,  55, 4, 75,  param.GOLD_BLOCK)
mc.setBlocks(56, 5, 70,  56, 5, 75,  param.GOLD_BLOCK)
mc.setBlocks(57, 6, 70,  57, 6, 75,  param.GOLD_BLOCK)