# 162 theurgy/sal_tank, liquefaction, vessels, array, fermentation
#area 116 376 175 401
fill 116 64 376 160 91 401 minecraft:air
fill 161 64 376 175 91 401 minecraft:air
fill 116 60 376 175 62 401 minecraft:stone
fill 116 63 376 175 63 401 minecraft:light_gray_concrete
fill 120 64 382 175 79 382 minecraft:light_gray_concrete
fill 120 64 382 120 79 395 minecraft:light_gray_concrete
setblock 121 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.1"}','{"text": "theurgy"}','{"text": "sal_tank"}','{"text": ""}']}}
setblock 122 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell Tank und"}','{"text": "Akkumulator auf"}','{"text": ""}','{"text": ""}']}}
fill 130 64 382 130 79 395 minecraft:light_gray_concrete
setblock 125 64 387 theurgy:sal_ammoniac_tank
setblock 125 65 387 theurgy:sal_ammoniac_accumulator
setblock 131 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.2"}','{"text": "theurgy"}','{"text": "liquefaction"}','{"text": ""}']}}
setblock 132 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Löse Sulfur aus"}','{"text": "Raw Iron"}','{"text": ""}','{"text": ""}']}}
fill 140 64 382 140 79 395 minecraft:light_gray_concrete
setblock 135 64 387 theurgy:pyromantic_brazier[lit=true]
setblock 135 65 387 theurgy:liquefaction_cauldron[half=lower,lit=true]
setblock 135 66 387 theurgy:liquefaction_cauldron[half=upper,lit=true]
setblock 141 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.3"}','{"text": "theurgy"}','{"text": "vessels"}','{"text": ""}']}}
setblock 142 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die drei"}','{"text": "Gefäße auf"}','{"text": ""}','{"text": ""}']}}
fill 150 64 382 150 79 395 minecraft:light_gray_concrete
setblock 145 64 387 theurgy:pyromantic_brazier[lit=true]
setblock 145 65 387 theurgy:incubator[half=lower]
setblock 145 66 387 theurgy:incubator[half=upper]
setblock 144 64 387 minecraft:stone_bricks
setblock 144 65 387 theurgy:incubator_salt_vessel
setblock 146 64 387 minecraft:stone_bricks
setblock 146 65 387 theurgy:incubator_sulfur_vessel
setblock 145 64 386 minecraft:stone_bricks
setblock 145 65 386 theurgy:incubator_mercury_vessel
setblock 151 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.4"}','{"text": "theurgy"}','{"text": "array"}','{"text": ""}']}}
setblock 152 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell drei"}','{"text": "Pedestale auf"}','{"text": ""}','{"text": ""}']}}
fill 160 64 382 160 79 395 minecraft:light_gray_concrete
setblock 153 64 387 theurgy:reformation_source_pedestal
setblock 155 64 386 theurgy:reformation_target_pedestal
setblock 157 64 387 theurgy:reformation_result_pedestal
setblock 155 64 389 minecraft:stone_bricks
setblock 155 65 389 theurgy:sulfuric_flux_emitter[facing=up]
setblock 161 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.5"}','{"text": "theurgy"}','{"text": "fermentation"}','{"text": ""}']}}
setblock 162 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Vergär Sulfur"}','{"text": "zu Niter"}','{"text": ""}','{"text": ""}']}}
fill 170 64 382 170 79 395 minecraft:light_gray_concrete
setblock 165 64 387 theurgy:fermentation_vat[facing=south,has_output=false,open=true]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
