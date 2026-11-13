# 163 eidolon/brazier, crucible, altar, stone_altar
#area 171 376 220 401
fill 171 64 376 215 91 401 minecraft:air
fill 216 64 376 220 91 401 minecraft:air
fill 171 60 376 220 62 401 minecraft:stone
fill 171 63 376 220 63 401 minecraft:light_gray_concrete
fill 175 64 382 220 79 382 minecraft:light_gray_concrete
fill 175 64 382 175 79 395 minecraft:light_gray_concrete
setblock 176 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 177 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 185 64 382 185 79 395 minecraft:light_gray_concrete
setblock 180 64 387 eidolon_repraised:brazier
setblock 178 64 387 eidolon_repraised:stone_hand[facing=east]
setblock 182 64 387 eidolon_repraised:stone_hand[facing=west]
setblock 180 64 385 eidolon_repraised:stone_hand[facing=south]
setblock 186 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 187 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 195 64 382 195 79 395 minecraft:light_gray_concrete
setblock 190 64 387 minecraft:campfire[facing=south,lit=true]
setblock 190 65 387 eidolon_repraised:crucible
kw testworld use 190 65 387 up minecraft:water_bucket
setblock 196 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 197 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 205 64 382 205 79 395 minecraft:light_gray_concrete
fill 199 64 387 201 64 387 eidolon_repraised:wooden_altar
setblock 200 65 387 eidolon_repraised:straw_effigy[facing=south]
setblock 199 65 387 eidolon_repraised:candle
setblock 201 65 387 minecraft:skeleton_skull[rotation=8]
setblock 206 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 207 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 215 64 382 215 79 395 minecraft:light_gray_concrete
fill 209 64 387 211 64 387 eidolon_repraised:stone_altar
setblock 210 65 387 eidolon_repraised:unholy_effigy[facing=south]
setblock 209 65 387 eidolon_repraised:goblet
setblock 211 65 387 eidolon_repraised:candle
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
