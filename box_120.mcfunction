# 120 ae2/channels
#area -4 254 17 279
fill -4 64 254 17 91 279 minecraft:air
fill -4 60 254 17 62 279 minecraft:stone
fill -4 63 254 17 63 279 minecraft:light_gray_concrete
fill 0 64 260 17 79 260 minecraft:light_gray_concrete
fill 0 64 260 0 79 273 minecraft:light_gray_concrete
setblock 1 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "120"}','{"text": "ae2"}','{"text": "channels"}','{"text": ""}']}}
setblock 2 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "controller with"}','{"text": "dense cables"}','{"text": "branching into"}','{"text": "normal smart"}']}}
setblock 3 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables, channel"}','{"text": "stripes visible"}','{"text": ""}','{"text": ""}']}}
fill 12 64 260 12 79 273 minecraft:light_gray_concrete
setblock 3 63 265 ae2:creative_energy_cell
setblock 3 64 265 ae2:controller
kw testworld use 3 64 265 east ae2:fluix_covered_dense_cable
kw testworld use 3 64 265 east ae2:fluix_covered_dense_cable
kw testworld use 4 64 265 east ae2:fluix_covered_dense_cable
kw testworld use 5 64 265 east ae2:fluix_covered_dense_cable
kw testworld use 6 64 265 east ae2:fluix_covered_dense_cable
kw testworld use 7 64 265 east ae2:fluix_covered_dense_cable
kw testworld use 5 64 265 south ae2:fluix_smart_cable
kw testworld use 5 64 266 south ae2:fluix_smart_cable
setblock 5 64 268 ae2:drive[facing=south,spin=0]
kw testworld use 5 64 265 north ae2:fluix_smart_cable
setblock 5 64 263 ae2:drive[facing=south,spin=0]
kw testworld use 8 64 265 south ae2:fluix_smart_cable
kw testworld use 8 64 266 south ae2:fluix_smart_cable
setblock 8 64 268 ae2:drive[facing=south,spin=0]
kw testworld use 8 64 265 north ae2:fluix_smart_cable
setblock 8 64 263 ae2:drive[facing=south,spin=0]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
