# 163 eidolon/brazier, crucible, altar, stone_altar
#area 171 374 220 399
fill 171 64 374 215 91 399 minecraft:air
fill 216 64 374 220 91 399 minecraft:air
fill 171 60 374 220 62 399 minecraft:stone
fill 171 63 374 220 63 399 minecraft:light_gray_concrete
fill 175 64 380 220 79 380 minecraft:light_gray_concrete
fill 175 64 380 175 79 393 minecraft:light_gray_concrete
setblock 176 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 177 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 185 64 380 185 79 393 minecraft:light_gray_concrete
setblock 180 64 385 eidolon_repraised:brazier
setblock 178 64 385 eidolon_repraised:stone_hand[facing=east]
setblock 182 64 385 eidolon_repraised:stone_hand[facing=west]
setblock 180 64 383 eidolon_repraised:stone_hand[facing=south]
setblock 186 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 187 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 195 64 380 195 79 393 minecraft:light_gray_concrete
setblock 190 64 385 minecraft:campfire[facing=south,lit=true]
setblock 190 65 385 eidolon_repraised:crucible
kw testworld use 190 65 385 up minecraft:water_bucket
setblock 196 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 197 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 205 64 380 205 79 393 minecraft:light_gray_concrete
fill 199 64 385 201 64 385 eidolon_repraised:wooden_altar
setblock 200 65 385 eidolon_repraised:straw_effigy[facing=south]
setblock 199 65 385 eidolon_repraised:candle
setblock 201 65 385 minecraft:skeleton_skull[rotation=8]
setblock 206 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 207 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 215 64 380 215 79 393 minecraft:light_gray_concrete
fill 209 64 385 211 64 385 eidolon_repraised:stone_altar
setblock 210 65 385 eidolon_repraised:unholy_effigy[facing=south]
setblock 209 65 385 eidolon_repraised:goblet
setblock 211 65 385 eidolon_repraised:candle
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
