# 187 eidolon/brazier, crucible, altar, stone_altar
#area 181 407 230 432
fill 181 64 407 225 91 432 minecraft:air
fill 226 64 407 230 91 432 minecraft:air
fill 181 60 407 230 62 432 minecraft:stone
fill 181 63 407 230 63 432 minecraft:light_gray_concrete
fill 185 64 413 230 79 413 minecraft:light_gray_concrete
fill 185 64 413 185 79 426 minecraft:light_gray_concrete
setblock 186 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "187.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 187 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 195 64 413 195 79 426 minecraft:light_gray_concrete
setblock 190 64 418 eidolon_repraised:brazier
setblock 188 64 418 eidolon_repraised:stone_hand[facing=east]
setblock 192 64 418 eidolon_repraised:stone_hand[facing=west]
setblock 190 64 416 eidolon_repraised:stone_hand[facing=south]
setblock 196 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "187.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 197 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 205 64 413 205 79 426 minecraft:light_gray_concrete
setblock 200 64 418 minecraft:campfire[facing=south,lit=true]
setblock 200 65 418 eidolon_repraised:crucible
kw testworld use 200 65 418 up minecraft:water_bucket
setblock 206 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "187.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 207 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 215 64 413 215 79 426 minecraft:light_gray_concrete
fill 209 64 418 211 64 418 eidolon_repraised:wooden_altar
setblock 210 65 418 eidolon_repraised:straw_effigy[facing=south]
setblock 209 65 418 eidolon_repraised:candle
setblock 211 65 418 minecraft:skeleton_skull[rotation=8]
setblock 216 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "187.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 217 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 225 64 413 225 79 426 minecraft:light_gray_concrete
fill 219 64 418 221 64 418 eidolon_repraised:stone_altar
setblock 220 65 418 eidolon_repraised:unholy_effigy[facing=south]
setblock 219 65 418 eidolon_repraised:goblet
setblock 221 65 418 eidolon_repraised:candle
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
