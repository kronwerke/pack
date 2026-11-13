# 186 theurgy/sal_tank, liquefaction, vessels, wire, array, fermentation
#area 116 407 185 432
fill 116 64 407 160 91 432 minecraft:air
fill 161 64 407 185 91 432 minecraft:air
fill 116 60 407 185 62 432 minecraft:stone
fill 116 63 407 185 63 432 minecraft:light_gray_concrete
fill 120 64 413 185 79 413 minecraft:light_gray_concrete
fill 120 64 413 120 79 426 minecraft:light_gray_concrete
setblock 121 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.1"}','{"text": "theurgy"}','{"text": "sal_tank"}','{"text": ""}']}}
setblock 122 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell Tank und"}','{"text": "Akkumulator auf"}','{"text": ""}','{"text": ""}']}}
fill 130 64 413 130 79 426 minecraft:light_gray_concrete
setblock 125 64 418 theurgy:sal_ammoniac_tank
setblock 125 65 418 theurgy:sal_ammoniac_accumulator
setblock 131 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.2"}','{"text": "theurgy"}','{"text": "liquefaction"}','{"text": ""}']}}
setblock 132 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Löse Sulfur aus"}','{"text": "Raw Iron"}','{"text": ""}','{"text": ""}']}}
fill 140 64 413 140 79 426 minecraft:light_gray_concrete
setblock 135 64 418 theurgy:pyromantic_brazier[lit=true]
setblock 135 65 418 theurgy:liquefaction_cauldron[half=lower,lit=true]
setblock 135 66 418 theurgy:liquefaction_cauldron[half=upper,lit=true]
setblock 141 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.3"}','{"text": "theurgy"}','{"text": "vessels"}','{"text": ""}']}}
setblock 142 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die drei"}','{"text": "Gefäße auf"}','{"text": ""}','{"text": ""}']}}
fill 150 64 413 150 79 426 minecraft:light_gray_concrete
setblock 145 64 418 theurgy:pyromantic_brazier[lit=true]
setblock 145 65 418 theurgy:incubator[half=lower]
setblock 145 66 418 theurgy:incubator[half=upper]
setblock 144 64 418 minecraft:stone_bricks
setblock 144 65 418 theurgy:incubator_salt_vessel
setblock 146 64 418 minecraft:stone_bricks
setblock 146 65 418 theurgy:incubator_sulfur_vessel
setblock 145 64 417 minecraft:stone_bricks
setblock 145 65 417 theurgy:incubator_mercury_vessel
setblock 151 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.4"}','{"text": "theurgy"}','{"text": "wire"}','{"text": ""}']}}
setblock 152 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde sie"}','{"text": "mit Kupferdraht"}','{"text": ""}','{"text": ""}']}}
fill 160 64 413 160 79 426 minecraft:light_gray_concrete
setblock 155 64 418 minecraft:smooth_stone_slab
summon item_display 155.5 65.4 418.5 {item:{id:"theurgy:copper_wire",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 161 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.5"}','{"text": "theurgy"}','{"text": "array"}','{"text": ""}']}}
setblock 162 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell drei"}','{"text": "Pedestale auf"}','{"text": ""}','{"text": ""}']}}
fill 170 64 413 170 79 426 minecraft:light_gray_concrete
setblock 163 64 418 theurgy:reformation_source_pedestal
setblock 165 64 417 theurgy:reformation_target_pedestal
setblock 167 64 418 theurgy:reformation_result_pedestal
setblock 165 64 420 minecraft:stone_bricks
setblock 165 65 420 theurgy:sulfuric_flux_emitter[facing=up]
setblock 171 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.6"}','{"text": "theurgy"}','{"text": "fermentation"}','{"text": ""}']}}
setblock 172 64 425 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Vergär Sulfur"}','{"text": "zu Niter"}','{"text": ""}','{"text": ""}']}}
fill 180 64 413 180 79 426 minecraft:light_gray_concrete
setblock 175 64 418 theurgy:fermentation_vat[facing=south,has_output=false,open=true]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
