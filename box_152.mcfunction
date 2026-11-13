# 152 aether/portal, altar, ride, gloves, slider, queen
#area 158 336 232 363
fill 158 64 336 198 91 363 minecraft:air
fill 199 64 336 232 91 363 minecraft:air
fill 158 60 336 232 62 363 minecraft:stone
fill 158 63 336 232 63 363 minecraft:light_gray_concrete
fill 162 64 342 232 79 342 minecraft:light_gray_concrete
fill 162 64 342 162 79 357 minecraft:light_gray_concrete
setblock 163 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 164 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 171 64 342 171 79 357 minecraft:light_gray_concrete
setblock 165 65 347 minecraft:glowstone
setblock 165 66 347 minecraft:glowstone
setblock 165 67 347 minecraft:glowstone
setblock 166 64 347 minecraft:glowstone
setblock 166 68 347 minecraft:glowstone
setblock 167 64 347 minecraft:glowstone
setblock 167 68 347 minecraft:glowstone
setblock 168 65 347 minecraft:glowstone
setblock 168 66 347 minecraft:glowstone
setblock 168 67 347 minecraft:glowstone
fill 166 65 347 167 67 347 aether:aether_portal[axis=x]
execute if block 166 66 347 aether:aether_portal
setblock 172 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 173 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 181 64 342 181 79 357 minecraft:light_gray_concrete
fill 174 63 346 178 63 348 aether:holystone
setblock 174 64 347 aether:altar
setblock 176 64 347 aether:freezer
setblock 178 64 347 aether:incubator
setblock 182 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.3"}','{"text": "aether"}','{"text": "ride"}','{"text": ""}']}}
setblock 183 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reite ein Moa"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 193 64 342 193 79 357 minecraft:light_gray_concrete
summon aether:moa 187.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 194 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.4"}','{"text": "aether"}','{"text": "gloves"}','{"text": ""}']}}
setblock 195 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Trag Handschuhe"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 203 64 342 203 79 357 minecraft:light_gray_concrete
setblock 198 64 347 minecraft:smooth_stone_slab
summon item_display 198.5 65.4 347.5 {item:{id:"aether:zanite_gloves",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 204 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.5"}','{"text": "aether"}','{"text": "slider"}','{"text": ""}']}}
setblock 205 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Slider"}','{"text": ""}','{"text": ""}']}}
fill 215 64 342 215 79 357 minecraft:light_gray_concrete
summon aether:slider 209.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 216 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.6"}','{"text": "aether"}','{"text": "queen"}','{"text": ""}']}}
setblock 217 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Valkyrie Queen"}','{"text": ""}','{"text": ""}']}}
fill 227 64 342 227 79 357 minecraft:light_gray_concrete
summon aether:valkyrie_queen 221.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
