# 172 eidolon/brazier, crucible, altar, stone_altar
#area 181 405 230 430
fill 181 64 405 225 91 430 minecraft:air
fill 226 64 405 230 91 430 minecraft:air
fill 181 60 405 230 62 430 minecraft:stone
fill 181 63 405 230 63 430 minecraft:light_gray_concrete
fill 185 64 411 230 79 411 minecraft:light_gray_concrete
fill 185 64 411 185 79 424 minecraft:light_gray_concrete
setblock 186 64 423 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 187 64 423 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 195 64 411 195 79 424 minecraft:light_gray_concrete
setblock 190 64 416 eidolon_repraised:brazier
setblock 188 64 416 eidolon_repraised:stone_hand[facing=east]
setblock 192 64 416 eidolon_repraised:stone_hand[facing=west]
setblock 190 64 414 eidolon_repraised:stone_hand[facing=south]
setblock 196 64 423 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 197 64 423 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 205 64 411 205 79 424 minecraft:light_gray_concrete
setblock 200 64 416 minecraft:campfire[facing=south,lit=true]
setblock 200 65 416 eidolon_repraised:crucible
kw testworld use 200 65 416 up minecraft:water_bucket
setblock 206 64 423 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 207 64 423 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 215 64 411 215 79 424 minecraft:light_gray_concrete
fill 209 64 416 211 64 416 eidolon_repraised:wooden_altar
setblock 210 65 416 eidolon_repraised:straw_effigy[facing=south]
setblock 209 65 416 eidolon_repraised:candle
setblock 211 65 416 minecraft:skeleton_skull[rotation=8]
setblock 216 64 423 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 217 64 423 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 225 64 411 225 79 424 minecraft:light_gray_concrete
fill 219 64 416 221 64 416 eidolon_repraised:stone_altar
setblock 220 65 416 eidolon_repraised:unholy_effigy[facing=south]
setblock 219 65 416 eidolon_repraised:goblet
setblock 221 65 416 eidolon_repraised:candle
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
