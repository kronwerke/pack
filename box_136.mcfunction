# 136 ae2/channels
#area -4 292 17 317
fill -4 64 292 17 91 317 minecraft:air
fill -4 60 292 17 62 317 minecraft:stone
fill -4 63 292 17 63 317 minecraft:light_gray_concrete
fill 0 64 298 17 79 298 minecraft:light_gray_concrete
fill 0 64 298 0 79 311 minecraft:light_gray_concrete
setblock 1 64 310 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136"}','{"text": "ae2"}','{"text": "channels"}','{"text": ""}']}}
setblock 2 64 310 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "controller with"}','{"text": "dense cables"}','{"text": "branching into"}','{"text": "normal smart"}']}}
setblock 3 64 310 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables, channel"}','{"text": "stripes visible"}','{"text": ""}','{"text": ""}']}}
fill 12 64 298 12 79 311 minecraft:light_gray_concrete
setblock 3 63 303 ae2:creative_energy_cell
setblock 3 64 303 ae2:controller
kw testworld use 3 64 303 east ae2:fluix_covered_dense_cable
kw testworld use 3 64 303 east ae2:fluix_covered_dense_cable
kw testworld use 4 64 303 east ae2:fluix_covered_dense_cable
kw testworld use 5 64 303 east ae2:fluix_covered_dense_cable
kw testworld use 6 64 303 east ae2:fluix_covered_dense_cable
kw testworld use 7 64 303 east ae2:fluix_covered_dense_cable
kw testworld use 5 64 303 south ae2:fluix_smart_cable
kw testworld use 5 64 304 south ae2:fluix_smart_cable
setblock 5 64 306 ae2:drive[facing=south,spin=0]
kw testworld use 5 64 303 north ae2:fluix_smart_cable
setblock 5 64 301 ae2:drive[facing=south,spin=0]
kw testworld use 8 64 303 south ae2:fluix_smart_cable
kw testworld use 8 64 304 south ae2:fluix_smart_cable
setblock 8 64 306 ae2:drive[facing=south,spin=0]
kw testworld use 8 64 303 north ae2:fluix_smart_cable
setblock 8 64 301 ae2:drive[facing=south,spin=0]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
