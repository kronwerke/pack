# 065 ars_master/charged_certus
#area 242 88 261 113
fill 242 64 88 261 91 113 minecraft:air
fill 242 60 88 261 62 113 minecraft:stone
fill 242 63 88 261 63 113 minecraft:light_gray_concrete
fill 246 64 94 261 79 94 minecraft:light_gray_concrete
fill 246 64 94 246 79 107 minecraft:light_gray_concrete
setblock 247 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "065"}','{"text": "ars_master"}','{"text": "charged_certus"}','{"text": ""}']}}
setblock 248 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "redstone and"}','{"text": "glowstone"}','{"text": "pedestals"}']}}
fill 256 64 94 256 79 107 minecraft:light_gray_concrete
setblock 251 64 99 ars_nouveau:imbuement_chamber[facing=up]
setblock 250 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 250 64 99 south minecraft:redstone
setblock 252 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 252 64 99 south minecraft:glowstone_dust
kw testworld use 251 64 99 south ae2:certus_quartz_crystal
setblock 253 64 98 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
