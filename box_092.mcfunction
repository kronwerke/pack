# 092 botania_runes/rune_core
#area 199 143 218 168
fill 199 64 143 218 91 168 minecraft:air
fill 199 60 143 218 62 168 minecraft:stone
fill 199 63 143 218 63 168 minecraft:light_gray_concrete
fill 203 64 149 218 79 149 minecraft:light_gray_concrete
fill 203 64 149 203 79 162 minecraft:light_gray_concrete
setblock 204 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092"}','{"text": "botania_runes"}','{"text": "rune_core"}','{"text": ""}']}}
setblock 205 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the crafting"}','{"text": "grid"}','{"text": ""}','{"text": ""}']}}
fill 213 64 149 213 79 162 minecraft:light_gray_concrete
setblock 208 64 154 minecraft:smooth_stone_slab
summon item_display 208.5 64.95 154.5 {item:{id:"kronwerke:rune_core",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
