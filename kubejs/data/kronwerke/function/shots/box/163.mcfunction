# 163 hexerei/crow
fill 345 63 224 356 63 237 minecraft:light_gray_concrete
fill 345 64 224 356 71 224 minecraft:light_gray_concrete
fill 345 64 224 345 71 237 minecraft:light_gray_concrete
setblock 346 64 236 minecraft:air
setblock 346 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163"}','{"text": "hexerei"}','{"text": "crow"}','{"text": ""}']}}
setblock 347 64 236 minecraft:air
setblock 347 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crow on the"}','{"text": "shoulder, crow"}','{"text": "flute menu"}','{"text": ""}']}}
setblock 354 64 233 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"hexerei:crow_flute",count:1}]}
summon hexerei:crow 348.5 64 231.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
