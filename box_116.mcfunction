# 116 theurgy/sal_tank, liquefaction, vessels, array, fermentation
#area 96 336 155 361
fill 96 64 336 140 91 361 minecraft:air
fill 141 64 336 155 91 361 minecraft:air
fill 96 60 336 155 62 361 minecraft:stone
fill 96 63 336 155 63 361 minecraft:light_gray_concrete
fill 100 64 342 155 79 342 minecraft:light_gray_concrete
fill 100 64 342 100 79 355 minecraft:light_gray_concrete
setblock 101 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.1"}','{"text": "theurgy"}','{"text": "sal_tank"}','{"text": ""}']}}
setblock 102 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell Tank und"}','{"text": "Akkumulator auf"}','{"text": ""}','{"text": ""}']}}
fill 110 64 342 110 79 355 minecraft:light_gray_concrete
setblock 105 64 347 theurgy:sal_ammoniac_tank
setblock 105 65 347 theurgy:sal_ammoniac_accumulator
setblock 111 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.2"}','{"text": "theurgy"}','{"text": "liquefaction"}','{"text": ""}']}}
setblock 112 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Löse Sulfur aus"}','{"text": "Raw Iron"}','{"text": ""}','{"text": ""}']}}
fill 120 64 342 120 79 355 minecraft:light_gray_concrete
setblock 115 64 347 theurgy:pyromantic_brazier[lit=true]
setblock 115 65 347 theurgy:liquefaction_cauldron[half=lower,lit=true]
setblock 115 66 347 theurgy:liquefaction_cauldron[half=upper,lit=true]
setblock 121 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.3"}','{"text": "theurgy"}','{"text": "vessels"}','{"text": ""}']}}
setblock 122 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die drei"}','{"text": "Gefäße auf"}','{"text": ""}','{"text": ""}']}}
fill 130 64 342 130 79 355 minecraft:light_gray_concrete
setblock 125 64 347 theurgy:pyromantic_brazier[lit=true]
setblock 125 65 347 theurgy:incubator[half=lower]
setblock 125 66 347 theurgy:incubator[half=upper]
setblock 124 64 347 minecraft:stone_bricks
setblock 124 65 347 theurgy:incubator_salt_vessel
setblock 126 64 347 minecraft:stone_bricks
setblock 126 65 347 theurgy:incubator_sulfur_vessel
setblock 125 64 346 minecraft:stone_bricks
setblock 125 65 346 theurgy:incubator_mercury_vessel
setblock 131 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.4"}','{"text": "theurgy"}','{"text": "array"}','{"text": ""}']}}
setblock 132 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell drei"}','{"text": "Pedestale auf"}','{"text": ""}','{"text": ""}']}}
fill 140 64 342 140 79 355 minecraft:light_gray_concrete
setblock 133 64 347 theurgy:reformation_source_pedestal
setblock 135 64 346 theurgy:reformation_target_pedestal
setblock 137 64 347 theurgy:reformation_result_pedestal
setblock 135 64 349 minecraft:stone_bricks
setblock 135 65 349 theurgy:sulfuric_flux_emitter[facing=up]
setblock 141 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.5"}','{"text": "theurgy"}','{"text": "fermentation"}','{"text": ""}']}}
setblock 142 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Vergär Sulfur"}','{"text": "zu Niter"}','{"text": ""}','{"text": ""}']}}
fill 150 64 342 150 79 355 minecraft:light_gray_concrete
setblock 145 64 347 theurgy:fermentation_vat[facing=south,has_output=false,open=true]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
