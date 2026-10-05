# 026 create/alloy_mixing
fill 102 63 48 117 63 61 minecraft:light_gray_concrete
fill 102 64 48 117 71 48 minecraft:light_gray_concrete
fill 102 64 48 102 71 61 minecraft:light_gray_concrete
setblock 103 64 60 minecraft:air
setblock 103 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "026"}','{"text": "create"}','{"text": "alloy_mixing"}','{"text": ""}']}}
setblock 104 64 60 minecraft:air
setblock 104 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the whole"}','{"text": "andesite alloy"}','{"text": "line with"}','{"text": "belts, funnels,"}']}}
setblock 105 64 60 minecraft:air
setblock 105 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mixer and"}','{"text": "output chest"}','{"text": "Andesitlegierung:"}','{"text": "Andesit und"}']}}
setblock 106 64 60 minecraft:air
setblock 106 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Eisennugget ins"}','{"text": "Becken"}','{"text": ""}','{"text": ""}']}}
place template create:gametest/processing/brass_mixing 104 64 50 none
setblock 115 64 57 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:andesite",count:64},{Slot:1b,id:"minecraft:iron_nugget",count:64}]}
