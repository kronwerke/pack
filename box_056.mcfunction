# 056 mekanism_elite/fusion
#area 221 95 244 122
fill 221 64 95 244 93 122 minecraft:air
fill 221 60 95 244 62 122 minecraft:stone
fill 221 63 95 244 63 122 minecraft:light_gray_concrete
fill 225 64 101 244 81 101 minecraft:light_gray_concrete
fill 225 64 101 225 81 116 minecraft:light_gray_concrete
setblock 226 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "056"}','{"text": "mekanism_elite"}','{"text": "fusion"}','{"text": ""}']}}
setblock 227 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fusion reactor"}','{"text": "with laser and"}','{"text": "amplifier"}','{"text": ""}']}}
fill 239 64 101 239 81 116 minecraft:light_gray_concrete
setblock 228 64 107 mekanismgenerators:fusion_reactor_frame
setblock 228 65 106 mekanismgenerators:fusion_reactor_frame
setblock 228 65 107 mekanismgenerators:reactor_glass
setblock 228 65 108 mekanismgenerators:fusion_reactor_frame
setblock 228 66 105 mekanismgenerators:fusion_reactor_frame
setblock 228 66 106 mekanismgenerators:reactor_glass
setblock 228 66 107 mekanismgenerators:fusion_reactor_port[active=false]
setblock 228 66 108 mekanismgenerators:reactor_glass
setblock 228 66 109 mekanismgenerators:fusion_reactor_frame
setblock 228 67 106 mekanismgenerators:fusion_reactor_frame
setblock 228 67 107 mekanismgenerators:reactor_glass
setblock 228 67 108 mekanismgenerators:fusion_reactor_frame
setblock 228 68 107 mekanismgenerators:fusion_reactor_frame
setblock 229 64 106 mekanismgenerators:fusion_reactor_frame
setblock 229 64 107 mekanismgenerators:reactor_glass
setblock 229 64 108 mekanismgenerators:fusion_reactor_frame
setblock 229 65 105 mekanismgenerators:fusion_reactor_frame
setblock 229 65 109 mekanismgenerators:fusion_reactor_frame
setblock 229 66 105 mekanismgenerators:reactor_glass
setblock 229 66 109 mekanismgenerators:reactor_glass
setblock 229 67 105 mekanismgenerators:fusion_reactor_frame
setblock 229 67 109 mekanismgenerators:fusion_reactor_frame
setblock 229 68 106 mekanismgenerators:fusion_reactor_frame
setblock 229 68 107 mekanismgenerators:reactor_glass
setblock 229 68 108 mekanismgenerators:fusion_reactor_frame
setblock 230 64 105 mekanismgenerators:fusion_reactor_frame
setblock 230 64 106 mekanismgenerators:reactor_glass
setblock 230 64 107 mekanismgenerators:fusion_reactor_port[active=true]
setblock 230 64 108 mekanismgenerators:reactor_glass
setblock 230 64 109 mekanismgenerators:fusion_reactor_frame
setblock 230 65 105 mekanismgenerators:reactor_glass
setblock 230 65 109 mekanismgenerators:reactor_glass
setblock 230 66 105 mekanismgenerators:reactor_glass
setblock 230 66 109 mekanismgenerators:reactor_glass
setblock 230 67 105 mekanismgenerators:reactor_glass
setblock 230 67 109 mekanismgenerators:reactor_glass
setblock 230 68 105 mekanismgenerators:fusion_reactor_frame
setblock 230 68 106 mekanismgenerators:reactor_glass
setblock 230 68 107 mekanismgenerators:fusion_reactor_controller[active=false]
setblock 230 68 108 mekanismgenerators:reactor_glass
setblock 230 68 109 mekanismgenerators:fusion_reactor_frame
setblock 231 64 106 mekanismgenerators:fusion_reactor_frame
setblock 231 64 107 mekanismgenerators:reactor_glass
setblock 231 64 108 mekanismgenerators:fusion_reactor_frame
setblock 231 65 105 mekanismgenerators:fusion_reactor_frame
setblock 231 65 109 mekanismgenerators:fusion_reactor_frame
setblock 231 66 105 mekanismgenerators:reactor_glass
setblock 231 66 109 mekanismgenerators:reactor_glass
setblock 231 67 105 mekanismgenerators:fusion_reactor_frame
setblock 231 67 109 mekanismgenerators:fusion_reactor_frame
setblock 231 68 106 mekanismgenerators:fusion_reactor_frame
setblock 231 68 107 mekanismgenerators:reactor_glass
setblock 231 68 108 mekanismgenerators:fusion_reactor_frame
setblock 232 64 107 mekanismgenerators:fusion_reactor_frame
setblock 232 65 106 mekanismgenerators:fusion_reactor_frame
setblock 232 65 107 mekanismgenerators:reactor_glass
setblock 232 65 108 mekanismgenerators:fusion_reactor_frame
setblock 232 66 105 mekanismgenerators:fusion_reactor_frame
setblock 232 66 106 mekanismgenerators:reactor_glass
setblock 232 66 107 mekanismgenerators:laser_focus_matrix
setblock 232 66 108 mekanismgenerators:reactor_glass
setblock 232 66 109 mekanismgenerators:fusion_reactor_frame
setblock 232 67 106 mekanismgenerators:fusion_reactor_frame
setblock 232 67 107 mekanismgenerators:reactor_glass
setblock 232 67 108 mekanismgenerators:fusion_reactor_frame
setblock 232 68 107 mekanismgenerators:fusion_reactor_frame
fill 234 64 107 234 65 107 mekanism:steel_casing
setblock 234 66 107 mekanism:laser_amplifier[facing=west]
fill 236 64 107 236 65 107 mekanism:steel_casing
setblock 236 66 107 mekanism:laser[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
