# 108 hexerei/herbs
#area 249 176 268 201
fill 249 64 176 268 91 201 minecraft:air
fill 249 60 176 268 62 201 minecraft:stone
fill 249 63 176 268 63 201 minecraft:light_gray_concrete
fill 253 64 182 268 79 182 minecraft:light_gray_concrete
fill 253 64 182 253 79 195 minecraft:light_gray_concrete
setblock 254 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108"}','{"text": "hexerei"}','{"text": "herbs"}','{"text": ""}']}}
setblock 255 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "herb garden"}','{"text": "with all four"}','{"text": "plants grown"}','{"text": ""}']}}
fill 263 64 182 263 79 195 minecraft:light_gray_concrete
fill 256 63 186 260 63 188 minecraft:grass_block
setblock 256 64 186 hexerei:mandrake_plant[age=3]
setblock 257 64 186 hexerei:belladonna_plant[age=3]
setblock 259 64 186 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 186 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 186 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 186 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 256 64 187 hexerei:mandrake_plant[age=3]
setblock 257 64 187 hexerei:belladonna_plant[age=3]
setblock 259 64 187 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 187 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 187 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 187 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 256 64 188 hexerei:mandrake_plant[age=3]
setblock 257 64 188 hexerei:belladonna_plant[age=3]
setblock 259 64 188 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 188 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 188 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 188 hexerei:yellow_dock_bush[half=upper,age=3]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
