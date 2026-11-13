# 179 draconic_chaos/reactor
#area 35 386 54 411
fill 35 64 386 54 91 411 minecraft:air
fill 35 60 386 54 62 411 minecraft:stone
fill 35 63 386 54 63 411 minecraft:light_gray_concrete
fill 39 64 392 54 79 392 minecraft:light_gray_concrete
fill 39 64 392 39 79 405 minecraft:light_gray_concrete
setblock 40 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "179"}','{"text": "draconic_chaos"}','{"text": "reactor"}','{"text": ""}']}}
setblock 41 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Drakonischen"}','{"text": "Reaktor"}','{"text": ""}']}}
fill 49 64 392 49 79 405 minecraft:light_gray_concrete
setblock 42 64 397 minecraft:smooth_stone_slab
summon item_display 42.5 64.95 397.5 {item:{id:"draconicevolution:reactor_stabilizer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 44 64 397 minecraft:smooth_stone_slab
summon item_display 44.5 64.95 397.5 {item:{id:"draconicevolution:reactor_core",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 46 64 397 minecraft:smooth_stone_slab
summon item_display 46.5 64.95 397.5 {item:{id:"draconicevolution:reactor_injector",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
