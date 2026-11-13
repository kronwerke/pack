# 128 industrial/extractor, latex_unit
#area -4 250 25 275
fill -4 64 250 25 91 275 minecraft:air
fill -4 60 250 25 62 275 minecraft:stone
fill -4 63 250 25 63 275 minecraft:light_gray_concrete
fill 0 64 256 25 79 256 minecraft:light_gray_concrete
fill 0 64 256 0 79 269 minecraft:light_gray_concrete
setblock 1 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128.1"}','{"text": "industrial"}','{"text": "extractor"}','{"text": ""}']}}
setblock 2 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pity frame"}','{"text": "recipe,"}','{"text": "extractors"}','{"text": "around a log"}']}}
setblock 3 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "column, the"}','{"text": "latex unit GUI,"}','{"text": "dry rubber in a"}','{"text": "furnace, the"}']}}
setblock 4 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dissolution"}','{"text": "chamber GUI"}','{"text": ""}','{"text": ""}']}}
fill 10 64 256 10 79 269 minecraft:light_gray_concrete
fill 5 64 261 5 67 261 minecraft:acacia_log[axis=y]
setblock 4 64 261 industrialforegoing:fluid_extractor[subfacing=east]
setblock 6 64 261 industrialforegoing:fluid_extractor[subfacing=west]
setblock 4 65 261 industrialforegoing:fluid_extractor[subfacing=east]
setblock 6 65 261 industrialforegoing:fluid_extractor[subfacing=west]
setblock 11 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128.2"}','{"text": "industrial"}','{"text": "latex_unit"}','{"text": ""}']}}
setblock 12 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Latexverarbeitungsmaschine"}','{"text": ""}','{"text": ""}']}}
fill 20 64 256 20 79 269 minecraft:light_gray_concrete
setblock 14 64 261 industrialforegoing:latex_processing_unit[subfacing=south]
setblock 16 64 261 industrialforegoing:dissolution_chamber[subfacing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
