# 085 industrial/extractor, latex_unit
#area 361 177 390 202
fill 361 64 177 390 91 202 minecraft:air
fill 361 60 177 390 62 202 minecraft:stone
fill 361 63 177 390 63 202 minecraft:light_gray_concrete
fill 365 64 183 390 79 183 minecraft:light_gray_concrete
fill 365 64 183 365 79 196 minecraft:light_gray_concrete
setblock 366 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085.1"}','{"text": "industrial"}','{"text": "extractor"}','{"text": ""}']}}
setblock 367 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pity frame"}','{"text": "recipe,"}','{"text": "extractors"}','{"text": "around a log"}']}}
setblock 368 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "column, the"}','{"text": "latex unit GUI,"}','{"text": "dry rubber in a"}','{"text": "furnace, the"}']}}
setblock 369 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dissolution"}','{"text": "chamber GUI"}','{"text": ""}','{"text": ""}']}}
fill 375 64 183 375 79 196 minecraft:light_gray_concrete
fill 370 64 188 370 67 188 minecraft:acacia_log[axis=y]
setblock 369 64 188 industrialforegoing:fluid_extractor[subfacing=east]
setblock 371 64 188 industrialforegoing:fluid_extractor[subfacing=west]
setblock 369 65 188 industrialforegoing:fluid_extractor[subfacing=east]
setblock 371 65 188 industrialforegoing:fluid_extractor[subfacing=west]
setblock 376 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085.2"}','{"text": "industrial"}','{"text": "latex_unit"}','{"text": ""}']}}
setblock 377 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Latexverarbeitungsmaschine"}','{"text": ""}','{"text": ""}']}}
fill 385 64 183 385 79 196 minecraft:light_gray_concrete
setblock 379 64 188 industrialforegoing:latex_processing_unit[subfacing=south]
setblock 381 64 188 industrialforegoing:dissolution_chamber[subfacing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
