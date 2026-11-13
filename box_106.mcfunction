# 106 theurgy/sal_tank, liquefaction, vessels, array, fermentation
#area 96 317 155 342
fill 96 64 317 140 91 342 minecraft:air
fill 141 64 317 155 91 342 minecraft:air
fill 96 60 317 155 62 342 minecraft:stone
fill 96 63 317 155 63 342 minecraft:light_gray_concrete
fill 100 64 323 155 79 323 minecraft:light_gray_concrete
fill 100 64 323 100 79 336 minecraft:light_gray_concrete
setblock 101 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106.1"}','{"text": "theurgy"}','{"text": "sal_tank"}','{"text": ""}']}}
setblock 102 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell Tank und"}','{"text": "Akkumulator auf"}','{"text": ""}','{"text": ""}']}}
fill 110 64 323 110 79 336 minecraft:light_gray_concrete
setblock 105 64 328 theurgy:sal_ammoniac_tank
setblock 105 65 328 theurgy:sal_ammoniac_accumulator
setblock 111 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106.2"}','{"text": "theurgy"}','{"text": "liquefaction"}','{"text": ""}']}}
setblock 112 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Löse Sulfur aus"}','{"text": "Raw Iron"}','{"text": ""}','{"text": ""}']}}
fill 120 64 323 120 79 336 minecraft:light_gray_concrete
setblock 115 64 328 theurgy:pyromantic_brazier[lit=true]
setblock 115 65 328 theurgy:liquefaction_cauldron[half=lower,lit=true]
setblock 115 66 328 theurgy:liquefaction_cauldron[half=upper,lit=true]
setblock 121 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106.3"}','{"text": "theurgy"}','{"text": "vessels"}','{"text": ""}']}}
setblock 122 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die drei"}','{"text": "Gefäße auf"}','{"text": ""}','{"text": ""}']}}
fill 130 64 323 130 79 336 minecraft:light_gray_concrete
setblock 125 64 328 theurgy:pyromantic_brazier[lit=true]
setblock 125 65 328 theurgy:incubator[half=lower]
setblock 125 66 328 theurgy:incubator[half=upper]
setblock 124 64 328 minecraft:stone_bricks
setblock 124 65 328 theurgy:incubator_salt_vessel
setblock 126 64 328 minecraft:stone_bricks
setblock 126 65 328 theurgy:incubator_sulfur_vessel
setblock 125 64 327 minecraft:stone_bricks
setblock 125 65 327 theurgy:incubator_mercury_vessel
setblock 131 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106.4"}','{"text": "theurgy"}','{"text": "array"}','{"text": ""}']}}
setblock 132 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell drei"}','{"text": "Pedestale auf"}','{"text": ""}','{"text": ""}']}}
fill 140 64 323 140 79 336 minecraft:light_gray_concrete
setblock 133 64 328 theurgy:reformation_source_pedestal
setblock 135 64 327 theurgy:reformation_target_pedestal
setblock 137 64 328 theurgy:reformation_result_pedestal
setblock 135 64 330 minecraft:stone_bricks
setblock 135 65 330 theurgy:sulfuric_flux_emitter[facing=up]
setblock 141 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106.5"}','{"text": "theurgy"}','{"text": "fermentation"}','{"text": ""}']}}
setblock 142 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Vergär Sulfur"}','{"text": "zu Niter"}','{"text": ""}','{"text": ""}']}}
fill 150 64 323 150 79 336 minecraft:light_gray_concrete
setblock 145 64 328 theurgy:fermentation_vat[facing=south,has_output=false,open=true]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
