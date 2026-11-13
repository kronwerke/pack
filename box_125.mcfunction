# 125 ae2/channels
#area -4 256 17 281
fill -4 64 256 17 91 281 minecraft:air
fill -4 60 256 17 62 281 minecraft:stone
fill -4 63 256 17 63 281 minecraft:light_gray_concrete
fill 0 64 262 17 79 262 minecraft:light_gray_concrete
fill 0 64 262 0 79 275 minecraft:light_gray_concrete
setblock 1 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125"}','{"text": "ae2"}','{"text": "channels"}','{"text": ""}']}}
setblock 2 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "controller with"}','{"text": "dense cables"}','{"text": "branching into"}','{"text": "normal smart"}']}}
setblock 3 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables, channel"}','{"text": "stripes visible"}','{"text": ""}','{"text": ""}']}}
fill 12 64 262 12 79 275 minecraft:light_gray_concrete
setblock 3 63 267 ae2:creative_energy_cell
setblock 3 64 267 ae2:controller
kw testworld use 3 64 267 east ae2:fluix_covered_dense_cable
kw testworld use 3 64 267 east ae2:fluix_covered_dense_cable
kw testworld use 4 64 267 east ae2:fluix_covered_dense_cable
kw testworld use 5 64 267 east ae2:fluix_covered_dense_cable
kw testworld use 6 64 267 east ae2:fluix_covered_dense_cable
kw testworld use 7 64 267 east ae2:fluix_covered_dense_cable
kw testworld use 5 64 267 south ae2:fluix_smart_cable
kw testworld use 5 64 268 south ae2:fluix_smart_cable
setblock 5 64 270 ae2:drive[facing=south,spin=0]
kw testworld use 5 64 267 north ae2:fluix_smart_cable
setblock 5 64 265 ae2:drive[facing=south,spin=0]
kw testworld use 8 64 267 south ae2:fluix_smart_cable
kw testworld use 8 64 268 south ae2:fluix_smart_cable
setblock 8 64 270 ae2:drive[facing=south,spin=0]
kw testworld use 8 64 267 north ae2:fluix_smart_cable
setblock 8 64 265 ae2:drive[facing=south,spin=0]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
