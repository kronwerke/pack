# 149 theurgy/sal_tank, liquefaction, vessels, array, fermentation
#area 96 340 155 365
fill 96 64 340 140 91 365 minecraft:air
fill 141 64 340 155 91 365 minecraft:air
fill 96 60 340 155 62 365 minecraft:stone
fill 96 63 340 155 63 365 minecraft:light_gray_concrete
fill 100 64 346 155 79 346 minecraft:light_gray_concrete
fill 100 64 346 100 79 359 minecraft:light_gray_concrete
setblock 101 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149.1"}','{"text": "theurgy"}','{"text": "sal_tank"}','{"text": ""}']}}
setblock 102 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell Tank und"}','{"text": "Akkumulator auf"}','{"text": ""}','{"text": ""}']}}
fill 110 64 346 110 79 359 minecraft:light_gray_concrete
setblock 105 64 351 theurgy:sal_ammoniac_tank
setblock 105 65 351 theurgy:sal_ammoniac_accumulator
setblock 111 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149.2"}','{"text": "theurgy"}','{"text": "liquefaction"}','{"text": ""}']}}
setblock 112 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Löse Sulfur aus"}','{"text": "Raw Iron"}','{"text": ""}','{"text": ""}']}}
fill 120 64 346 120 79 359 minecraft:light_gray_concrete
setblock 115 64 351 theurgy:pyromantic_brazier[lit=true]
setblock 115 65 351 theurgy:liquefaction_cauldron[half=lower,lit=true]
setblock 115 66 351 theurgy:liquefaction_cauldron[half=upper,lit=true]
setblock 121 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149.3"}','{"text": "theurgy"}','{"text": "vessels"}','{"text": ""}']}}
setblock 122 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die drei"}','{"text": "Gefäße auf"}','{"text": ""}','{"text": ""}']}}
fill 130 64 346 130 79 359 minecraft:light_gray_concrete
setblock 125 64 351 theurgy:pyromantic_brazier[lit=true]
setblock 125 65 351 theurgy:incubator[half=lower]
setblock 125 66 351 theurgy:incubator[half=upper]
setblock 124 64 351 minecraft:stone_bricks
setblock 124 65 351 theurgy:incubator_salt_vessel
setblock 126 64 351 minecraft:stone_bricks
setblock 126 65 351 theurgy:incubator_sulfur_vessel
setblock 125 64 350 minecraft:stone_bricks
setblock 125 65 350 theurgy:incubator_mercury_vessel
setblock 131 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149.4"}','{"text": "theurgy"}','{"text": "array"}','{"text": ""}']}}
setblock 132 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell drei"}','{"text": "Pedestale auf"}','{"text": ""}','{"text": ""}']}}
fill 140 64 346 140 79 359 minecraft:light_gray_concrete
setblock 133 64 351 theurgy:reformation_source_pedestal
setblock 135 64 350 theurgy:reformation_target_pedestal
setblock 137 64 351 theurgy:reformation_result_pedestal
setblock 135 64 353 minecraft:stone_bricks
setblock 135 65 353 theurgy:sulfuric_flux_emitter[facing=up]
setblock 141 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149.5"}','{"text": "theurgy"}','{"text": "fermentation"}','{"text": ""}']}}
setblock 142 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Vergär Sulfur"}','{"text": "zu Niter"}','{"text": ""}','{"text": ""}']}}
fill 150 64 346 150 79 359 minecraft:light_gray_concrete
setblock 145 64 351 theurgy:fermentation_vat[facing=south,has_output=false,open=true]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
