# 002 start_here/o_feeder
fill 17 63 6 30 63 21 minecraft:light_gray_concrete
fill 17 64 6 30 71 6 minecraft:light_gray_concrete
fill 17 64 6 17 71 21 minecraft:light_gray_concrete
setblock 18 64 20 minecraft:air
setblock 18 64 20 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "002"}','{"text": "start_here"}','{"text": "o_feeder"}','{"text": ""}']}}
setblock 19 64 20 minecraft:air
setblock 19 64 20 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a barrel next"}','{"text": "to the obelisk"}','{"text": "fed by a hopper"}','{"text": "or a belt"}']}}
fill 21 64 10 25 64 14 minecraft:polished_deepslate
setblock 23 65 12 kronwerke:obelisk
setblock 23 64 15 kronwerke:obelisk_intake
setblock 23 65 15 minecraft:hopper[facing=down]
setblock 23 66 15 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:cobblestone",count:64},{Slot:1b,id:"minecraft:cobblestone",count:64},{Slot:2b,id:"minecraft:cobblestone",count:64}]}
