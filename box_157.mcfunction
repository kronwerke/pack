# 157 aether/portal, altar, ride, gloves, slider, queen
#area 158 340 232 367
fill 158 64 340 198 91 367 minecraft:air
fill 199 64 340 232 91 367 minecraft:air
fill 158 60 340 232 62 367 minecraft:stone
fill 158 63 340 232 63 367 minecraft:light_gray_concrete
fill 162 64 346 232 79 346 minecraft:light_gray_concrete
fill 162 64 346 162 79 361 minecraft:light_gray_concrete
setblock 163 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "157.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 164 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 171 64 346 171 79 361 minecraft:light_gray_concrete
setblock 165 65 351 minecraft:glowstone
setblock 165 66 351 minecraft:glowstone
setblock 165 67 351 minecraft:glowstone
setblock 166 64 351 minecraft:glowstone
setblock 166 68 351 minecraft:glowstone
setblock 167 64 351 minecraft:glowstone
setblock 167 68 351 minecraft:glowstone
setblock 168 65 351 minecraft:glowstone
setblock 168 66 351 minecraft:glowstone
setblock 168 67 351 minecraft:glowstone
fill 166 65 351 167 67 351 aether:aether_portal[axis=x]
execute if block 166 66 351 aether:aether_portal
setblock 172 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "157.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 173 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 181 64 346 181 79 361 minecraft:light_gray_concrete
fill 174 63 350 178 63 352 aether:holystone
setblock 174 64 351 aether:altar
setblock 176 64 351 aether:freezer
setblock 178 64 351 aether:incubator
setblock 182 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "157.3"}','{"text": "aether"}','{"text": "ride"}','{"text": ""}']}}
setblock 183 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reite ein Moa"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 193 64 346 193 79 361 minecraft:light_gray_concrete
summon aether:moa 187.5 64 352.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 194 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "157.4"}','{"text": "aether"}','{"text": "gloves"}','{"text": ""}']}}
setblock 195 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Trag Handschuhe"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 203 64 346 203 79 361 minecraft:light_gray_concrete
setblock 198 64 351 minecraft:smooth_stone_slab
summon item_display 198.5 65.4 351.5 {item:{id:"aether:zanite_gloves",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 204 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "157.5"}','{"text": "aether"}','{"text": "slider"}','{"text": ""}']}}
setblock 205 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Slider"}','{"text": ""}','{"text": ""}']}}
fill 215 64 346 215 79 361 minecraft:light_gray_concrete
summon aether:slider 209.5 64 352.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 216 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "157.6"}','{"text": "aether"}','{"text": "queen"}','{"text": ""}']}}
setblock 217 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Valkyrie Queen"}','{"text": ""}','{"text": ""}']}}
fill 227 64 346 227 79 361 minecraft:light_gray_concrete
summon aether:valkyrie_queen 221.5 64 352.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
