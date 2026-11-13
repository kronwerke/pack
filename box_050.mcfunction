# 050 mekanism_ores/foundry
#area 125 95 144 120
fill 125 64 95 144 91 120 minecraft:air
fill 125 60 95 144 62 120 minecraft:stone
fill 125 63 95 144 63 120 minecraft:light_gray_concrete
fill 129 64 101 144 79 101 minecraft:light_gray_concrete
fill 129 64 101 129 79 114 minecraft:light_gray_concrete
setblock 130 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "050"}','{"text": "mekanism_ores"}','{"text": "foundry"}','{"text": ""}']}}
setblock 131 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Metalworks"}','{"text": "foundry with"}','{"text": "raw ore going"}','{"text": "in and the"}']}}
setblock 132 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ingot cast"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 139 64 101 139 79 114 minecraft:light_gray_concrete
kw testworld place shots:productivemetalworks/foundry_molten 131 63 103 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
