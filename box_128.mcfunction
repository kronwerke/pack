# 128 industrial/extractor, latex_unit
#area -4 252 25 277
fill -4 64 252 25 91 277 minecraft:air
fill -4 60 252 25 62 277 minecraft:stone
fill -4 63 252 25 63 277 minecraft:light_gray_concrete
fill 0 64 258 25 79 258 minecraft:light_gray_concrete
fill 0 64 258 0 79 271 minecraft:light_gray_concrete
setblock 1 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128.1"}','{"text": "industrial"}','{"text": "extractor"}','{"text": ""}']}}
setblock 2 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pity frame"}','{"text": "recipe,"}','{"text": "extractors"}','{"text": "around a log"}']}}
setblock 3 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "column, the"}','{"text": "latex unit GUI,"}','{"text": "dry rubber in a"}','{"text": "furnace, the"}']}}
setblock 4 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dissolution"}','{"text": "chamber GUI"}','{"text": ""}','{"text": ""}']}}
fill 10 64 258 10 79 271 minecraft:light_gray_concrete
fill 5 64 263 5 67 263 minecraft:acacia_log[axis=y]
setblock 4 64 263 industrialforegoing:fluid_extractor[subfacing=east]
setblock 6 64 263 industrialforegoing:fluid_extractor[subfacing=west]
setblock 4 65 263 industrialforegoing:fluid_extractor[subfacing=east]
setblock 6 65 263 industrialforegoing:fluid_extractor[subfacing=west]
setblock 11 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128.2"}','{"text": "industrial"}','{"text": "latex_unit"}','{"text": ""}']}}
setblock 12 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Latexverarbeitungsmaschine"}','{"text": ""}','{"text": ""}']}}
fill 20 64 258 20 79 271 minecraft:light_gray_concrete
setblock 14 64 263 industrialforegoing:latex_processing_unit[subfacing=south]
setblock 16 64 263 industrialforegoing:dissolution_chamber[subfacing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
