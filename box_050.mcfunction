# 050 mekanism_ores/foundry
#area 125 95 148 130
fill 125 64 95 148 91 130 minecraft:air
fill 125 60 95 148 62 130 minecraft:stone
fill 125 63 95 148 63 130 minecraft:light_gray_concrete
fill 129 64 101 148 79 101 minecraft:light_gray_concrete
fill 129 64 101 129 79 124 minecraft:light_gray_concrete
setblock 130 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "050"}','{"text": "mekanism_ores"}','{"text": "foundry"}','{"text": ""}']}}
setblock 131 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Metalworks"}','{"text": "foundry with"}','{"text": "raw ore going"}','{"text": "in and the"}']}}
setblock 132 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ingot cast"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 143 64 101 143 79 124 minecraft:light_gray_concrete
kw testworld place shots:productivemetalworks/foundry_molten 133 63 105 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
