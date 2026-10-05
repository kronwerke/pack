# 036 create_brass/brass_mixing
fill 270 63 48 283 63 61 minecraft:light_gray_concrete
fill 270 64 48 283 71 48 minecraft:light_gray_concrete
fill 270 64 48 270 71 61 minecraft:light_gray_concrete
setblock 271 64 60 minecraft:air
setblock 271 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "036"}','{"text": "create_brass"}','{"text": "brass_mixing"}','{"text": ""}']}}
setblock 272 64 60 minecraft:air
setblock 272 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "heated burner,"}','{"text": "basin and mixer"}','{"text": "stack"}','{"text": ""}']}}
place template create:gametest/processing/brass_mixing_2 272 64 50 none
