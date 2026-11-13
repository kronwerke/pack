# 099 productive_trees/first_tree, sawmill_run
#area 131 277 160 302
fill 131 64 277 160 91 302 minecraft:air
fill 131 60 277 160 62 302 minecraft:stone
fill 131 63 277 160 63 302 minecraft:light_gray_concrete
fill 135 64 283 160 79 283 minecraft:light_gray_concrete
fill 135 64 283 135 79 296 minecraft:light_gray_concrete
setblock 136 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099.1"}','{"text": "productive_trees"}','{"text": "first_tree"}','{"text": ""}']}}
setblock 137 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Pflanz die"}','{"text": "Walnuss und"}','{"text": "ernte Nüsse"}','{"text": ""}']}}
fill 145 64 283 145 79 296 minecraft:light_gray_concrete
fill 140 64 288 140 68 288 productivetrees:walnut_log[axis=y]
setblock 138 67 287 productivetrees:walnut_leaves
setblock 138 67 288 productivetrees:walnut_leaves
setblock 138 67 289 productivetrees:walnut_leaves
setblock 139 67 286 productivetrees:walnut_fruit[age=7]
setblock 139 67 287 productivetrees:walnut_fruit[age=7]
setblock 139 67 288 productivetrees:walnut_fruit[age=7]
setblock 139 67 289 productivetrees:walnut_fruit[age=7]
setblock 139 67 290 productivetrees:walnut_fruit[age=7]
setblock 140 67 286 productivetrees:walnut_fruit[age=7]
setblock 140 67 287 productivetrees:walnut_fruit[age=7]
setblock 140 67 289 productivetrees:walnut_fruit[age=7]
setblock 140 67 290 productivetrees:walnut_fruit[age=7]
setblock 141 67 286 productivetrees:walnut_leaves
setblock 141 67 287 productivetrees:walnut_leaves
setblock 141 67 288 productivetrees:walnut_leaves
setblock 141 67 289 productivetrees:walnut_leaves
setblock 141 67 290 productivetrees:walnut_leaves
setblock 142 67 287 productivetrees:walnut_fruit[age=7]
setblock 142 67 288 productivetrees:walnut_fruit[age=7]
setblock 142 67 289 productivetrees:walnut_fruit[age=7]
setblock 138 68 287 productivetrees:walnut_fruit[age=7]
setblock 138 68 288 productivetrees:walnut_fruit[age=7]
setblock 138 68 289 productivetrees:walnut_fruit[age=7]
setblock 139 68 286 productivetrees:walnut_leaves
setblock 139 68 287 productivetrees:walnut_leaves
setblock 139 68 288 productivetrees:walnut_leaves
setblock 139 68 289 productivetrees:walnut_leaves
setblock 139 68 290 productivetrees:walnut_leaves
setblock 140 68 286 productivetrees:walnut_fruit[age=7]
setblock 140 68 287 productivetrees:walnut_fruit[age=7]
setblock 140 68 289 productivetrees:walnut_fruit[age=7]
setblock 140 68 290 productivetrees:walnut_fruit[age=7]
setblock 141 68 286 productivetrees:walnut_fruit[age=7]
setblock 141 68 287 productivetrees:walnut_fruit[age=7]
setblock 141 68 288 productivetrees:walnut_fruit[age=7]
setblock 141 68 289 productivetrees:walnut_fruit[age=7]
setblock 141 68 290 productivetrees:walnut_fruit[age=7]
setblock 142 68 287 productivetrees:walnut_leaves
setblock 142 68 288 productivetrees:walnut_leaves
setblock 142 68 289 productivetrees:walnut_leaves
setblock 139 69 287 productivetrees:walnut_fruit[age=7]
setblock 139 69 288 productivetrees:walnut_fruit[age=7]
setblock 139 69 289 productivetrees:walnut_fruit[age=7]
setblock 140 69 287 productivetrees:walnut_leaves
setblock 140 69 288 productivetrees:walnut_leaves
setblock 140 69 289 productivetrees:walnut_leaves
setblock 141 69 287 productivetrees:walnut_fruit[age=7]
setblock 141 69 288 productivetrees:walnut_fruit[age=7]
setblock 141 69 289 productivetrees:walnut_fruit[age=7]
setblock 139 70 287 productivetrees:walnut_leaves
setblock 139 70 288 productivetrees:walnut_leaves
setblock 139 70 289 productivetrees:walnut_leaves
setblock 140 70 287 productivetrees:walnut_fruit[age=7]
setblock 140 70 288 productivetrees:walnut_fruit[age=7]
setblock 140 70 289 productivetrees:walnut_fruit[age=7]
setblock 141 70 287 productivetrees:walnut_leaves
setblock 141 70 288 productivetrees:walnut_leaves
setblock 141 70 289 productivetrees:walnut_leaves
setblock 138 64 290 productivetrees:walnut_sapling
setblock 146 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099.2"}','{"text": "productive_trees"}','{"text": "sawmill_run"}','{"text": ""}']}}
setblock 147 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Säge Stämme im"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 155 64 283 155 79 296 minecraft:light_gray_concrete
setblock 149 64 288 productivetrees:sawmill
setblock 149 65 288 minecraft:hopper[facing=down]
setblock 151 64 288 productivetrees:stripper
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
