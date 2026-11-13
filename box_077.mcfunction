# 077 ars_master/charged_certus
#area 242 122 261 147
fill 242 64 122 261 91 147 minecraft:air
fill 242 60 122 261 62 147 minecraft:stone
fill 242 63 122 261 63 147 minecraft:light_gray_concrete
fill 246 64 128 261 79 128 minecraft:light_gray_concrete
fill 246 64 128 246 79 141 minecraft:light_gray_concrete
setblock 247 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077"}','{"text": "ars_master"}','{"text": "charged_certus"}','{"text": ""}']}}
setblock 248 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "redstone and"}','{"text": "glowstone"}','{"text": "pedestals"}']}}
fill 256 64 128 256 79 141 minecraft:light_gray_concrete
setblock 251 64 133 ars_nouveau:imbuement_chamber[facing=up]
setblock 250 64 133 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 250 64 133 south minecraft:redstone
setblock 252 64 133 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 252 64 133 south minecraft:glowstone_dust
kw testworld use 251 64 133 south ae2:certus_quartz_crystal
setblock 253 64 132 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
