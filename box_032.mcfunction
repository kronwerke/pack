# 032 create_brass/pg_winding, pg_generator, pg_magnet
#area 280 42 318 71
fill 280 64 42 318 91 71 minecraft:air
fill 280 60 42 318 62 71 minecraft:stone
fill 280 63 42 318 63 71 minecraft:light_gray_concrete
fill 284 64 48 318 79 48 minecraft:light_gray_concrete
fill 284 64 48 284 79 65 minecraft:light_gray_concrete
setblock 285 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032.1"}','{"text": "create_brass"}','{"text": "pg_winding"}','{"text": ""}']}}
setblock 286 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Power Grid"}','{"text": "parts, the full"}','{"text": "generator with"}','{"text": "a lamp, the"}']}}
setblock 287 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "self excited"}','{"text": "wiring, the"}','{"text": "electromagnet"}','{"text": "over a depot"}']}}
fill 295 64 48 295 79 65 minecraft:light_gray_concrete
kw testworld place shots:powergrid/generator/generator_1 286 63 50 none
setblock 296 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032.2"}','{"text": "create_brass"}','{"text": "pg_generator"}','{"text": ""}']}}
setblock 297 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ den"}','{"text": "Kollektor an"}','{"text": ""}','{"text": ""}']}}
fill 305 64 48 305 79 65 minecraft:light_gray_concrete
kw testworld place shots:powergrid/generator/generator_3 297 63 50 none
setblock 306 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032.3"}','{"text": "create_brass"}','{"text": "pg_magnet"}','{"text": ""}']}}
setblock 307 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Magnetisier"}','{"text": "Andesitlegierung"}','{"text": ""}','{"text": ""}']}}
fill 313 64 48 313 79 65 minecraft:light_gray_concrete
kw testworld place shots:powergrid/electromagnet 307 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
