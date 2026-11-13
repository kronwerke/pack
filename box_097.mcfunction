# 097 hexerei/herbs
#area 249 144 268 169
fill 249 64 144 268 91 169 minecraft:air
fill 249 60 144 268 62 169 minecraft:stone
fill 249 63 144 268 63 169 minecraft:light_gray_concrete
fill 253 64 150 268 79 150 minecraft:light_gray_concrete
fill 253 64 150 253 79 163 minecraft:light_gray_concrete
setblock 254 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097"}','{"text": "hexerei"}','{"text": "herbs"}','{"text": ""}']}}
setblock 255 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "herb garden"}','{"text": "with all four"}','{"text": "plants grown"}','{"text": ""}']}}
fill 263 64 150 263 79 163 minecraft:light_gray_concrete
fill 256 63 154 260 63 156 minecraft:grass_block
setblock 256 64 154 hexerei:mandrake_plant[age=3]
setblock 257 64 154 hexerei:belladonna_plant[age=3]
setblock 259 64 154 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 154 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 154 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 154 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 256 64 155 hexerei:mandrake_plant[age=3]
setblock 257 64 155 hexerei:belladonna_plant[age=3]
setblock 259 64 155 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 155 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 155 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 155 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 256 64 156 hexerei:mandrake_plant[age=3]
setblock 257 64 156 hexerei:belladonna_plant[age=3]
setblock 259 64 156 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 156 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 156 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 156 hexerei:yellow_dock_bush[half=upper,age=3]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
