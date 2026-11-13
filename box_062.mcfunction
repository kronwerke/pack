# 062 mekanism_elite/fusion
#area 272 97 295 124
fill 272 64 97 295 93 124 minecraft:air
fill 272 60 97 295 62 124 minecraft:stone
fill 272 63 97 295 63 124 minecraft:light_gray_concrete
fill 276 64 103 295 81 103 minecraft:light_gray_concrete
fill 276 64 103 276 81 118 minecraft:light_gray_concrete
setblock 277 64 117 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "062"}','{"text": "mekanism_elite"}','{"text": "fusion"}','{"text": ""}']}}
setblock 278 64 117 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fusion reactor"}','{"text": "with laser and"}','{"text": "amplifier"}','{"text": ""}']}}
fill 290 64 103 290 81 118 minecraft:light_gray_concrete
setblock 279 64 109 mekanismgenerators:fusion_reactor_frame
setblock 279 65 108 mekanismgenerators:fusion_reactor_frame
setblock 279 65 109 mekanismgenerators:reactor_glass
setblock 279 65 110 mekanismgenerators:fusion_reactor_frame
setblock 279 66 107 mekanismgenerators:fusion_reactor_frame
setblock 279 66 108 mekanismgenerators:reactor_glass
setblock 279 66 109 mekanismgenerators:fusion_reactor_port[active=false]
setblock 279 66 110 mekanismgenerators:reactor_glass
setblock 279 66 111 mekanismgenerators:fusion_reactor_frame
setblock 279 67 108 mekanismgenerators:fusion_reactor_frame
setblock 279 67 109 mekanismgenerators:reactor_glass
setblock 279 67 110 mekanismgenerators:fusion_reactor_frame
setblock 279 68 109 mekanismgenerators:fusion_reactor_frame
setblock 280 64 108 mekanismgenerators:fusion_reactor_frame
setblock 280 64 109 mekanismgenerators:reactor_glass
setblock 280 64 110 mekanismgenerators:fusion_reactor_frame
setblock 280 65 107 mekanismgenerators:fusion_reactor_frame
setblock 280 65 111 mekanismgenerators:fusion_reactor_frame
setblock 280 66 107 mekanismgenerators:reactor_glass
setblock 280 66 111 mekanismgenerators:reactor_glass
setblock 280 67 107 mekanismgenerators:fusion_reactor_frame
setblock 280 67 111 mekanismgenerators:fusion_reactor_frame
setblock 280 68 108 mekanismgenerators:fusion_reactor_frame
setblock 280 68 109 mekanismgenerators:reactor_glass
setblock 280 68 110 mekanismgenerators:fusion_reactor_frame
setblock 281 64 107 mekanismgenerators:fusion_reactor_frame
setblock 281 64 108 mekanismgenerators:reactor_glass
setblock 281 64 109 mekanismgenerators:fusion_reactor_port[active=true]
setblock 281 64 110 mekanismgenerators:reactor_glass
setblock 281 64 111 mekanismgenerators:fusion_reactor_frame
setblock 281 65 107 mekanismgenerators:reactor_glass
setblock 281 65 111 mekanismgenerators:reactor_glass
setblock 281 66 107 mekanismgenerators:reactor_glass
setblock 281 66 111 mekanismgenerators:reactor_glass
setblock 281 67 107 mekanismgenerators:reactor_glass
setblock 281 67 111 mekanismgenerators:reactor_glass
setblock 281 68 107 mekanismgenerators:fusion_reactor_frame
setblock 281 68 108 mekanismgenerators:reactor_glass
setblock 281 68 109 mekanismgenerators:fusion_reactor_controller[active=false]
setblock 281 68 110 mekanismgenerators:reactor_glass
setblock 281 68 111 mekanismgenerators:fusion_reactor_frame
setblock 282 64 108 mekanismgenerators:fusion_reactor_frame
setblock 282 64 109 mekanismgenerators:reactor_glass
setblock 282 64 110 mekanismgenerators:fusion_reactor_frame
setblock 282 65 107 mekanismgenerators:fusion_reactor_frame
setblock 282 65 111 mekanismgenerators:fusion_reactor_frame
setblock 282 66 107 mekanismgenerators:reactor_glass
setblock 282 66 111 mekanismgenerators:reactor_glass
setblock 282 67 107 mekanismgenerators:fusion_reactor_frame
setblock 282 67 111 mekanismgenerators:fusion_reactor_frame
setblock 282 68 108 mekanismgenerators:fusion_reactor_frame
setblock 282 68 109 mekanismgenerators:reactor_glass
setblock 282 68 110 mekanismgenerators:fusion_reactor_frame
setblock 283 64 109 mekanismgenerators:fusion_reactor_frame
setblock 283 65 108 mekanismgenerators:fusion_reactor_frame
setblock 283 65 109 mekanismgenerators:reactor_glass
setblock 283 65 110 mekanismgenerators:fusion_reactor_frame
setblock 283 66 107 mekanismgenerators:fusion_reactor_frame
setblock 283 66 108 mekanismgenerators:reactor_glass
setblock 283 66 109 mekanismgenerators:laser_focus_matrix
setblock 283 66 110 mekanismgenerators:reactor_glass
setblock 283 66 111 mekanismgenerators:fusion_reactor_frame
setblock 283 67 108 mekanismgenerators:fusion_reactor_frame
setblock 283 67 109 mekanismgenerators:reactor_glass
setblock 283 67 110 mekanismgenerators:fusion_reactor_frame
setblock 283 68 109 mekanismgenerators:fusion_reactor_frame
fill 285 64 109 285 65 109 mekanism:steel_casing
setblock 285 66 109 mekanism:laser_amplifier[facing=west]
fill 287 64 109 287 65 109 mekanism:steel_casing
setblock 287 66 109 mekanism:laser[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
