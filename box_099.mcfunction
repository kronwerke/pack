# 099 hexerei/herbs
#area 249 146 268 171
fill 249 64 146 268 91 171 minecraft:air
fill 249 60 146 268 62 171 minecraft:stone
fill 249 63 146 268 63 171 minecraft:light_gray_concrete
fill 253 64 152 268 79 152 minecraft:light_gray_concrete
fill 253 64 152 253 79 165 minecraft:light_gray_concrete
setblock 254 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099"}','{"text": "hexerei"}','{"text": "herbs"}','{"text": ""}']}}
setblock 255 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "herb garden"}','{"text": "with all four"}','{"text": "plants grown"}','{"text": ""}']}}
fill 263 64 152 263 79 165 minecraft:light_gray_concrete
fill 256 63 156 260 63 158 minecraft:grass_block
setblock 256 64 156 hexerei:mandrake_plant[age=3]
setblock 257 64 156 hexerei:belladonna_plant[age=3]
setblock 259 64 156 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 156 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 156 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 156 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 256 64 157 hexerei:mandrake_plant[age=3]
setblock 257 64 157 hexerei:belladonna_plant[age=3]
setblock 259 64 157 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 157 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 157 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 157 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 256 64 158 hexerei:mandrake_plant[age=3]
setblock 257 64 158 hexerei:belladonna_plant[age=3]
setblock 259 64 158 hexerei:mugwort_bush[half=lower,age=3]
setblock 259 65 158 hexerei:mugwort_bush[half=upper,age=3]
setblock 260 64 158 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 260 65 158 hexerei:yellow_dock_bush[half=upper,age=3]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
