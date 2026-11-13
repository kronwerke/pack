# 063 ars_master/charged_certus
#area 240 88 259 113
fill 240 64 88 259 91 113 minecraft:air
fill 240 60 88 259 62 113 minecraft:stone
fill 240 63 88 259 63 113 minecraft:light_gray_concrete
fill 244 64 94 259 79 94 minecraft:light_gray_concrete
fill 244 64 94 244 79 107 minecraft:light_gray_concrete
setblock 245 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "ars_master"}','{"text": "charged_certus"}','{"text": ""}']}}
setblock 246 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "redstone and"}','{"text": "glowstone"}','{"text": "pedestals"}']}}
fill 254 64 94 254 79 107 minecraft:light_gray_concrete
setblock 249 64 99 ars_nouveau:imbuement_chamber[facing=up]
setblock 248 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 248 64 99 south minecraft:redstone
setblock 250 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 250 64 99 south minecraft:glowstone_dust
kw testworld use 249 64 99 south ae2:certus_quartz_crystal
setblock 251 64 98 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
