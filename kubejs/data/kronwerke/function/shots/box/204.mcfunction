# 204 nether/welcome, fortress, blaze_burner, biomes, structures, ig_kill, nm_kill, bastion, debris
fill 0 63 402 91 63 415 minecraft:light_gray_concrete
fill 0 64 402 91 71 402 minecraft:light_gray_concrete
fill 0 64 402 0 71 415 minecraft:light_gray_concrete
setblock 1 64 414 minecraft:air
setblock 1 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.1"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 414 minecraft:air
setblock 2 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 4 64 407 7 68 407 minecraft:obsidian
fill 5 65 407 6 67 407 minecraft:nether_portal[axis=x]
setblock 11 64 414 minecraft:air
setblock 11 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.2"}','{"text": "nether"}','{"text": "fortress"}','{"text": ""}']}}
setblock 12 64 414 minecraft:air
setblock 12 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde eine"}','{"text": "Netherfestung"}','{"text": ""}','{"text": ""}']}}
setblock 12 64 406 minecraft:nether_bricks
setblock 21 64 414 minecraft:air
setblock 21 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.3"}','{"text": "nether"}','{"text": "blaze_burner"}','{"text": ""}']}}
setblock 22 64 414 minecraft:air
setblock 22 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fang eine Lohe"}','{"text": "ein"}','{"text": ""}','{"text": ""}']}}
summon minecraft:blaze 25.5 65 407.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 29 64 411 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:blaze_burner",count:1}]}
setblock 31 64 414 minecraft:air
setblock 31 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.4"}','{"text": "nether"}','{"text": "biomes"}','{"text": ""}']}}
setblock 32 64 414 minecraft:air
setblock 32 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besuche alle"}','{"text": "fünf Biome"}','{"text": ""}','{"text": ""}']}}
setblock 32 64 406 minecraft:warped_fungus
setblock 41 64 414 minecraft:air
setblock 41 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.5"}','{"text": "nether"}','{"text": "structures"}','{"text": ""}']}}
setblock 42 64 414 minecraft:air
setblock 42 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde ein"}','{"text": "Bauwerk von"}','{"text": "Dungeons and"}','{"text": "Taverns"}']}}
setblock 42 64 406 minecraft:chiseled_polished_blackstone
setblock 51 64 414 minecraft:air
setblock 51 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.6"}','{"text": "nether"}','{"text": "ig_kill"}','{"text": ""}']}}
setblock 52 64 414 minecraft:air
setblock 52 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege Ignis"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
setblock 52 64 406 minecraft:polished_andesite
summon item_frame 52 64 407 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"cataclysm:ignitium_ingot",count:1}}
summon cataclysm:ignis 53.5 64 409.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 61 64 414 minecraft:air
setblock 61 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.7"}','{"text": "nether"}','{"text": "nm_kill"}','{"text": ""}']}}
setblock 62 64 414 minecraft:air
setblock 62 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Netherite"}','{"text": "Monstrosity"}','{"text": ""}']}}
setblock 62 64 406 minecraft:polished_andesite
summon item_frame 62 64 407 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"cataclysm:infernal_forge",count:1}}
summon cataclysm:netherite_monstrosity 63.5 64 409.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 71 64 414 minecraft:air
setblock 71 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.8"}','{"text": "nether"}','{"text": "bastion"}','{"text": ""}']}}
setblock 72 64 414 minecraft:air
setblock 72 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Plünder eine"}','{"text": "Bastion"}','{"text": ""}','{"text": ""}']}}
setblock 72 64 406 minecraft:gilded_blackstone
setblock 81 64 414 minecraft:air
setblock 81 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.9"}','{"text": "nether"}','{"text": "debris"}','{"text": ""}']}}
setblock 82 64 414 minecraft:air
setblock 82 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Grab Antiken"}','{"text": "Schrott"}','{"text": ""}','{"text": ""}']}}
setblock 82 64 406 minecraft:ancient_debris
