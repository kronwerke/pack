# 148 industrial/welcome, extractor, latex_unit, plastic
#area 200 242 249 267
fill 200 64 242 244 91 267 minecraft:air
fill 245 64 242 249 91 267 minecraft:air
fill 200 60 242 249 62 267 minecraft:stone
fill 200 63 242 249 63 267 minecraft:light_gray_concrete
fill 204 64 248 249 79 248 minecraft:light_gray_concrete
fill 204 64 248 204 79 261 minecraft:light_gray_concrete
setblock 205 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.1"}','{"text": "industrial"}','{"text": "welcome"}','{"text": ""}']}}
setblock 206 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pity frame"}','{"text": "recipe,"}','{"text": "extractors"}','{"text": "around a log"}']}}
setblock 207 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "column, the"}','{"text": "latex unit GUI,"}','{"text": "dry rubber in a"}','{"text": "furnace, the"}']}}
setblock 208 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dissolution"}','{"text": "chamber GUI"}','{"text": ""}','{"text": ""}']}}
fill 214 64 248 214 79 261 minecraft:light_gray_concrete
setblock 209 64 253 minecraft:smooth_stone_slab
summon item_display 209.5 65.4 253.5 {item:{id:"industrialforegoing:machine_frame_pity",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 215 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.2"}','{"text": "industrial"}','{"text": "extractor"}','{"text": ""}']}}
setblock 216 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitsextraktor"}','{"text": ""}','{"text": ""}']}}
fill 224 64 248 224 79 261 minecraft:light_gray_concrete
fill 219 64 253 219 67 253 minecraft:acacia_log[axis=y]
setblock 218 64 253 industrialforegoing:fluid_extractor[subfacing=east]
setblock 220 64 253 industrialforegoing:fluid_extractor[subfacing=west]
setblock 218 65 253 industrialforegoing:fluid_extractor[subfacing=east]
setblock 220 65 253 industrialforegoing:fluid_extractor[subfacing=west]
setblock 225 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.3"}','{"text": "industrial"}','{"text": "latex_unit"}','{"text": ""}']}}
setblock 226 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Latexverarbeitungsmaschine"}','{"text": ""}','{"text": ""}']}}
fill 234 64 248 234 79 261 minecraft:light_gray_concrete
setblock 228 64 253 industrialforegoing:latex_processing_unit[subfacing=south]
setblock 230 64 253 industrialforegoing:dissolution_chamber[subfacing=south]
setblock 235 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.4"}','{"text": "industrial"}','{"text": "plastic"}','{"text": ""}']}}
setblock 236 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmilz Gummi"}','{"text": "zu Kunststoff"}','{"text": ""}','{"text": ""}']}}
fill 244 64 248 244 79 261 minecraft:light_gray_concrete
setblock 238 64 253 minecraft:smooth_stone_slab
summon item_display 238.5 64.95 253.5 {item:{id:"industrialforegoing:dryrubber",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 240 64 253 minecraft:smooth_stone_slab
summon item_display 240.5 64.95 253.5 {item:{id:"industrialforegoing:plastic",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
