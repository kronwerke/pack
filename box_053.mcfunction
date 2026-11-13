# 053 mekanism_elite/fusion
#area 206 95 229 122
fill 206 64 95 229 93 122 minecraft:air
fill 206 60 95 229 62 122 minecraft:stone
fill 206 63 95 229 63 122 minecraft:light_gray_concrete
fill 210 64 101 229 81 101 minecraft:light_gray_concrete
fill 210 64 101 210 81 116 minecraft:light_gray_concrete
setblock 211 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "053"}','{"text": "mekanism_elite"}','{"text": "fusion"}','{"text": ""}']}}
setblock 212 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fusion reactor"}','{"text": "with laser and"}','{"text": "amplifier"}','{"text": ""}']}}
fill 224 64 101 224 81 116 minecraft:light_gray_concrete
setblock 213 64 107 mekanismgenerators:fusion_reactor_frame
setblock 213 65 106 mekanismgenerators:fusion_reactor_frame
setblock 213 65 107 mekanismgenerators:reactor_glass
setblock 213 65 108 mekanismgenerators:fusion_reactor_frame
setblock 213 66 105 mekanismgenerators:fusion_reactor_frame
setblock 213 66 106 mekanismgenerators:reactor_glass
setblock 213 66 107 mekanismgenerators:fusion_reactor_port[active=false]
setblock 213 66 108 mekanismgenerators:reactor_glass
setblock 213 66 109 mekanismgenerators:fusion_reactor_frame
setblock 213 67 106 mekanismgenerators:fusion_reactor_frame
setblock 213 67 107 mekanismgenerators:reactor_glass
setblock 213 67 108 mekanismgenerators:fusion_reactor_frame
setblock 213 68 107 mekanismgenerators:fusion_reactor_frame
setblock 214 64 106 mekanismgenerators:fusion_reactor_frame
setblock 214 64 107 mekanismgenerators:reactor_glass
setblock 214 64 108 mekanismgenerators:fusion_reactor_frame
setblock 214 65 105 mekanismgenerators:fusion_reactor_frame
setblock 214 65 109 mekanismgenerators:fusion_reactor_frame
setblock 214 66 105 mekanismgenerators:reactor_glass
setblock 214 66 109 mekanismgenerators:reactor_glass
setblock 214 67 105 mekanismgenerators:fusion_reactor_frame
setblock 214 67 109 mekanismgenerators:fusion_reactor_frame
setblock 214 68 106 mekanismgenerators:fusion_reactor_frame
setblock 214 68 107 mekanismgenerators:reactor_glass
setblock 214 68 108 mekanismgenerators:fusion_reactor_frame
setblock 215 64 105 mekanismgenerators:fusion_reactor_frame
setblock 215 64 106 mekanismgenerators:reactor_glass
setblock 215 64 107 mekanismgenerators:fusion_reactor_port[active=true]
setblock 215 64 108 mekanismgenerators:reactor_glass
setblock 215 64 109 mekanismgenerators:fusion_reactor_frame
setblock 215 65 105 mekanismgenerators:reactor_glass
setblock 215 65 109 mekanismgenerators:reactor_glass
setblock 215 66 105 mekanismgenerators:reactor_glass
setblock 215 66 109 mekanismgenerators:reactor_glass
setblock 215 67 105 mekanismgenerators:reactor_glass
setblock 215 67 109 mekanismgenerators:reactor_glass
setblock 215 68 105 mekanismgenerators:fusion_reactor_frame
setblock 215 68 106 mekanismgenerators:reactor_glass
setblock 215 68 107 mekanismgenerators:fusion_reactor_controller[active=false]
setblock 215 68 108 mekanismgenerators:reactor_glass
setblock 215 68 109 mekanismgenerators:fusion_reactor_frame
setblock 216 64 106 mekanismgenerators:fusion_reactor_frame
setblock 216 64 107 mekanismgenerators:reactor_glass
setblock 216 64 108 mekanismgenerators:fusion_reactor_frame
setblock 216 65 105 mekanismgenerators:fusion_reactor_frame
setblock 216 65 109 mekanismgenerators:fusion_reactor_frame
setblock 216 66 105 mekanismgenerators:reactor_glass
setblock 216 66 109 mekanismgenerators:reactor_glass
setblock 216 67 105 mekanismgenerators:fusion_reactor_frame
setblock 216 67 109 mekanismgenerators:fusion_reactor_frame
setblock 216 68 106 mekanismgenerators:fusion_reactor_frame
setblock 216 68 107 mekanismgenerators:reactor_glass
setblock 216 68 108 mekanismgenerators:fusion_reactor_frame
setblock 217 64 107 mekanismgenerators:fusion_reactor_frame
setblock 217 65 106 mekanismgenerators:fusion_reactor_frame
setblock 217 65 107 mekanismgenerators:reactor_glass
setblock 217 65 108 mekanismgenerators:fusion_reactor_frame
setblock 217 66 105 mekanismgenerators:fusion_reactor_frame
setblock 217 66 106 mekanismgenerators:reactor_glass
setblock 217 66 107 mekanismgenerators:laser_focus_matrix
setblock 217 66 108 mekanismgenerators:reactor_glass
setblock 217 66 109 mekanismgenerators:fusion_reactor_frame
setblock 217 67 106 mekanismgenerators:fusion_reactor_frame
setblock 217 67 107 mekanismgenerators:reactor_glass
setblock 217 67 108 mekanismgenerators:fusion_reactor_frame
setblock 217 68 107 mekanismgenerators:fusion_reactor_frame
fill 219 64 107 219 65 107 mekanism:steel_casing
setblock 219 66 107 mekanism:laser_amplifier[facing=west]
fill 221 64 107 221 65 107 mekanism:steel_casing
setblock 221 66 107 mekanism:laser[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
