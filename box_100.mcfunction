# 100 industrial/extractor, latex_unit
#area -4 214 25 239
fill -4 64 214 25 91 239 minecraft:air
fill -4 60 214 25 62 239 minecraft:stone
fill -4 63 214 25 63 239 minecraft:light_gray_concrete
fill 0 64 220 25 79 220 minecraft:light_gray_concrete
fill 0 64 220 0 79 233 minecraft:light_gray_concrete
setblock 1 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.1"}','{"text": "industrial"}','{"text": "extractor"}','{"text": ""}']}}
setblock 2 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pity frame"}','{"text": "recipe,"}','{"text": "extractors"}','{"text": "around a log"}']}}
setblock 3 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "column, the"}','{"text": "latex unit GUI,"}','{"text": "dry rubber in a"}','{"text": "furnace, the"}']}}
setblock 4 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dissolution"}','{"text": "chamber GUI"}','{"text": ""}','{"text": ""}']}}
fill 10 64 220 10 79 233 minecraft:light_gray_concrete
fill 5 64 225 5 67 225 minecraft:acacia_log[axis=y]
setblock 4 64 225 industrialforegoing:fluid_extractor[subfacing=east]
setblock 6 64 225 industrialforegoing:fluid_extractor[subfacing=west]
setblock 4 65 225 industrialforegoing:fluid_extractor[subfacing=east]
setblock 6 65 225 industrialforegoing:fluid_extractor[subfacing=west]
setblock 11 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.2"}','{"text": "industrial"}','{"text": "latex_unit"}','{"text": ""}']}}
setblock 12 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Latexverarbeitungsmaschine"}','{"text": ""}','{"text": ""}']}}
fill 20 64 220 20 79 233 minecraft:light_gray_concrete
setblock 14 64 225 industrialforegoing:latex_processing_unit[subfacing=south]
setblock 16 64 225 industrialforegoing:dissolution_chamber[subfacing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
