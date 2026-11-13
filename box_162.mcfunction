# 162 theurgy/sal_tank, liquefaction, vessels, array, fermentation
#area 116 374 175 399
fill 116 64 374 160 91 399 minecraft:air
fill 161 64 374 175 91 399 minecraft:air
fill 116 60 374 175 62 399 minecraft:stone
fill 116 63 374 175 63 399 minecraft:light_gray_concrete
fill 120 64 380 175 79 380 minecraft:light_gray_concrete
fill 120 64 380 120 79 393 minecraft:light_gray_concrete
setblock 121 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.1"}','{"text": "theurgy"}','{"text": "sal_tank"}','{"text": ""}']}}
setblock 122 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell Tank und"}','{"text": "Akkumulator auf"}','{"text": ""}','{"text": ""}']}}
fill 130 64 380 130 79 393 minecraft:light_gray_concrete
setblock 125 64 385 theurgy:sal_ammoniac_tank
setblock 125 65 385 theurgy:sal_ammoniac_accumulator
setblock 131 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.2"}','{"text": "theurgy"}','{"text": "liquefaction"}','{"text": ""}']}}
setblock 132 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Löse Sulfur aus"}','{"text": "Raw Iron"}','{"text": ""}','{"text": ""}']}}
fill 140 64 380 140 79 393 minecraft:light_gray_concrete
setblock 135 64 385 theurgy:pyromantic_brazier[lit=true]
setblock 135 65 385 theurgy:liquefaction_cauldron[half=lower,lit=true]
setblock 135 66 385 theurgy:liquefaction_cauldron[half=upper,lit=true]
setblock 141 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.3"}','{"text": "theurgy"}','{"text": "vessels"}','{"text": ""}']}}
setblock 142 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die drei"}','{"text": "Gefäße auf"}','{"text": ""}','{"text": ""}']}}
fill 150 64 380 150 79 393 minecraft:light_gray_concrete
setblock 145 64 385 theurgy:pyromantic_brazier[lit=true]
setblock 145 65 385 theurgy:incubator[half=lower]
setblock 145 66 385 theurgy:incubator[half=upper]
setblock 144 64 385 minecraft:stone_bricks
setblock 144 65 385 theurgy:incubator_salt_vessel
setblock 146 64 385 minecraft:stone_bricks
setblock 146 65 385 theurgy:incubator_sulfur_vessel
setblock 145 64 384 minecraft:stone_bricks
setblock 145 65 384 theurgy:incubator_mercury_vessel
setblock 151 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.4"}','{"text": "theurgy"}','{"text": "array"}','{"text": ""}']}}
setblock 152 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell drei"}','{"text": "Pedestale auf"}','{"text": ""}','{"text": ""}']}}
fill 160 64 380 160 79 393 minecraft:light_gray_concrete
setblock 153 64 385 theurgy:reformation_source_pedestal
setblock 155 64 384 theurgy:reformation_target_pedestal
setblock 157 64 385 theurgy:reformation_result_pedestal
setblock 155 64 387 minecraft:stone_bricks
setblock 155 65 387 theurgy:sulfuric_flux_emitter[facing=up]
setblock 161 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.5"}','{"text": "theurgy"}','{"text": "fermentation"}','{"text": ""}']}}
setblock 162 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Vergär Sulfur"}','{"text": "zu Niter"}','{"text": ""}','{"text": ""}']}}
fill 170 64 380 170 79 393 minecraft:light_gray_concrete
setblock 165 64 385 theurgy:fermentation_vat[facing=south,has_output=false,open=true]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
