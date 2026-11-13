# 114 hexerei/candles
#area 279 180 298 205
fill 279 64 180 298 91 205 minecraft:air
fill 279 60 180 298 62 205 minecraft:stone
fill 279 63 180 298 63 205 minecraft:light_gray_concrete
fill 283 64 186 298 79 186 minecraft:light_gray_concrete
fill 283 64 186 283 79 199 minecraft:light_gray_concrete
setblock 284 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "114"}','{"text": "hexerei"}','{"text": "candles"}','{"text": ""}']}}
setblock 285 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "candle dipper"}','{"text": "on a tallow"}','{"text": "cauldron with"}','{"text": "candles"}']}}
fill 293 64 186 293 79 199 minecraft:light_gray_concrete
setblock 288 64 191 hexerei:mixing_cauldron
setblock 288 65 191 hexerei:candle_dipper[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
