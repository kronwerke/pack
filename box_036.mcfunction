# 036 mekanism_elite/fusion
#area 173 65 196 92
fill 173 64 65 196 93 92 minecraft:air
fill 173 60 65 196 62 92 minecraft:stone
fill 173 63 65 196 63 92 minecraft:light_gray_concrete
fill 177 64 71 196 81 71 minecraft:light_gray_concrete
fill 177 64 71 177 81 86 minecraft:light_gray_concrete
setblock 178 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "036"}','{"text": "mekanism_elite"}','{"text": "fusion"}','{"text": ""}']}}
setblock 179 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fusion reactor"}','{"text": "with laser and"}','{"text": "amplifier"}','{"text": ""}']}}
fill 191 64 71 191 81 86 minecraft:light_gray_concrete
setblock 180 64 77 mekanismgenerators:fusion_reactor_frame
setblock 180 65 76 mekanismgenerators:fusion_reactor_frame
setblock 180 65 77 mekanismgenerators:reactor_glass
setblock 180 65 78 mekanismgenerators:fusion_reactor_frame
setblock 180 66 75 mekanismgenerators:fusion_reactor_frame
setblock 180 66 76 mekanismgenerators:reactor_glass
setblock 180 66 77 mekanismgenerators:fusion_reactor_port[active=false]
setblock 180 66 78 mekanismgenerators:reactor_glass
setblock 180 66 79 mekanismgenerators:fusion_reactor_frame
setblock 180 67 76 mekanismgenerators:fusion_reactor_frame
setblock 180 67 77 mekanismgenerators:reactor_glass
setblock 180 67 78 mekanismgenerators:fusion_reactor_frame
setblock 180 68 77 mekanismgenerators:fusion_reactor_frame
setblock 181 64 76 mekanismgenerators:fusion_reactor_frame
setblock 181 64 77 mekanismgenerators:reactor_glass
setblock 181 64 78 mekanismgenerators:fusion_reactor_frame
setblock 181 65 75 mekanismgenerators:fusion_reactor_frame
setblock 181 65 79 mekanismgenerators:fusion_reactor_frame
setblock 181 66 75 mekanismgenerators:reactor_glass
setblock 181 66 79 mekanismgenerators:reactor_glass
setblock 181 67 75 mekanismgenerators:fusion_reactor_frame
setblock 181 67 79 mekanismgenerators:fusion_reactor_frame
setblock 181 68 76 mekanismgenerators:fusion_reactor_frame
setblock 181 68 77 mekanismgenerators:reactor_glass
setblock 181 68 78 mekanismgenerators:fusion_reactor_frame
setblock 182 64 75 mekanismgenerators:fusion_reactor_frame
setblock 182 64 76 mekanismgenerators:reactor_glass
setblock 182 64 77 mekanismgenerators:fusion_reactor_port[active=true]
setblock 182 64 78 mekanismgenerators:reactor_glass
setblock 182 64 79 mekanismgenerators:fusion_reactor_frame
setblock 182 65 75 mekanismgenerators:reactor_glass
setblock 182 65 79 mekanismgenerators:reactor_glass
setblock 182 66 75 mekanismgenerators:reactor_glass
setblock 182 66 79 mekanismgenerators:reactor_glass
setblock 182 67 75 mekanismgenerators:reactor_glass
setblock 182 67 79 mekanismgenerators:reactor_glass
setblock 182 68 75 mekanismgenerators:fusion_reactor_frame
setblock 182 68 76 mekanismgenerators:reactor_glass
setblock 182 68 77 mekanismgenerators:fusion_reactor_controller[active=false]
setblock 182 68 78 mekanismgenerators:reactor_glass
setblock 182 68 79 mekanismgenerators:fusion_reactor_frame
setblock 183 64 76 mekanismgenerators:fusion_reactor_frame
setblock 183 64 77 mekanismgenerators:reactor_glass
setblock 183 64 78 mekanismgenerators:fusion_reactor_frame
setblock 183 65 75 mekanismgenerators:fusion_reactor_frame
setblock 183 65 79 mekanismgenerators:fusion_reactor_frame
setblock 183 66 75 mekanismgenerators:reactor_glass
setblock 183 66 79 mekanismgenerators:reactor_glass
setblock 183 67 75 mekanismgenerators:fusion_reactor_frame
setblock 183 67 79 mekanismgenerators:fusion_reactor_frame
setblock 183 68 76 mekanismgenerators:fusion_reactor_frame
setblock 183 68 77 mekanismgenerators:reactor_glass
setblock 183 68 78 mekanismgenerators:fusion_reactor_frame
setblock 184 64 77 mekanismgenerators:fusion_reactor_frame
setblock 184 65 76 mekanismgenerators:fusion_reactor_frame
setblock 184 65 77 mekanismgenerators:reactor_glass
setblock 184 65 78 mekanismgenerators:fusion_reactor_frame
setblock 184 66 75 mekanismgenerators:fusion_reactor_frame
setblock 184 66 76 mekanismgenerators:reactor_glass
setblock 184 66 77 mekanismgenerators:laser_focus_matrix
setblock 184 66 78 mekanismgenerators:reactor_glass
setblock 184 66 79 mekanismgenerators:fusion_reactor_frame
setblock 184 67 76 mekanismgenerators:fusion_reactor_frame
setblock 184 67 77 mekanismgenerators:reactor_glass
setblock 184 67 78 mekanismgenerators:fusion_reactor_frame
setblock 184 68 77 mekanismgenerators:fusion_reactor_frame
fill 186 64 77 186 65 77 mekanism:steel_casing
setblock 186 66 77 mekanism:laser_amplifier[facing=west]
fill 188 64 77 188 65 77 mekanism:steel_casing
setblock 188 66 77 mekanism:laser[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
