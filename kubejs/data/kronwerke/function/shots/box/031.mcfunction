# 031 create/stock_ticker
fill 187 63 52 198 63 65 minecraft:light_gray_concrete
fill 187 64 52 198 71 52 minecraft:light_gray_concrete
fill 187 64 52 187 71 65 minecraft:light_gray_concrete
setblock 188 64 64 minecraft:air
setblock 188 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "create"}','{"text": "stock_ticker"}','{"text": ""}']}}
setblock 189 64 64 minecraft:air
setblock 189 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a seated"}','{"text": "villager next"}','{"text": "to the stock"}','{"text": "ticker, order"}']}}
setblock 190 64 64 minecraft:air
setblock 190 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "screen open"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 192.5 71 57.5 {text:'[{"text": "031  ", "color": "gold"}, {"text": "create/stock_ticker", "color": "gray"}, {"text": "\\nBestell am Lagerticker", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 192 64 57 create:stock_ticker[facing=south]
setblock 191 64 57 create:red_seat
summon minecraft:villager 191.5 64 57.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 193 64 57 create:item_vault
