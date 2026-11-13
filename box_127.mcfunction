# 127 hexerei/herbs
#area 264 184 283 209
fill 264 64 184 283 91 209 minecraft:air
fill 264 60 184 283 62 209 minecraft:stone
fill 264 63 184 283 63 209 minecraft:light_gray_concrete
fill 268 64 190 283 79 190 minecraft:light_gray_concrete
fill 268 64 190 268 79 203 minecraft:light_gray_concrete
setblock 269 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127"}','{"text": "hexerei"}','{"text": "herbs"}','{"text": ""}']}}
setblock 270 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "herb garden"}','{"text": "with all four"}','{"text": "plants grown"}','{"text": ""}']}}
fill 278 64 190 278 79 203 minecraft:light_gray_concrete
fill 271 63 194 275 63 196 minecraft:grass_block
setblock 271 64 194 hexerei:mandrake_plant[age=3]
setblock 272 64 194 hexerei:belladonna_plant[age=3]
setblock 274 64 194 hexerei:mugwort_bush[half=lower,age=3]
setblock 274 65 194 hexerei:mugwort_bush[half=upper,age=3]
setblock 275 64 194 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 275 65 194 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 271 64 195 hexerei:mandrake_plant[age=3]
setblock 272 64 195 hexerei:belladonna_plant[age=3]
setblock 274 64 195 hexerei:mugwort_bush[half=lower,age=3]
setblock 274 65 195 hexerei:mugwort_bush[half=upper,age=3]
setblock 275 64 195 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 275 65 195 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 271 64 196 hexerei:mandrake_plant[age=3]
setblock 272 64 196 hexerei:belladonna_plant[age=3]
setblock 274 64 196 hexerei:mugwort_bush[half=lower,age=3]
setblock 274 65 196 hexerei:mugwort_bush[half=upper,age=3]
setblock 275 64 196 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 275 65 196 hexerei:yellow_dock_bush[half=upper,age=3]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
