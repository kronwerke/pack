# 154 undergarden/arrival, guardian, forgotten, infuser
#area 244 336 294 363
fill 244 64 336 284 91 363 minecraft:air
fill 285 64 336 294 91 363 minecraft:air
fill 244 60 336 294 62 363 minecraft:stone
fill 244 63 336 294 63 363 minecraft:light_gray_concrete
fill 248 64 342 294 79 342 minecraft:light_gray_concrete
fill 248 64 342 248 79 357 minecraft:light_gray_concrete
setblock 249 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 250 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 257 64 342 257 79 357 minecraft:light_gray_concrete
setblock 251 65 347 minecraft:stone_bricks
setblock 251 66 347 minecraft:stone_bricks
setblock 251 67 347 minecraft:stone_bricks
setblock 252 64 347 minecraft:stone_bricks
setblock 252 68 347 minecraft:stone_bricks
setblock 253 64 347 minecraft:stone_bricks
setblock 253 68 347 minecraft:stone_bricks
setblock 254 65 347 minecraft:stone_bricks
setblock 254 66 347 minecraft:stone_bricks
setblock 254 67 347 minecraft:stone_bricks
fill 252 65 347 253 67 347 undergarden:undergarden_portal[axis=x]
execute if block 252 66 347 undergarden:undergarden_portal
setblock 258 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.2"}','{"text": "undergarden"}','{"text": "guardian"}','{"text": ""}']}}
setblock 259 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Vergessenen"}','{"text": "Wächter"}','{"text": ""}']}}
fill 269 64 342 269 79 357 minecraft:light_gray_concrete
summon undergarden:forgotten_guardian 263.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 270 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.3"}','{"text": "undergarden"}','{"text": "forgotten"}','{"text": ""}']}}
setblock 271 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Werte die"}','{"text": "Spitzhacke auf"}','{"text": ""}','{"text": ""}']}}
fill 279 64 342 279 79 357 minecraft:light_gray_concrete
setblock 274 64 347 minecraft:smooth_stone_slab
summon item_display 274.5 65.4 347.5 {item:{id:"undergarden:forgotten_pickaxe",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 280 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.4"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 281 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 289 64 342 289 79 357 minecraft:light_gray_concrete
fill 283 63 346 285 63 348 undergarden:depthrock
setblock 284 64 347 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
