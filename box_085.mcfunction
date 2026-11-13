# 085 flux_networks/dust
#area 32 250 51 275
fill 32 64 250 51 91 275 minecraft:air
fill 32 60 250 51 62 275 minecraft:stone
fill 32 63 250 51 63 275 minecraft:light_gray_concrete
fill 36 64 256 51 79 256 minecraft:light_gray_concrete
fill 36 64 256 36 79 269 minecraft:light_gray_concrete
setblock 37 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 38 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 39 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 46 64 256 46 79 269 minecraft:light_gray_concrete
setblock 41 64 261 minecraft:bedrock
summon item 41.5 65.1 261.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 41 66 261 minecraft:obsidian
