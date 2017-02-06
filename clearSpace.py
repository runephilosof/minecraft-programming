# -*- coding: utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
storrelse = int(raw_input("størrelse der skal ryddes?"))
hojde = int(raw_input("højde der skal ryddes?"))
mc.setBlocks(
    pos.x-storrelse,
    pos.y,
    pos.z-storrelse,
    pos.x+storrelse,
    pos.y+hojde,
    pos.z+storrelse,
    block.AIR.id
    )
