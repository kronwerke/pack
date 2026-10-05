# 035 create_brass/blaze_burner
fill 255 63 48 266 63 61 minecraft:light_gray_concrete
fill 255 64 48 266 71 48 minecraft:light_gray_concrete
fill 255 64 48 255 71 61 minecraft:light_gray_concrete
setblock 256 64 60 minecraft:air
setblock 256 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "create_brass"}','{"text": "blaze_burner"}','{"text": ""}']}}
setblock 257 64 60 minecraft:air
setblock 257 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "catching a"}','{"text": "blaze with the"}','{"text": "empty burner"}','{"text": "Leeren Brenner"}']}}
setblock 258 64 60 minecraft:air
setblock 258 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "auf die Lohe"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
setblock 257 64 51 create:blaze_burner
summon minecraft:blaze 258.5 64 55.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
