# 086 flux_networks/dust
#area 87 250 106 275
fill 87 64 250 106 91 275 minecraft:air
fill 87 60 250 106 62 275 minecraft:stone
fill 87 63 250 106 63 275 minecraft:light_gray_concrete
fill 91 64 256 106 79 256 minecraft:light_gray_concrete
fill 91 64 256 91 79 269 minecraft:light_gray_concrete
setblock 92 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 93 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 94 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 101 64 256 101 79 269 minecraft:light_gray_concrete
setblock 96 64 261 minecraft:bedrock
summon item 96.5 65.1 261.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 96 66 261 minecraft:obsidian
