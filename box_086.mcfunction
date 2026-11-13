# 086 flux_networks/dust
#area 65 250 84 275
fill 65 64 250 84 91 275 minecraft:air
fill 65 60 250 84 62 275 minecraft:stone
fill 65 63 250 84 63 275 minecraft:light_gray_concrete
fill 69 64 256 84 79 256 minecraft:light_gray_concrete
fill 69 64 256 69 79 269 minecraft:light_gray_concrete
setblock 70 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 71 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 72 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 79 64 256 79 79 269 minecraft:light_gray_concrete
setblock 74 64 261 minecraft:bedrock
summon item 74.5 65.1 261.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 74 66 261 minecraft:obsidian
