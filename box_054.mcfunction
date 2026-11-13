# 054 mekanism_ores/foundry
#area 140 97 163 132
fill 140 64 97 163 91 132 minecraft:air
fill 140 60 97 163 62 132 minecraft:stone
fill 140 63 97 163 63 132 minecraft:light_gray_concrete
fill 144 64 103 163 79 103 minecraft:light_gray_concrete
fill 144 64 103 144 79 126 minecraft:light_gray_concrete
setblock 145 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "mekanism_ores"}','{"text": "foundry"}','{"text": ""}']}}
setblock 146 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Metalworks"}','{"text": "foundry with"}','{"text": "raw ore going"}','{"text": "in and the"}']}}
setblock 147 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ingot cast"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 158 64 103 158 79 126 minecraft:light_gray_concrete
kw testworld place shots:productivemetalworks/foundry_molten 148 63 107 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
