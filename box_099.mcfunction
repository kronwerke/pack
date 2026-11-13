# 099 hexerei/candles
#area 279 144 298 169
fill 279 64 144 298 91 169 minecraft:air
fill 279 60 144 298 62 169 minecraft:stone
fill 279 63 144 298 63 169 minecraft:light_gray_concrete
fill 283 64 150 298 79 150 minecraft:light_gray_concrete
fill 283 64 150 283 79 163 minecraft:light_gray_concrete
setblock 284 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099"}','{"text": "hexerei"}','{"text": "candles"}','{"text": ""}']}}
setblock 285 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "candle dipper"}','{"text": "on a tallow"}','{"text": "cauldron with"}','{"text": "candles"}']}}
fill 293 64 150 293 79 163 minecraft:light_gray_concrete
setblock 288 64 155 hexerei:mixing_cauldron
setblock 288 65 155 hexerei:candle_dipper[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
