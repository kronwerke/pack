# 127 industrial/extractor, latex_unit
#area -4 246 25 271
fill -4 64 246 25 91 271 minecraft:air
fill -4 60 246 25 62 271 minecraft:stone
fill -4 63 246 25 63 271 minecraft:light_gray_concrete
fill 0 64 252 25 79 252 minecraft:light_gray_concrete
fill 0 64 252 0 79 265 minecraft:light_gray_concrete
setblock 1 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.1"}','{"text": "industrial"}','{"text": "extractor"}','{"text": ""}']}}
setblock 2 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pity frame"}','{"text": "recipe,"}','{"text": "extractors"}','{"text": "around a log"}']}}
setblock 3 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "column, the"}','{"text": "latex unit GUI,"}','{"text": "dry rubber in a"}','{"text": "furnace, the"}']}}
setblock 4 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dissolution"}','{"text": "chamber GUI"}','{"text": ""}','{"text": ""}']}}
fill 10 64 252 10 79 265 minecraft:light_gray_concrete
fill 5 64 257 5 67 257 minecraft:acacia_log[axis=y]
setblock 4 64 257 industrialforegoing:fluid_extractor[subfacing=east]
setblock 6 64 257 industrialforegoing:fluid_extractor[subfacing=west]
setblock 4 65 257 industrialforegoing:fluid_extractor[subfacing=east]
setblock 6 65 257 industrialforegoing:fluid_extractor[subfacing=west]
setblock 11 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.2"}','{"text": "industrial"}','{"text": "latex_unit"}','{"text": ""}']}}
setblock 12 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Latexverarbeitungsmaschine"}','{"text": ""}','{"text": ""}']}}
fill 20 64 252 20 79 265 minecraft:light_gray_concrete
setblock 14 64 257 industrialforegoing:latex_processing_unit[subfacing=south]
setblock 16 64 257 industrialforegoing:dissolution_chamber[subfacing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
