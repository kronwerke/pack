# 024 create/stock_ticker
#area 123 44 143 70
fill 123 64 44 143 91 70 minecraft:air
fill 123 60 44 143 62 70 minecraft:stone
fill 123 63 44 143 63 70 minecraft:light_gray_concrete
fill 127 64 50 143 79 50 minecraft:light_gray_concrete
fill 127 64 50 127 79 64 minecraft:light_gray_concrete
setblock 128 64 63 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "024"}','{"text": "create"}','{"text": "stock_ticker"}','{"text": ""}']}}
setblock 129 64 63 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a seated"}','{"text": "villager next"}','{"text": "to the stock"}','{"text": "ticker, order"}']}}
setblock 130 64 63 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "screen open"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 138 64 50 138 79 64 minecraft:light_gray_concrete
kw testworld place shots:create/high_logistics/stock_ticker 129 63 52 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
