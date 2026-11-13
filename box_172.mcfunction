# 172 aether/portal, altar, ride, gloves, slider, queen
#area 158 342 232 369
fill 158 64 342 198 91 369 minecraft:air
fill 199 64 342 232 91 369 minecraft:air
fill 158 60 342 232 62 369 minecraft:stone
fill 158 63 342 232 63 369 minecraft:light_gray_concrete
fill 162 64 348 232 79 348 minecraft:light_gray_concrete
fill 162 64 348 162 79 363 minecraft:light_gray_concrete
setblock 163 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 164 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 171 64 348 171 79 363 minecraft:light_gray_concrete
setblock 165 65 353 minecraft:glowstone
setblock 165 66 353 minecraft:glowstone
setblock 165 67 353 minecraft:glowstone
setblock 166 64 353 minecraft:glowstone
setblock 166 68 353 minecraft:glowstone
setblock 167 64 353 minecraft:glowstone
setblock 167 68 353 minecraft:glowstone
setblock 168 65 353 minecraft:glowstone
setblock 168 66 353 minecraft:glowstone
setblock 168 67 353 minecraft:glowstone
fill 166 65 353 167 67 353 aether:aether_portal[axis=x]
execute if block 166 66 353 aether:aether_portal
setblock 172 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 173 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 181 64 348 181 79 363 minecraft:light_gray_concrete
fill 174 63 352 178 63 354 aether:holystone
setblock 174 64 353 aether:altar
setblock 176 64 353 aether:freezer
setblock 178 64 353 aether:incubator
setblock 182 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172.3"}','{"text": "aether"}','{"text": "ride"}','{"text": ""}']}}
setblock 183 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reite ein Moa"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 193 64 348 193 79 363 minecraft:light_gray_concrete
summon aether:moa 187.5 64 354.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 194 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172.4"}','{"text": "aether"}','{"text": "gloves"}','{"text": ""}']}}
setblock 195 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Trag Handschuhe"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 203 64 348 203 79 363 minecraft:light_gray_concrete
setblock 198 64 353 minecraft:smooth_stone_slab
summon item_display 198.5 65.4 353.5 {item:{id:"aether:zanite_gloves",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 204 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172.5"}','{"text": "aether"}','{"text": "slider"}','{"text": ""}']}}
setblock 205 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Slider"}','{"text": ""}','{"text": ""}']}}
fill 215 64 348 215 79 363 minecraft:light_gray_concrete
summon aether:slider 209.5 64 354.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 216 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172.6"}','{"text": "aether"}','{"text": "queen"}','{"text": ""}']}}
setblock 217 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Valkyrie Queen"}','{"text": ""}','{"text": ""}']}}
fill 227 64 348 227 79 363 minecraft:light_gray_concrete
summon aether:valkyrie_queen 221.5 64 354.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
