# 031 create/stock_ticker
fill 187 63 48 198 63 61 minecraft:light_gray_concrete
fill 187 64 48 198 71 48 minecraft:light_gray_concrete
fill 187 64 48 187 71 61 minecraft:light_gray_concrete
setblock 188 64 60 minecraft:air
setblock 188 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "create"}','{"text": "stock_ticker"}','{"text": ""}']}}
setblock 189 64 60 minecraft:air
setblock 189 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a seated"}','{"text": "villager next"}','{"text": "to the stock"}','{"text": "ticker, order"}']}}
setblock 190 64 60 minecraft:air
setblock 190 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "screen open"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
setblock 192 64 53 create:stock_ticker[facing=south]
setblock 191 64 53 create:red_seat
summon minecraft:villager 191.5 64 53.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 193 64 53 create:item_vault
