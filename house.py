# -*- coding: utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
storrelse = int(raw_input("størrelse på hus?"))
hojde = int(raw_input("højde på hus?"))
mc.setBlocks(
    pos.x+2,
    pos.y,
    pos.z,
    pos.x+storrelse,
    pos.y+hojde,
    pos.z+storrelse,
    block.BRICK_BLOCK.id
    )
mc.setBlocks(
    pos.x+2,
    pos.y-1,
    pos.z,
    pos.x+storrelse,
    pos.y-1,
    pos.z+storrelse,
    block.WOOD_PLANKS.id
    )
mc.setBlocks(
    pos.x+3,
    pos.y,
    pos.z+2,
    pos.x+storrelse-1,
    pos.y+hojde-1,
    pos.z+storrelse-1,
    block.AIR.id
    )
