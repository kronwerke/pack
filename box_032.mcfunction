# 032 create_brass/pg_winding, pg_generator, pg_magnet
#area 295 42 333 71
fill 295 64 42 333 91 71 minecraft:air
fill 295 60 42 333 62 71 minecraft:stone
fill 295 63 42 333 63 71 minecraft:light_gray_concrete
fill 299 64 48 333 79 48 minecraft:light_gray_concrete
fill 299 64 48 299 79 65 minecraft:light_gray_concrete
setblock 300 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032.1"}','{"text": "create_brass"}','{"text": "pg_winding"}','{"text": ""}']}}
setblock 301 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Power Grid"}','{"text": "parts, the full"}','{"text": "generator with"}','{"text": "a lamp, the"}']}}
setblock 302 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "self excited"}','{"text": "wiring, the"}','{"text": "electromagnet"}','{"text": "over a depot"}']}}
fill 310 64 48 310 79 65 minecraft:light_gray_concrete
kw testworld place shots:powergrid/generator/generator_1 301 63 50 none
setblock 311 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032.2"}','{"text": "create_brass"}','{"text": "pg_generator"}','{"text": ""}']}}
setblock 312 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ den"}','{"text": "Kollektor an"}','{"text": ""}','{"text": ""}']}}
fill 320 64 48 320 79 65 minecraft:light_gray_concrete
kw testworld place shots:powergrid/generator/generator_3 312 63 50 none
setblock 321 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032.3"}','{"text": "create_brass"}','{"text": "pg_magnet"}','{"text": ""}']}}
setblock 322 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Magnetisier"}','{"text": "Andesitlegierung"}','{"text": ""}','{"text": ""}']}}
fill 328 64 48 328 79 65 minecraft:light_gray_concrete
kw testworld place shots:powergrid/electromagnet 322 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
