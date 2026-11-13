# 044 mekanism_elite/fusion
#area 191 65 214 92
fill 191 64 65 214 93 92 minecraft:air
fill 191 60 65 214 62 92 minecraft:stone
fill 191 63 65 214 63 92 minecraft:light_gray_concrete
fill 195 64 71 214 81 71 minecraft:light_gray_concrete
fill 195 64 71 195 81 86 minecraft:light_gray_concrete
setblock 196 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044"}','{"text": "mekanism_elite"}','{"text": "fusion"}','{"text": ""}']}}
setblock 197 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fusion reactor"}','{"text": "with laser and"}','{"text": "amplifier"}','{"text": ""}']}}
fill 209 64 71 209 81 86 minecraft:light_gray_concrete
setblock 198 64 77 mekanismgenerators:fusion_reactor_frame
setblock 198 65 76 mekanismgenerators:fusion_reactor_frame
setblock 198 65 77 mekanismgenerators:reactor_glass
setblock 198 65 78 mekanismgenerators:fusion_reactor_frame
setblock 198 66 75 mekanismgenerators:fusion_reactor_frame
setblock 198 66 76 mekanismgenerators:reactor_glass
setblock 198 66 77 mekanismgenerators:fusion_reactor_port[active=false]
setblock 198 66 78 mekanismgenerators:reactor_glass
setblock 198 66 79 mekanismgenerators:fusion_reactor_frame
setblock 198 67 76 mekanismgenerators:fusion_reactor_frame
setblock 198 67 77 mekanismgenerators:reactor_glass
setblock 198 67 78 mekanismgenerators:fusion_reactor_frame
setblock 198 68 77 mekanismgenerators:fusion_reactor_frame
setblock 199 64 76 mekanismgenerators:fusion_reactor_frame
setblock 199 64 77 mekanismgenerators:reactor_glass
setblock 199 64 78 mekanismgenerators:fusion_reactor_frame
setblock 199 65 75 mekanismgenerators:fusion_reactor_frame
setblock 199 65 79 mekanismgenerators:fusion_reactor_frame
setblock 199 66 75 mekanismgenerators:reactor_glass
setblock 199 66 79 mekanismgenerators:reactor_glass
setblock 199 67 75 mekanismgenerators:fusion_reactor_frame
setblock 199 67 79 mekanismgenerators:fusion_reactor_frame
setblock 199 68 76 mekanismgenerators:fusion_reactor_frame
setblock 199 68 77 mekanismgenerators:reactor_glass
setblock 199 68 78 mekanismgenerators:fusion_reactor_frame
setblock 200 64 75 mekanismgenerators:fusion_reactor_frame
setblock 200 64 76 mekanismgenerators:reactor_glass
setblock 200 64 77 mekanismgenerators:fusion_reactor_port[active=true]
setblock 200 64 78 mekanismgenerators:reactor_glass
setblock 200 64 79 mekanismgenerators:fusion_reactor_frame
setblock 200 65 75 mekanismgenerators:reactor_glass
setblock 200 65 79 mekanismgenerators:reactor_glass
setblock 200 66 75 mekanismgenerators:reactor_glass
setblock 200 66 79 mekanismgenerators:reactor_glass
setblock 200 67 75 mekanismgenerators:reactor_glass
setblock 200 67 79 mekanismgenerators:reactor_glass
setblock 200 68 75 mekanismgenerators:fusion_reactor_frame
setblock 200 68 76 mekanismgenerators:reactor_glass
setblock 200 68 77 mekanismgenerators:fusion_reactor_controller[active=false]
setblock 200 68 78 mekanismgenerators:reactor_glass
setblock 200 68 79 mekanismgenerators:fusion_reactor_frame
setblock 201 64 76 mekanismgenerators:fusion_reactor_frame
setblock 201 64 77 mekanismgenerators:reactor_glass
setblock 201 64 78 mekanismgenerators:fusion_reactor_frame
setblock 201 65 75 mekanismgenerators:fusion_reactor_frame
setblock 201 65 79 mekanismgenerators:fusion_reactor_frame
setblock 201 66 75 mekanismgenerators:reactor_glass
setblock 201 66 79 mekanismgenerators:reactor_glass
setblock 201 67 75 mekanismgenerators:fusion_reactor_frame
setblock 201 67 79 mekanismgenerators:fusion_reactor_frame
setblock 201 68 76 mekanismgenerators:fusion_reactor_frame
setblock 201 68 77 mekanismgenerators:reactor_glass
setblock 201 68 78 mekanismgenerators:fusion_reactor_frame
setblock 202 64 77 mekanismgenerators:fusion_reactor_frame
setblock 202 65 76 mekanismgenerators:fusion_reactor_frame
setblock 202 65 77 mekanismgenerators:reactor_glass
setblock 202 65 78 mekanismgenerators:fusion_reactor_frame
setblock 202 66 75 mekanismgenerators:fusion_reactor_frame
setblock 202 66 76 mekanismgenerators:reactor_glass
setblock 202 66 77 mekanismgenerators:laser_focus_matrix
setblock 202 66 78 mekanismgenerators:reactor_glass
setblock 202 66 79 mekanismgenerators:fusion_reactor_frame
setblock 202 67 76 mekanismgenerators:fusion_reactor_frame
setblock 202 67 77 mekanismgenerators:reactor_glass
setblock 202 67 78 mekanismgenerators:fusion_reactor_frame
setblock 202 68 77 mekanismgenerators:fusion_reactor_frame
fill 204 64 77 204 65 77 mekanism:steel_casing
setblock 204 66 77 mekanism:laser_amplifier[facing=west]
fill 206 64 77 206 65 77 mekanism:steel_casing
setblock 206 66 77 mekanism:laser[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
