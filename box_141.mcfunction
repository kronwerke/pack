# 141 ae2/channels
#area -4 296 17 321
fill -4 64 296 17 91 321 minecraft:air
fill -4 60 296 17 62 321 minecraft:stone
fill -4 63 296 17 63 321 minecraft:light_gray_concrete
fill 0 64 302 17 79 302 minecraft:light_gray_concrete
fill 0 64 302 0 79 315 minecraft:light_gray_concrete
setblock 1 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "141"}','{"text": "ae2"}','{"text": "channels"}','{"text": ""}']}}
setblock 2 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "controller with"}','{"text": "dense cables"}','{"text": "branching into"}','{"text": "normal smart"}']}}
setblock 3 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables, channel"}','{"text": "stripes visible"}','{"text": ""}','{"text": ""}']}}
fill 12 64 302 12 79 315 minecraft:light_gray_concrete
setblock 3 63 307 ae2:creative_energy_cell
setblock 3 64 307 ae2:controller
kw testworld use 3 64 307 east ae2:fluix_covered_dense_cable
kw testworld use 3 64 307 east ae2:fluix_covered_dense_cable
kw testworld use 4 64 307 east ae2:fluix_covered_dense_cable
kw testworld use 5 64 307 east ae2:fluix_covered_dense_cable
kw testworld use 6 64 307 east ae2:fluix_covered_dense_cable
kw testworld use 7 64 307 east ae2:fluix_covered_dense_cable
kw testworld use 5 64 307 south ae2:fluix_smart_cable
kw testworld use 5 64 308 south ae2:fluix_smart_cable
setblock 5 64 310 ae2:drive[facing=south,spin=0]
kw testworld use 5 64 307 north ae2:fluix_smart_cable
setblock 5 64 305 ae2:drive[facing=south,spin=0]
kw testworld use 8 64 307 south ae2:fluix_smart_cable
kw testworld use 8 64 308 south ae2:fluix_smart_cable
setblock 8 64 310 ae2:drive[facing=south,spin=0]
kw testworld use 8 64 307 north ae2:fluix_smart_cable
setblock 8 64 305 ae2:drive[facing=south,spin=0]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
