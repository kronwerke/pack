# 114 industrial/extractor, latex_unit
#area -4 216 25 241
fill -4 64 216 25 91 241 minecraft:air
fill -4 60 216 25 62 241 minecraft:stone
fill -4 63 216 25 63 241 minecraft:light_gray_concrete
fill 0 64 222 25 79 222 minecraft:light_gray_concrete
fill 0 64 222 0 79 235 minecraft:light_gray_concrete
setblock 1 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "114.1"}','{"text": "industrial"}','{"text": "extractor"}','{"text": ""}']}}
setblock 2 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pity frame"}','{"text": "recipe,"}','{"text": "extractors"}','{"text": "around a log"}']}}
setblock 3 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "column, the"}','{"text": "latex unit GUI,"}','{"text": "dry rubber in a"}','{"text": "furnace, the"}']}}
setblock 4 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dissolution"}','{"text": "chamber GUI"}','{"text": ""}','{"text": ""}']}}
fill 10 64 222 10 79 235 minecraft:light_gray_concrete
fill 5 64 227 5 67 227 minecraft:acacia_log[axis=y]
setblock 4 64 227 industrialforegoing:fluid_extractor[subfacing=east]
setblock 6 64 227 industrialforegoing:fluid_extractor[subfacing=west]
setblock 4 65 227 industrialforegoing:fluid_extractor[subfacing=east]
setblock 6 65 227 industrialforegoing:fluid_extractor[subfacing=west]
setblock 11 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "114.2"}','{"text": "industrial"}','{"text": "latex_unit"}','{"text": ""}']}}
setblock 12 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Latexverarbeitungsmaschine"}','{"text": ""}','{"text": ""}']}}
fill 20 64 222 20 79 235 minecraft:light_gray_concrete
setblock 14 64 227 industrialforegoing:latex_processing_unit[subfacing=south]
setblock 16 64 227 industrialforegoing:dissolution_chamber[subfacing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
