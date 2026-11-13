# 086 hexerei/herbs
#area 187 144 206 169
fill 187 64 144 206 91 169 minecraft:air
fill 187 60 144 206 62 169 minecraft:stone
fill 187 63 144 206 63 169 minecraft:light_gray_concrete
fill 191 64 150 206 79 150 minecraft:light_gray_concrete
fill 191 64 150 191 79 163 minecraft:light_gray_concrete
setblock 192 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086"}','{"text": "hexerei"}','{"text": "herbs"}','{"text": ""}']}}
setblock 193 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "herb garden"}','{"text": "with all four"}','{"text": "plants grown"}','{"text": ""}']}}
fill 201 64 150 201 79 163 minecraft:light_gray_concrete
fill 194 63 154 198 63 156 minecraft:grass_block
setblock 194 64 154 hexerei:mandrake_plant[age=3]
setblock 195 64 154 hexerei:belladonna_plant[age=3]
setblock 197 64 154 hexerei:mugwort_bush[half=lower,age=3]
setblock 197 65 154 hexerei:mugwort_bush[half=upper,age=3]
setblock 198 64 154 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 198 65 154 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 194 64 155 hexerei:mandrake_plant[age=3]
setblock 195 64 155 hexerei:belladonna_plant[age=3]
setblock 197 64 155 hexerei:mugwort_bush[half=lower,age=3]
setblock 197 65 155 hexerei:mugwort_bush[half=upper,age=3]
setblock 198 64 155 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 198 65 155 hexerei:yellow_dock_bush[half=upper,age=3]
setblock 194 64 156 hexerei:mandrake_plant[age=3]
setblock 195 64 156 hexerei:belladonna_plant[age=3]
setblock 197 64 156 hexerei:mugwort_bush[half=lower,age=3]
setblock 197 65 156 hexerei:mugwort_bush[half=upper,age=3]
setblock 198 64 156 hexerei:yellow_dock_bush[half=lower,age=3]
setblock 198 65 156 hexerei:yellow_dock_bush[half=upper,age=3]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
