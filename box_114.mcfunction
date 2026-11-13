# 114 hexerei/candles
#area 279 182 298 207
fill 279 64 182 298 91 207 minecraft:air
fill 279 60 182 298 62 207 minecraft:stone
fill 279 63 182 298 63 207 minecraft:light_gray_concrete
fill 283 64 188 298 79 188 minecraft:light_gray_concrete
fill 283 64 188 283 79 201 minecraft:light_gray_concrete
setblock 284 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "114"}','{"text": "hexerei"}','{"text": "candles"}','{"text": ""}']}}
setblock 285 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "candle dipper"}','{"text": "on a tallow"}','{"text": "cauldron with"}','{"text": "candles"}']}}
fill 293 64 188 293 79 201 minecraft:light_gray_concrete
setblock 288 64 193 hexerei:mixing_cauldron
setblock 288 65 193 hexerei:candle_dipper[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
