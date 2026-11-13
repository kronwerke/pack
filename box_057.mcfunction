# 057 ars_master/charged_certus
#area 195 88 214 113
fill 195 64 88 214 91 113 minecraft:air
fill 195 60 88 214 62 113 minecraft:stone
fill 195 63 88 214 63 113 minecraft:light_gray_concrete
fill 199 64 94 214 79 94 minecraft:light_gray_concrete
fill 199 64 94 199 79 107 minecraft:light_gray_concrete
setblock 200 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057"}','{"text": "ars_master"}','{"text": "charged_certus"}','{"text": ""}']}}
setblock 201 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "redstone and"}','{"text": "glowstone"}','{"text": "pedestals"}']}}
fill 209 64 94 209 79 107 minecraft:light_gray_concrete
setblock 204 64 99 ars_nouveau:imbuement_chamber[facing=up]
setblock 203 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 203 64 99 south minecraft:redstone
setblock 205 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 205 64 99 south minecraft:glowstone_dust
kw testworld use 204 64 99 south ae2:certus_quartz_crystal
setblock 206 64 98 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
