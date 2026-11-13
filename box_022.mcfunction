# 022 create/stock_ticker
#area 123 42 143 68
fill 123 64 42 143 91 68 minecraft:air
fill 123 60 42 143 62 68 minecraft:stone
fill 123 63 42 143 63 68 minecraft:light_gray_concrete
fill 127 64 48 143 79 48 minecraft:light_gray_concrete
fill 127 64 48 127 79 62 minecraft:light_gray_concrete
setblock 128 64 61 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "022"}','{"text": "create"}','{"text": "stock_ticker"}','{"text": ""}']}}
setblock 129 64 61 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a seated"}','{"text": "villager next"}','{"text": "to the stock"}','{"text": "ticker, order"}']}}
setblock 130 64 61 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "screen open"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 138 64 48 138 79 62 minecraft:light_gray_concrete
kw testworld place shots:create/high_logistics/stock_ticker 129 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
