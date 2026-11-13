# 133 industrial/welcome, extractor, latex_unit, plastic
#area 200 240 249 265
fill 200 64 240 244 91 265 minecraft:air
fill 245 64 240 249 91 265 minecraft:air
fill 200 60 240 249 62 265 minecraft:stone
fill 200 63 240 249 63 265 minecraft:light_gray_concrete
fill 204 64 246 249 79 246 minecraft:light_gray_concrete
fill 204 64 246 204 79 259 minecraft:light_gray_concrete
setblock 205 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.1"}','{"text": "industrial"}','{"text": "welcome"}','{"text": ""}']}}
setblock 206 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pity frame"}','{"text": "recipe,"}','{"text": "extractors"}','{"text": "around a log"}']}}
setblock 207 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "column, the"}','{"text": "latex unit GUI,"}','{"text": "dry rubber in a"}','{"text": "furnace, the"}']}}
setblock 208 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dissolution"}','{"text": "chamber GUI"}','{"text": ""}','{"text": ""}']}}
fill 214 64 246 214 79 259 minecraft:light_gray_concrete
setblock 209 64 251 minecraft:smooth_stone_slab
summon item_display 209.5 65.4 251.5 {item:{id:"industrialforegoing:machine_frame_pity",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 215 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.2"}','{"text": "industrial"}','{"text": "extractor"}','{"text": ""}']}}
setblock 216 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitsextraktor"}','{"text": ""}','{"text": ""}']}}
fill 224 64 246 224 79 259 minecraft:light_gray_concrete
fill 219 64 251 219 67 251 minecraft:acacia_log[axis=y]
setblock 218 64 251 industrialforegoing:fluid_extractor[subfacing=east]
setblock 220 64 251 industrialforegoing:fluid_extractor[subfacing=west]
setblock 218 65 251 industrialforegoing:fluid_extractor[subfacing=east]
setblock 220 65 251 industrialforegoing:fluid_extractor[subfacing=west]
setblock 225 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.3"}','{"text": "industrial"}','{"text": "latex_unit"}','{"text": ""}']}}
setblock 226 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Latexverarbeitungsmaschine"}','{"text": ""}','{"text": ""}']}}
fill 234 64 246 234 79 259 minecraft:light_gray_concrete
setblock 228 64 251 industrialforegoing:latex_processing_unit[subfacing=south]
setblock 230 64 251 industrialforegoing:dissolution_chamber[subfacing=south]
setblock 235 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.4"}','{"text": "industrial"}','{"text": "plastic"}','{"text": ""}']}}
setblock 236 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmilz Gummi"}','{"text": "zu Kunststoff"}','{"text": ""}','{"text": ""}']}}
fill 244 64 246 244 79 259 minecraft:light_gray_concrete
setblock 238 64 251 minecraft:smooth_stone_slab
summon item_display 238.5 64.95 251.5 {item:{id:"industrialforegoing:dryrubber",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 240 64 251 minecraft:smooth_stone_slab
summon item_display 240.5 64.95 251.5 {item:{id:"industrialforegoing:plastic",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
