# 147 theurgy/sal_tank, liquefaction, vessels, array, fermentation
#area 96 338 155 363
fill 96 64 338 140 91 363 minecraft:air
fill 141 64 338 155 91 363 minecraft:air
fill 96 60 338 155 62 363 minecraft:stone
fill 96 63 338 155 63 363 minecraft:light_gray_concrete
fill 100 64 344 155 79 344 minecraft:light_gray_concrete
fill 100 64 344 100 79 357 minecraft:light_gray_concrete
setblock 101 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.1"}','{"text": "theurgy"}','{"text": "sal_tank"}','{"text": ""}']}}
setblock 102 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell Tank und"}','{"text": "Akkumulator auf"}','{"text": ""}','{"text": ""}']}}
fill 110 64 344 110 79 357 minecraft:light_gray_concrete
setblock 105 64 349 theurgy:sal_ammoniac_tank
setblock 105 65 349 theurgy:sal_ammoniac_accumulator
setblock 111 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.2"}','{"text": "theurgy"}','{"text": "liquefaction"}','{"text": ""}']}}
setblock 112 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Löse Sulfur aus"}','{"text": "Raw Iron"}','{"text": ""}','{"text": ""}']}}
fill 120 64 344 120 79 357 minecraft:light_gray_concrete
setblock 115 64 349 theurgy:pyromantic_brazier[lit=true]
setblock 115 65 349 theurgy:liquefaction_cauldron[half=lower,lit=true]
setblock 115 66 349 theurgy:liquefaction_cauldron[half=upper,lit=true]
setblock 121 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.3"}','{"text": "theurgy"}','{"text": "vessels"}','{"text": ""}']}}
setblock 122 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die drei"}','{"text": "Gefäße auf"}','{"text": ""}','{"text": ""}']}}
fill 130 64 344 130 79 357 minecraft:light_gray_concrete
setblock 125 64 349 theurgy:pyromantic_brazier[lit=true]
setblock 125 65 349 theurgy:incubator[half=lower]
setblock 125 66 349 theurgy:incubator[half=upper]
setblock 124 64 349 minecraft:stone_bricks
setblock 124 65 349 theurgy:incubator_salt_vessel
setblock 126 64 349 minecraft:stone_bricks
setblock 126 65 349 theurgy:incubator_sulfur_vessel
setblock 125 64 348 minecraft:stone_bricks
setblock 125 65 348 theurgy:incubator_mercury_vessel
setblock 131 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.4"}','{"text": "theurgy"}','{"text": "array"}','{"text": ""}']}}
setblock 132 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell drei"}','{"text": "Pedestale auf"}','{"text": ""}','{"text": ""}']}}
fill 140 64 344 140 79 357 minecraft:light_gray_concrete
setblock 133 64 349 theurgy:reformation_source_pedestal
setblock 135 64 348 theurgy:reformation_target_pedestal
setblock 137 64 349 theurgy:reformation_result_pedestal
setblock 135 64 351 minecraft:stone_bricks
setblock 135 65 351 theurgy:sulfuric_flux_emitter[facing=up]
setblock 141 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.5"}','{"text": "theurgy"}','{"text": "fermentation"}','{"text": ""}']}}
setblock 142 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Vergär Sulfur"}','{"text": "zu Niter"}','{"text": ""}','{"text": ""}']}}
fill 150 64 344 150 79 357 minecraft:light_gray_concrete
setblock 145 64 349 theurgy:fermentation_vat[facing=south,has_output=false,open=true]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
