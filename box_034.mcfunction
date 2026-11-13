# 034 create_brass/pg_winding, pg_generator, pg_magnet
#area 280 44 318 73
fill 280 64 44 318 91 73 minecraft:air
fill 280 60 44 318 62 73 minecraft:stone
fill 280 63 44 318 63 73 minecraft:light_gray_concrete
fill 284 64 50 318 79 50 minecraft:light_gray_concrete
fill 284 64 50 284 79 67 minecraft:light_gray_concrete
setblock 285 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034.1"}','{"text": "create_brass"}','{"text": "pg_winding"}','{"text": ""}']}}
setblock 286 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Power Grid"}','{"text": "parts, the full"}','{"text": "generator with"}','{"text": "a lamp, the"}']}}
setblock 287 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "self excited"}','{"text": "wiring, the"}','{"text": "electromagnet"}','{"text": "over a depot"}']}}
fill 295 64 50 295 79 67 minecraft:light_gray_concrete
kw testworld place shots:powergrid/generator/generator_1 286 63 52 none
setblock 296 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034.2"}','{"text": "create_brass"}','{"text": "pg_generator"}','{"text": ""}']}}
setblock 297 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ den"}','{"text": "Kollektor an"}','{"text": ""}','{"text": ""}']}}
fill 305 64 50 305 79 67 minecraft:light_gray_concrete
kw testworld place shots:powergrid/generator/generator_3 297 63 52 none
setblock 306 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034.3"}','{"text": "create_brass"}','{"text": "pg_magnet"}','{"text": ""}']}}
setblock 307 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Magnetisier"}','{"text": "Andesitlegierung"}','{"text": ""}','{"text": ""}']}}
fill 313 64 50 313 79 67 minecraft:light_gray_concrete
kw testworld place shots:powergrid/electromagnet 307 63 52 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
