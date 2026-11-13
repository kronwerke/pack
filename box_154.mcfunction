# 154 undergarden/arrival, guardian, forgotten, depths, infuser
#area 284 336 344 363
fill 284 64 336 324 91 363 minecraft:air
fill 325 64 336 344 91 363 minecraft:air
fill 284 60 336 344 62 363 minecraft:stone
fill 284 63 336 344 63 363 minecraft:light_gray_concrete
fill 288 64 342 344 79 342 minecraft:light_gray_concrete
fill 288 64 342 288 79 357 minecraft:light_gray_concrete
setblock 289 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 290 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 297 64 342 297 79 357 minecraft:light_gray_concrete
setblock 291 65 347 minecraft:stone_bricks
setblock 291 66 347 minecraft:stone_bricks
setblock 291 67 347 minecraft:stone_bricks
setblock 292 64 347 minecraft:stone_bricks
setblock 292 68 347 minecraft:stone_bricks
setblock 293 64 347 minecraft:stone_bricks
setblock 293 68 347 minecraft:stone_bricks
setblock 294 65 347 minecraft:stone_bricks
setblock 294 66 347 minecraft:stone_bricks
setblock 294 67 347 minecraft:stone_bricks
fill 292 65 347 293 67 347 undergarden:undergarden_portal[axis=x]
execute if block 292 66 347 undergarden:undergarden_portal
setblock 298 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.2"}','{"text": "undergarden"}','{"text": "guardian"}','{"text": ""}']}}
setblock 299 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Vergessenen"}','{"text": "Wächter"}','{"text": ""}']}}
fill 309 64 342 309 79 357 minecraft:light_gray_concrete
summon undergarden:forgotten_guardian 303.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 310 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.3"}','{"text": "undergarden"}','{"text": "forgotten"}','{"text": ""}']}}
setblock 311 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Werte die"}','{"text": "Spitzhacke auf"}','{"text": ""}','{"text": ""}']}}
fill 319 64 342 319 79 357 minecraft:light_gray_concrete
setblock 314 64 347 minecraft:smooth_stone_slab
summon item_display 314.5 65.4 347.5 {item:{id:"undergarden:forgotten_pickaxe",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 320 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.4"}','{"text": "undergarden"}','{"text": "depths"}','{"text": ""}']}}
setblock 321 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Brich in die"}','{"text": "Tiefen durch"}','{"text": ""}','{"text": ""}']}}
fill 329 64 342 329 79 357 minecraft:light_gray_concrete
fill 322 64 346 326 67 347 undergarden:dreadrock
setblock 323 65 347 undergarden:dreadrock_rogdorium_ore
setblock 324 65 347 undergarden:dreadrock_rogdorium_ore
setblock 324 66 347 undergarden:dreadrock_rogdorium_ore
setblock 325 66 347 undergarden:dreadrock_rogdorium_ore
setblock 322 67 347 undergarden:dreadrock_rogdorium_ore
setblock 326 64 347 undergarden:dreadrock_rogdorium_ore
setblock 324 64 349 minecraft:smooth_stone_slab
summon item_display 324.5 65.175 349.5 {item:{id:"undergarden:rogdorium",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.5f,1.5f,1.5f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 330 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.5"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 331 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 339 64 342 339 79 357 minecraft:light_gray_concrete
fill 333 63 346 335 63 348 undergarden:depthrock
setblock 334 64 347 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
