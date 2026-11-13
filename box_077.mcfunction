# 077 ars_master/charged_certus
#area 242 118 261 143
fill 242 64 118 261 91 143 minecraft:air
fill 242 60 118 261 62 143 minecraft:stone
fill 242 63 118 261 63 143 minecraft:light_gray_concrete
fill 246 64 124 261 79 124 minecraft:light_gray_concrete
fill 246 64 124 246 79 137 minecraft:light_gray_concrete
setblock 247 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077"}','{"text": "ars_master"}','{"text": "charged_certus"}','{"text": ""}']}}
setblock 248 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "redstone and"}','{"text": "glowstone"}','{"text": "pedestals"}']}}
fill 256 64 124 256 79 137 minecraft:light_gray_concrete
setblock 251 64 129 ars_nouveau:imbuement_chamber[facing=up]
setblock 250 64 129 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 250 64 129 south minecraft:redstone
setblock 252 64 129 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 252 64 129 south minecraft:glowstone_dust
kw testworld use 251 64 129 south ae2:certus_quartz_crystal
setblock 253 64 128 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
