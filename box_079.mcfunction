# 079 ars_master/charged_certus
#area 257 124 276 149
fill 257 64 124 276 91 149 minecraft:air
fill 257 60 124 276 62 149 minecraft:stone
fill 257 63 124 276 63 149 minecraft:light_gray_concrete
fill 261 64 130 276 79 130 minecraft:light_gray_concrete
fill 261 64 130 261 79 143 minecraft:light_gray_concrete
setblock 262 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "ars_master"}','{"text": "charged_certus"}','{"text": ""}']}}
setblock 263 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "redstone and"}','{"text": "glowstone"}','{"text": "pedestals"}']}}
fill 271 64 130 271 79 143 minecraft:light_gray_concrete
setblock 266 64 135 ars_nouveau:imbuement_chamber[facing=up]
setblock 265 64 135 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 265 64 135 south minecraft:redstone
setblock 267 64 135 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 267 64 135 south minecraft:glowstone_dust
kw testworld use 266 64 135 south ae2:certus_quartz_crystal
setblock 268 64 134 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
