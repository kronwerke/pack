# 154 undergarden/arrival, guardian, forgotten, infuser
#area 156 336 206 363
fill 156 64 336 196 91 363 minecraft:air
fill 197 64 336 206 91 363 minecraft:air
fill 156 60 336 206 62 363 minecraft:stone
fill 156 63 336 206 63 363 minecraft:light_gray_concrete
fill 160 64 342 206 79 342 minecraft:light_gray_concrete
fill 160 64 342 160 79 357 minecraft:light_gray_concrete
setblock 161 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 162 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 169 64 342 169 79 357 minecraft:light_gray_concrete
setblock 163 65 347 minecraft:stone_bricks
setblock 163 66 347 minecraft:stone_bricks
setblock 163 67 347 minecraft:stone_bricks
setblock 164 64 347 minecraft:stone_bricks
setblock 164 68 347 minecraft:stone_bricks
setblock 165 64 347 minecraft:stone_bricks
setblock 165 68 347 minecraft:stone_bricks
setblock 166 65 347 minecraft:stone_bricks
setblock 166 66 347 minecraft:stone_bricks
setblock 166 67 347 minecraft:stone_bricks
fill 164 65 347 165 67 347 undergarden:undergarden_portal[axis=x]
execute if block 164 66 347 undergarden:undergarden_portal
setblock 170 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.2"}','{"text": "undergarden"}','{"text": "guardian"}','{"text": ""}']}}
setblock 171 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Vergessenen"}','{"text": "Wächter"}','{"text": ""}']}}
fill 181 64 342 181 79 357 minecraft:light_gray_concrete
summon undergarden:forgotten_guardian 175.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 182 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.3"}','{"text": "undergarden"}','{"text": "forgotten"}','{"text": ""}']}}
setblock 183 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Werte die"}','{"text": "Spitzhacke auf"}','{"text": ""}','{"text": ""}']}}
fill 191 64 342 191 79 357 minecraft:light_gray_concrete
setblock 186 64 347 minecraft:smooth_stone_slab
summon item_display 186.5 65.4 347.5 {item:{id:"undergarden:forgotten_pickaxe",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 192 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.4"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 193 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 201 64 342 201 79 357 minecraft:light_gray_concrete
fill 195 63 346 197 63 348 undergarden:depthrock
setblock 196 64 347 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
