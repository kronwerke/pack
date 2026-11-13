# 159 undergarden/arrival, guardian, forgotten, depths, infuser
#area 284 340 344 367
fill 284 64 340 324 91 367 minecraft:air
fill 325 64 340 344 91 367 minecraft:air
fill 284 60 340 344 62 367 minecraft:stone
fill 284 63 340 344 63 367 minecraft:light_gray_concrete
fill 288 64 346 344 79 346 minecraft:light_gray_concrete
fill 288 64 346 288 79 361 minecraft:light_gray_concrete
setblock 289 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 290 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 297 64 346 297 79 361 minecraft:light_gray_concrete
setblock 291 65 351 minecraft:stone_bricks
setblock 291 66 351 minecraft:stone_bricks
setblock 291 67 351 minecraft:stone_bricks
setblock 292 64 351 minecraft:stone_bricks
setblock 292 68 351 minecraft:stone_bricks
setblock 293 64 351 minecraft:stone_bricks
setblock 293 68 351 minecraft:stone_bricks
setblock 294 65 351 minecraft:stone_bricks
setblock 294 66 351 minecraft:stone_bricks
setblock 294 67 351 minecraft:stone_bricks
fill 292 65 351 293 67 351 undergarden:undergarden_portal[axis=x]
execute if block 292 66 351 undergarden:undergarden_portal
setblock 298 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.2"}','{"text": "undergarden"}','{"text": "guardian"}','{"text": ""}']}}
setblock 299 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Vergessenen"}','{"text": "Wächter"}','{"text": ""}']}}
fill 309 64 346 309 79 361 minecraft:light_gray_concrete
summon undergarden:forgotten_guardian 303.5 64 352.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 310 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.3"}','{"text": "undergarden"}','{"text": "forgotten"}','{"text": ""}']}}
setblock 311 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Werte die"}','{"text": "Spitzhacke auf"}','{"text": ""}','{"text": ""}']}}
fill 319 64 346 319 79 361 minecraft:light_gray_concrete
setblock 314 64 351 minecraft:smooth_stone_slab
summon item_display 314.5 65.4 351.5 {item:{id:"undergarden:forgotten_pickaxe",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 320 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.4"}','{"text": "undergarden"}','{"text": "depths"}','{"text": ""}']}}
setblock 321 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Brich in die"}','{"text": "Tiefen durch"}','{"text": ""}','{"text": ""}']}}
fill 329 64 346 329 79 361 minecraft:light_gray_concrete
fill 322 64 350 326 67 351 undergarden:dreadrock
setblock 323 65 351 undergarden:dreadrock_rogdorium_ore
setblock 324 65 351 undergarden:dreadrock_rogdorium_ore
setblock 324 66 351 undergarden:dreadrock_rogdorium_ore
setblock 325 66 351 undergarden:dreadrock_rogdorium_ore
setblock 322 67 351 undergarden:dreadrock_rogdorium_ore
setblock 326 64 351 undergarden:dreadrock_rogdorium_ore
setblock 324 64 353 minecraft:smooth_stone_slab
summon item_display 324.5 65.175 353.5 {item:{id:"undergarden:rogdorium",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.5f,1.5f,1.5f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 330 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.5"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 331 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 339 64 346 339 79 361 minecraft:light_gray_concrete
fill 333 63 350 335 63 352 undergarden:depthrock
setblock 334 64 351 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
