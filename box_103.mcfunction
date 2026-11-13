# 103 hexerei/candles
#area 279 146 298 171
fill 279 64 146 298 91 171 minecraft:air
fill 279 60 146 298 62 171 minecraft:stone
fill 279 63 146 298 63 171 minecraft:light_gray_concrete
fill 283 64 152 298 79 152 minecraft:light_gray_concrete
fill 283 64 152 283 79 165 minecraft:light_gray_concrete
setblock 284 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103"}','{"text": "hexerei"}','{"text": "candles"}','{"text": ""}']}}
setblock 285 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "candle dipper"}','{"text": "on a tallow"}','{"text": "cauldron with"}','{"text": "candles"}']}}
fill 293 64 152 293 79 165 minecraft:light_gray_concrete
setblock 288 64 157 hexerei:mixing_cauldron
setblock 288 65 157 hexerei:candle_dipper[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
