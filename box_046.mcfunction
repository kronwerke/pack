# 046 mekanism_elite/fusion
#area 206 65 229 92
fill 206 64 65 229 93 92 minecraft:air
fill 206 60 65 229 62 92 minecraft:stone
fill 206 63 65 229 63 92 minecraft:light_gray_concrete
fill 210 64 71 229 81 71 minecraft:light_gray_concrete
fill 210 64 71 210 81 86 minecraft:light_gray_concrete
setblock 211 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "046"}','{"text": "mekanism_elite"}','{"text": "fusion"}','{"text": ""}']}}
setblock 212 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fusion reactor"}','{"text": "with laser and"}','{"text": "amplifier"}','{"text": ""}']}}
fill 224 64 71 224 81 86 minecraft:light_gray_concrete
setblock 213 64 77 mekanismgenerators:fusion_reactor_frame
setblock 213 65 76 mekanismgenerators:fusion_reactor_frame
setblock 213 65 77 mekanismgenerators:reactor_glass
setblock 213 65 78 mekanismgenerators:fusion_reactor_frame
setblock 213 66 75 mekanismgenerators:fusion_reactor_frame
setblock 213 66 76 mekanismgenerators:reactor_glass
setblock 213 66 77 mekanismgenerators:fusion_reactor_port[active=false]
setblock 213 66 78 mekanismgenerators:reactor_glass
setblock 213 66 79 mekanismgenerators:fusion_reactor_frame
setblock 213 67 76 mekanismgenerators:fusion_reactor_frame
setblock 213 67 77 mekanismgenerators:reactor_glass
setblock 213 67 78 mekanismgenerators:fusion_reactor_frame
setblock 213 68 77 mekanismgenerators:fusion_reactor_frame
setblock 214 64 76 mekanismgenerators:fusion_reactor_frame
setblock 214 64 77 mekanismgenerators:reactor_glass
setblock 214 64 78 mekanismgenerators:fusion_reactor_frame
setblock 214 65 75 mekanismgenerators:fusion_reactor_frame
setblock 214 65 79 mekanismgenerators:fusion_reactor_frame
setblock 214 66 75 mekanismgenerators:reactor_glass
setblock 214 66 79 mekanismgenerators:reactor_glass
setblock 214 67 75 mekanismgenerators:fusion_reactor_frame
setblock 214 67 79 mekanismgenerators:fusion_reactor_frame
setblock 214 68 76 mekanismgenerators:fusion_reactor_frame
setblock 214 68 77 mekanismgenerators:reactor_glass
setblock 214 68 78 mekanismgenerators:fusion_reactor_frame
setblock 215 64 75 mekanismgenerators:fusion_reactor_frame
setblock 215 64 76 mekanismgenerators:reactor_glass
setblock 215 64 77 mekanismgenerators:fusion_reactor_port[active=true]
setblock 215 64 78 mekanismgenerators:reactor_glass
setblock 215 64 79 mekanismgenerators:fusion_reactor_frame
setblock 215 65 75 mekanismgenerators:reactor_glass
setblock 215 65 79 mekanismgenerators:reactor_glass
setblock 215 66 75 mekanismgenerators:reactor_glass
setblock 215 66 79 mekanismgenerators:reactor_glass
setblock 215 67 75 mekanismgenerators:reactor_glass
setblock 215 67 79 mekanismgenerators:reactor_glass
setblock 215 68 75 mekanismgenerators:fusion_reactor_frame
setblock 215 68 76 mekanismgenerators:reactor_glass
setblock 215 68 77 mekanismgenerators:fusion_reactor_controller[active=false]
setblock 215 68 78 mekanismgenerators:reactor_glass
setblock 215 68 79 mekanismgenerators:fusion_reactor_frame
setblock 216 64 76 mekanismgenerators:fusion_reactor_frame
setblock 216 64 77 mekanismgenerators:reactor_glass
setblock 216 64 78 mekanismgenerators:fusion_reactor_frame
setblock 216 65 75 mekanismgenerators:fusion_reactor_frame
setblock 216 65 79 mekanismgenerators:fusion_reactor_frame
setblock 216 66 75 mekanismgenerators:reactor_glass
setblock 216 66 79 mekanismgenerators:reactor_glass
setblock 216 67 75 mekanismgenerators:fusion_reactor_frame
setblock 216 67 79 mekanismgenerators:fusion_reactor_frame
setblock 216 68 76 mekanismgenerators:fusion_reactor_frame
setblock 216 68 77 mekanismgenerators:reactor_glass
setblock 216 68 78 mekanismgenerators:fusion_reactor_frame
setblock 217 64 77 mekanismgenerators:fusion_reactor_frame
setblock 217 65 76 mekanismgenerators:fusion_reactor_frame
setblock 217 65 77 mekanismgenerators:reactor_glass
setblock 217 65 78 mekanismgenerators:fusion_reactor_frame
setblock 217 66 75 mekanismgenerators:fusion_reactor_frame
setblock 217 66 76 mekanismgenerators:reactor_glass
setblock 217 66 77 mekanismgenerators:laser_focus_matrix
setblock 217 66 78 mekanismgenerators:reactor_glass
setblock 217 66 79 mekanismgenerators:fusion_reactor_frame
setblock 217 67 76 mekanismgenerators:fusion_reactor_frame
setblock 217 67 77 mekanismgenerators:reactor_glass
setblock 217 67 78 mekanismgenerators:fusion_reactor_frame
setblock 217 68 77 mekanismgenerators:fusion_reactor_frame
fill 219 64 77 219 65 77 mekanism:steel_casing
setblock 219 66 77 mekanism:laser_amplifier[facing=west]
fill 221 64 77 221 65 77 mekanism:steel_casing
setblock 221 66 77 mekanism:laser[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
