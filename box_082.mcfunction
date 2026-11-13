# 082 flux_networks/dust
#area 32 231 51 256
fill 32 64 231 51 91 256 minecraft:air
fill 32 60 231 51 62 256 minecraft:stone
fill 32 63 231 51 63 256 minecraft:light_gray_concrete
fill 36 64 237 51 79 237 minecraft:light_gray_concrete
fill 36 64 237 36 79 250 minecraft:light_gray_concrete
setblock 37 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082"}','{"text": "flux_networks"}','{"text": "dust"}','{"text": ""}']}}
setblock 38 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the bedrock gap"}','{"text": "with redstone"}','{"text": "and obsidian,"}','{"text": "left-clicking"}']}}
setblock 39 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the obsidian"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 46 64 237 46 79 250 minecraft:light_gray_concrete
setblock 41 64 242 minecraft:bedrock
summon item 41.5 65.1 242.5 {Item:{id:"minecraft:redstone",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 41 66 242 minecraft:obsidian
