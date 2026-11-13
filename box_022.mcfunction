# 022 create/stock_ticker
#area 138 42 158 68
fill 138 64 42 158 91 68 minecraft:air
fill 138 60 42 158 62 68 minecraft:stone
fill 138 63 42 158 63 68 minecraft:light_gray_concrete
fill 142 64 48 158 79 48 minecraft:light_gray_concrete
fill 142 64 48 142 79 62 minecraft:light_gray_concrete
setblock 143 64 61 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "022"}','{"text": "create"}','{"text": "stock_ticker"}','{"text": ""}']}}
setblock 144 64 61 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a seated"}','{"text": "villager next"}','{"text": "to the stock"}','{"text": "ticker, order"}']}}
setblock 145 64 61 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "screen open"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 153 64 48 153 79 62 minecraft:light_gray_concrete
kw testworld place shots:create/high_logistics/stock_ticker 144 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
