# 152 aether/portal, altar, ride, gloves, slider, queen
#area 118 336 192 363
fill 118 64 336 158 91 363 minecraft:air
fill 159 64 336 192 91 363 minecraft:air
fill 118 60 336 192 62 363 minecraft:stone
fill 118 63 336 192 63 363 minecraft:light_gray_concrete
fill 122 64 342 192 79 342 minecraft:light_gray_concrete
fill 122 64 342 122 79 357 minecraft:light_gray_concrete
setblock 123 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 124 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 131 64 342 131 79 357 minecraft:light_gray_concrete
setblock 125 65 347 minecraft:glowstone
setblock 125 66 347 minecraft:glowstone
setblock 125 67 347 minecraft:glowstone
setblock 126 64 347 minecraft:glowstone
setblock 126 68 347 minecraft:glowstone
setblock 127 64 347 minecraft:glowstone
setblock 127 68 347 minecraft:glowstone
setblock 128 65 347 minecraft:glowstone
setblock 128 66 347 minecraft:glowstone
setblock 128 67 347 minecraft:glowstone
fill 126 65 347 127 67 347 aether:aether_portal[axis=x]
execute if block 126 66 347 aether:aether_portal
setblock 132 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 133 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 141 64 342 141 79 357 minecraft:light_gray_concrete
fill 134 63 346 138 63 348 aether:holystone
setblock 134 64 347 aether:altar
setblock 136 64 347 aether:freezer
setblock 138 64 347 aether:incubator
setblock 142 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.3"}','{"text": "aether"}','{"text": "ride"}','{"text": ""}']}}
setblock 143 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reite ein Moa"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 153 64 342 153 79 357 minecraft:light_gray_concrete
summon aether:moa 147.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 154 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.4"}','{"text": "aether"}','{"text": "gloves"}','{"text": ""}']}}
setblock 155 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Trag Handschuhe"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 163 64 342 163 79 357 minecraft:light_gray_concrete
setblock 158 64 347 minecraft:smooth_stone_slab
summon item_display 158.5 65.4 347.5 {item:{id:"aether:zanite_gloves",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 164 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.5"}','{"text": "aether"}','{"text": "slider"}','{"text": ""}']}}
setblock 165 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Slider"}','{"text": ""}','{"text": ""}']}}
fill 175 64 342 175 79 357 minecraft:light_gray_concrete
summon aether:slider 169.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 176 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.6"}','{"text": "aether"}','{"text": "queen"}','{"text": ""}']}}
setblock 177 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Valkyrie Queen"}','{"text": ""}','{"text": ""}']}}
fill 187 64 342 187 79 357 minecraft:light_gray_concrete
summon aether:valkyrie_queen 181.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
