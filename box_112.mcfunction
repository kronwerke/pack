# 112 hexerei/herbs
#area 249 180 268 205
fill 249 64 180 268 91 205 minecraft:air
fill 249 60 180 268 62 205 minecraft:stone
fill 249 63 180 268 63 205 minecraft:light_gray_concrete
fill 253 64 186 268 79 186 minecraft:light_gray_concrete
fill 253 64 186 253 79 199 minecraft:light_gray_concrete
setblock 254 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112"}','{"text": "hexerei"}','{"text": "herbs"}','{"text": ""}']}}
setblock 255 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "herb garden"}','{"text": "with all four"}','{"text": "plants grown"}','{"text": ""}']}}
fill 263 64 186 263 79 199 minecraft:light_gray_concrete
fill 256 63 190 260 63 192 minecraft:grass_block
setblock 256 64 190 hexerei:mandrake_plant[age=3]
setblock 257 64 190 hexerei:belladonna_plant[age=3]
setblock 259 64 190 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 190 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 190 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 190 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 256 64 191 hexerei:mandrake_plant[age=3]
setblock 257 64 191 hexerei:belladonna_plant[age=3]
setblock 259 64 191 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 191 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 191 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 191 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 256 64 192 hexerei:mandrake_plant[age=3]
setblock 257 64 192 hexerei:belladonna_plant[age=3]
setblock 259 64 192 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 192 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 192 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 192 hexerei:yellow_dock_bush[half=upper,age=3]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
