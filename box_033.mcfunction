# 033 mekanism_elite/fusion
#area 173 63 196 90
fill 173 64 63 196 93 90 minecraft:air
fill 173 60 63 196 62 90 minecraft:stone
fill 173 63 63 196 63 90 minecraft:light_gray_concrete
fill 177 64 69 196 81 69 minecraft:light_gray_concrete
fill 177 64 69 177 81 84 minecraft:light_gray_concrete
setblock 178 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "033"}','{"text": "mekanism_elite"}','{"text": "fusion"}','{"text": ""}']}}
setblock 179 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fusion reactor"}','{"text": "with laser and"}','{"text": "amplifier"}','{"text": ""}']}}
fill 191 64 69 191 81 84 minecraft:light_gray_concrete
setblock 180 64 75 mekanismgenerators:fusion_reactor_frame
setblock 180 65 74 mekanismgenerators:fusion_reactor_frame
setblock 180 65 75 mekanismgenerators:reactor_glass
setblock 180 65 76 mekanismgenerators:fusion_reactor_frame
setblock 180 66 73 mekanismgenerators:fusion_reactor_frame
setblock 180 66 74 mekanismgenerators:reactor_glass
setblock 180 66 75 mekanismgenerators:fusion_reactor_port[active=false]
setblock 180 66 76 mekanismgenerators:reactor_glass
setblock 180 66 77 mekanismgenerators:fusion_reactor_frame
setblock 180 67 74 mekanismgenerators:fusion_reactor_frame
setblock 180 67 75 mekanismgenerators:reactor_glass
setblock 180 67 76 mekanismgenerators:fusion_reactor_frame
setblock 180 68 75 mekanismgenerators:fusion_reactor_frame
setblock 181 64 74 mekanismgenerators:fusion_reactor_frame
setblock 181 64 75 mekanismgenerators:reactor_glass
setblock 181 64 76 mekanismgenerators:fusion_reactor_frame
setblock 181 65 73 mekanismgenerators:fusion_reactor_frame
setblock 181 65 77 mekanismgenerators:fusion_reactor_frame
setblock 181 66 73 mekanismgenerators:reactor_glass
setblock 181 66 77 mekanismgenerators:reactor_glass
setblock 181 67 73 mekanismgenerators:fusion_reactor_frame
setblock 181 67 77 mekanismgenerators:fusion_reactor_frame
setblock 181 68 74 mekanismgenerators:fusion_reactor_frame
setblock 181 68 75 mekanismgenerators:reactor_glass
setblock 181 68 76 mekanismgenerators:fusion_reactor_frame
setblock 182 64 73 mekanismgenerators:fusion_reactor_frame
setblock 182 64 74 mekanismgenerators:reactor_glass
setblock 182 64 75 mekanismgenerators:fusion_reactor_port[active=true]
setblock 182 64 76 mekanismgenerators:reactor_glass
setblock 182 64 77 mekanismgenerators:fusion_reactor_frame
setblock 182 65 73 mekanismgenerators:reactor_glass
setblock 182 65 77 mekanismgenerators:reactor_glass
setblock 182 66 73 mekanismgenerators:reactor_glass
setblock 182 66 77 mekanismgenerators:reactor_glass
setblock 182 67 73 mekanismgenerators:reactor_glass
setblock 182 67 77 mekanismgenerators:reactor_glass
setblock 182 68 73 mekanismgenerators:fusion_reactor_frame
setblock 182 68 74 mekanismgenerators:reactor_glass
setblock 182 68 75 mekanismgenerators:fusion_reactor_controller[active=false]
setblock 182 68 76 mekanismgenerators:reactor_glass
setblock 182 68 77 mekanismgenerators:fusion_reactor_frame
setblock 183 64 74 mekanismgenerators:fusion_reactor_frame
setblock 183 64 75 mekanismgenerators:reactor_glass
setblock 183 64 76 mekanismgenerators:fusion_reactor_frame
setblock 183 65 73 mekanismgenerators:fusion_reactor_frame
setblock 183 65 77 mekanismgenerators:fusion_reactor_frame
setblock 183 66 73 mekanismgenerators:reactor_glass
setblock 183 66 77 mekanismgenerators:reactor_glass
setblock 183 67 73 mekanismgenerators:fusion_reactor_frame
setblock 183 67 77 mekanismgenerators:fusion_reactor_frame
setblock 183 68 74 mekanismgenerators:fusion_reactor_frame
setblock 183 68 75 mekanismgenerators:reactor_glass
setblock 183 68 76 mekanismgenerators:fusion_reactor_frame
setblock 184 64 75 mekanismgenerators:fusion_reactor_frame
setblock 184 65 74 mekanismgenerators:fusion_reactor_frame
setblock 184 65 75 mekanismgenerators:reactor_glass
setblock 184 65 76 mekanismgenerators:fusion_reactor_frame
setblock 184 66 73 mekanismgenerators:fusion_reactor_frame
setblock 184 66 74 mekanismgenerators:reactor_glass
setblock 184 66 75 mekanismgenerators:laser_focus_matrix
setblock 184 66 76 mekanismgenerators:reactor_glass
setblock 184 66 77 mekanismgenerators:fusion_reactor_frame
setblock 184 67 74 mekanismgenerators:fusion_reactor_frame
setblock 184 67 75 mekanismgenerators:reactor_glass
setblock 184 67 76 mekanismgenerators:fusion_reactor_frame
setblock 184 68 75 mekanismgenerators:fusion_reactor_frame
fill 186 64 75 186 65 75 mekanism:steel_casing
setblock 186 66 75 mekanism:laser_amplifier[facing=west]
fill 188 64 75 188 65 75 mekanism:steel_casing
setblock 188 66 75 mekanism:laser[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
