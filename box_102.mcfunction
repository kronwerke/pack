# 102 botania_runes/rune_core
#area 199 147 218 172
fill 199 64 147 218 91 172 minecraft:air
fill 199 60 147 218 62 172 minecraft:stone
fill 199 63 147 218 63 172 minecraft:light_gray_concrete
fill 203 64 153 218 79 153 minecraft:light_gray_concrete
fill 203 64 153 203 79 166 minecraft:light_gray_concrete
setblock 204 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102"}','{"text": "botania_runes"}','{"text": "rune_core"}','{"text": ""}']}}
setblock 205 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the crafting"}','{"text": "grid"}','{"text": ""}','{"text": ""}']}}
fill 213 64 153 213 79 166 minecraft:light_gray_concrete
setblock 208 64 158 minecraft:smooth_stone_slab
summon item_display 208.5 65.4 158.5 {item:{id:"kronwerke:rune_core",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
