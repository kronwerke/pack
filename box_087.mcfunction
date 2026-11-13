# 087 ars_master/charged_certus
#area 302 126 321 151
fill 302 64 126 321 91 151 minecraft:air
fill 302 60 126 321 62 151 minecraft:stone
fill 302 63 126 321 63 151 minecraft:light_gray_concrete
fill 306 64 132 321 79 132 minecraft:light_gray_concrete
fill 306 64 132 306 79 145 minecraft:light_gray_concrete
setblock 307 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087"}','{"text": "ars_master"}','{"text": "charged_certus"}','{"text": ""}']}}
setblock 308 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber with"}','{"text": "redstone and"}','{"text": "glowstone"}','{"text": "pedestals"}']}}
fill 316 64 132 316 79 145 minecraft:light_gray_concrete
setblock 311 64 137 ars_nouveau:imbuement_chamber[facing=up]
setblock 310 64 137 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 310 64 137 south minecraft:redstone
setblock 312 64 137 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 312 64 137 south minecraft:glowstone_dust
kw testworld use 311 64 137 south ae2:certus_quartz_crystal
setblock 313 64 136 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
