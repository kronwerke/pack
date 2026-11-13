# 110 hexerei/candles
#area 279 176 298 201
fill 279 64 176 298 91 201 minecraft:air
fill 279 60 176 298 62 201 minecraft:stone
fill 279 63 176 298 63 201 minecraft:light_gray_concrete
fill 283 64 182 298 79 182 minecraft:light_gray_concrete
fill 283 64 182 283 79 195 minecraft:light_gray_concrete
setblock 284 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "110"}','{"text": "hexerei"}','{"text": "candles"}','{"text": ""}']}}
setblock 285 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "candle dipper"}','{"text": "on a tallow"}','{"text": "cauldron with"}','{"text": "candles"}']}}
fill 293 64 182 293 79 195 minecraft:light_gray_concrete
setblock 288 64 187 hexerei:mixing_cauldron
setblock 288 65 187 hexerei:candle_dipper[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
