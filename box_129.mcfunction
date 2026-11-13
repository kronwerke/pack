# 129 hexerei/candles
#area 294 184 313 209
fill 294 64 184 313 91 209 minecraft:air
fill 294 60 184 313 62 209 minecraft:stone
fill 294 63 184 313 63 209 minecraft:light_gray_concrete
fill 298 64 190 313 79 190 minecraft:light_gray_concrete
fill 298 64 190 298 79 203 minecraft:light_gray_concrete
setblock 299 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129"}','{"text": "hexerei"}','{"text": "candles"}','{"text": ""}']}}
setblock 300 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "candle dipper"}','{"text": "on a tallow"}','{"text": "cauldron with"}','{"text": "candles"}']}}
fill 308 64 190 308 79 203 minecraft:light_gray_concrete
setblock 303 64 195 hexerei:mixing_cauldron
setblock 303 65 195 hexerei:candle_dipper[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
