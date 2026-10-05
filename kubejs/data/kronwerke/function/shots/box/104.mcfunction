# 104 ars_master/golem_bookwyrm
fill 322 63 130 333 63 143 minecraft:light_gray_concrete
fill 322 64 130 333 71 130 minecraft:light_gray_concrete
fill 322 64 130 322 71 143 minecraft:light_gray_concrete
setblock 323 64 142 minecraft:air
setblock 323 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "104"}','{"text": "ars_master"}','{"text": "golem_bookwyrm"}','{"text": ""}']}}
setblock 324 64 142 minecraft:air
setblock 324 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "amethyst golem"}','{"text": "at a geode,"}','{"text": "storage lectern"}','{"text": "GUI"}']}}
fill 324 64 132 326 66 134 minecraft:amethyst_block
setblock 325 67 133 minecraft:budding_amethyst
summon ars_nouveau:amethyst_golem 327.5 64 135.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 330 64 135 ars_nouveau:storage_lectern
