# 183 industrial/addons, sower, gatherer, bio, slaughter, crusher, duplicator
fill 0 63 297 71 63 310 minecraft:light_gray_concrete
fill 0 64 297 71 71 297 minecraft:light_gray_concrete
fill 0 64 297 0 71 310 minecraft:light_gray_concrete
setblock 1 64 309 minecraft:air
setblock 1 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.1"}','{"text": "industrial"}','{"text": "addons"}','{"text": ""}']}}
setblock 2 64 309 minecraft:air
setblock 2 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the machines at"}','{"text": "work"}','{"text": ""}','{"text": ""}']}}
setblock 2 64 300 industrialforegoing:plant_sower
setblock 9 64 306 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"industrialforegoing:speed_addon_tier_1",count:1},{Slot:1b,id:"industrialforegoing:efficiency_addon_tier_1",count:1}]}
setblock 11 64 309 minecraft:air
setblock 11 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.2"}','{"text": "industrial"}','{"text": "sower"}','{"text": ""}']}}
setblock 12 64 309 minecraft:air
setblock 12 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Sämaschine auf"}','{"text": ""}','{"text": ""}']}}
fill 12 63 299 18 63 305 minecraft:farmland
fill 12 64 299 18 64 305 minecraft:wheat[age=7]
setblock 15 64 302 industrialforegoing:plant_sower
setblock 15 65 302 industrialforegoing:plant_gatherer
setblock 21 64 309 minecraft:air
setblock 21 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.3"}','{"text": "industrial"}','{"text": "gatherer"}','{"text": ""}']}}
setblock 22 64 309 minecraft:air
setblock 22 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Erntemaschine"}','{"text": "auf"}','{"text": ""}']}}
fill 22 63 299 28 63 305 minecraft:farmland
fill 22 64 299 28 64 305 minecraft:wheat[age=7]
setblock 25 64 302 industrialforegoing:plant_sower
setblock 25 65 302 industrialforegoing:plant_gatherer
setblock 31 64 309 minecraft:air
setblock 31 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.4"}','{"text": "industrial"}','{"text": "bio"}','{"text": ""}']}}
setblock 32 64 309 minecraft:air
setblock 32 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betreib einen"}','{"text": "Biogenerator"}','{"text": ""}','{"text": ""}']}}
setblock 32 64 300 industrialforegoing:bioreactor
setblock 34 64 300 industrialforegoing:biofuel_generator
setblock 41 64 309 minecraft:air
setblock 41 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.5"}','{"text": "industrial"}','{"text": "slaughter"}','{"text": ""}']}}
setblock 42 64 309 minecraft:air
setblock 42 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fang Pinken"}','{"text": "Schleim auf"}','{"text": ""}','{"text": ""}']}}
setblock 42 64 300 industrialforegoing:mob_slaughter_factory
summon minecraft:cow 43.5 64 304.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:pig 46.5 64 304.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 51 64 309 minecraft:air
setblock 51 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.6"}','{"text": "industrial"}','{"text": "crusher"}','{"text": ""}']}}
setblock 52 64 309 minecraft:air
setblock 52 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterschnetzler"}','{"text": "auf"}','{"text": ""}']}}
setblock 52 64 300 industrialforegoing:mob_crusher
summon minecraft:zombie 53.5 64 304.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 61 64 309 minecraft:air
setblock 61 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.7"}','{"text": "industrial"}','{"text": "duplicator"}','{"text": ""}']}}
setblock 62 64 309 minecraft:air
setblock 62 64 309 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterspawner"}','{"text": "auf"}','{"text": ""}']}}
setblock 62 64 300 industrialforegoing:mob_duplicator
