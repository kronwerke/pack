# 115 hexerei/herbs
#area 249 182 268 207
fill 249 64 182 268 91 207 minecraft:air
fill 249 60 182 268 62 207 minecraft:stone
fill 249 63 182 268 63 207 minecraft:light_gray_concrete
fill 253 64 188 268 79 188 minecraft:light_gray_concrete
fill 253 64 188 253 79 201 minecraft:light_gray_concrete
setblock 254 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115"}','{"text": "hexerei"}','{"text": "herbs"}','{"text": ""}']}}
setblock 255 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "herb garden"}','{"text": "with all four"}','{"text": "plants grown"}','{"text": ""}']}}
fill 263 64 188 263 79 201 minecraft:light_gray_concrete
fill 256 63 192 260 63 194 minecraft:grass_block
setblock 256 64 192 hexerei:mandrake_plant[age=3]
setblock 257 64 192 hexerei:belladonna_plant[age=3]
setblock 259 64 192 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 192 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 192 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 192 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 256 64 193 hexerei:mandrake_plant[age=3]
setblock 257 64 193 hexerei:belladonna_plant[age=3]
setblock 259 64 193 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 193 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 193 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 193 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 256 64 194 hexerei:mandrake_plant[age=3]
setblock 257 64 194 hexerei:belladonna_plant[age=3]
setblock 259 64 194 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 194 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 194 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 194 hexerei:yellow_dock_bush[half=upper,age=3]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
