# 062 ars_master/charged_certus
#area 225 88 244 113
fill 225 64 88 244 91 113 minecraft:air
fill 225 60 88 244 62 113 minecraft:stone
fill 225 63 88 244 63 113 minecraft:light_gray_concrete
fill 229 64 94 244 79 94 minecraft:light_gray_concrete
fill 229 64 94 229 79 107 minecraft:light_gray_concrete
setblock 230 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "062"}','{"text": "ars_master"}','{"text": "charged_certus"}','{"text": ""}']}}
setblock 231 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "redstone and"}','{"text": "glowstone"}','{"text": "pedestals"}']}}
fill 239 64 94 239 79 107 minecraft:light_gray_concrete
setblock 234 64 99 ars_nouveau:imbuement_chamber[facing=up]
setblock 233 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 233 64 99 south minecraft:redstone
setblock 235 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 235 64 99 south minecraft:glowstone_dust
kw testworld use 234 64 99 south ae2:certus_quartz_crystal
setblock 236 64 98 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
