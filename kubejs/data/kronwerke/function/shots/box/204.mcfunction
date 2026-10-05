# 204 nether/welcome, fortress, blaze_burner, biomes, structures, ig_kill, nm_kill, bastion, debris
fill 0 63 420 91 63 433 minecraft:light_gray_concrete
fill 0 64 420 91 71 420 minecraft:light_gray_concrete
fill 0 64 420 0 71 433 minecraft:light_gray_concrete
setblock 1 64 432 minecraft:air
setblock 1 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.1"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 432 minecraft:air
setblock 2 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
summon text_display 5.5 71 425.5 {text:'[{"text": "204.1  ", "color": "gold"}, {"text": "nether/welcome", "color": "gray"}, {"text": "\\nBetritt den Nether", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 4 64 425 7 68 425 minecraft:obsidian
fill 5 65 425 6 67 425 minecraft:nether_portal[axis=x]
setblock 11 64 432 minecraft:air
setblock 11 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.2"}','{"text": "nether"}','{"text": "fortress"}','{"text": ""}']}}
setblock 12 64 432 minecraft:air
setblock 12 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde eine"}','{"text": "Netherfestung"}','{"text": ""}','{"text": ""}']}}
summon text_display 15.5 71 425.5 {text:'[{"text": "204.2  ", "color": "gold"}, {"text": "nether/fortress", "color": "gray"}, {"text": "\\nFinde eine Netherfestung", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 12 63 422 18 63 425 minecraft:polished_deepslate
fill 12 64 422 18 67 422 minecraft:deepslate_tiles
fill 12 64 422 18 64 422 minecraft:polished_blackstone
fill 12 67 422 18 67 422 minecraft:polished_blackstone
setblock 12 64 425 minecraft:lantern
setblock 18 64 425 minecraft:lantern
setblock 14 64 424 minecraft:nether_bricks
setblock 21 64 432 minecraft:air
setblock 21 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.3"}','{"text": "nether"}','{"text": "blaze_burner"}','{"text": ""}']}}
setblock 22 64 432 minecraft:air
setblock 22 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fang eine Lohe"}','{"text": "ein"}','{"text": ""}','{"text": ""}']}}
summon text_display 25.5 71 425.5 {text:'[{"text": "204.3  ", "color": "gold"}, {"text": "nether/blaze_burner", "color": "gray"}, {"text": "\\nFang eine Lohe ein", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
summon minecraft:blaze 25.5 65 425.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 29 64 429 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:blaze_burner",count:1}]}
setblock 31 64 432 minecraft:air
setblock 31 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.4"}','{"text": "nether"}','{"text": "biomes"}','{"text": ""}']}}
setblock 32 64 432 minecraft:air
setblock 32 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besuche alle"}','{"text": "fünf Biome"}','{"text": ""}','{"text": ""}']}}
summon text_display 35.5 71 425.5 {text:'[{"text": "204.4  ", "color": "gold"}, {"text": "nether/biomes", "color": "gray"}, {"text": "\\nBesuche alle fünf Biome", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 32 63 422 38 63 425 minecraft:polished_deepslate
fill 32 64 422 38 67 422 minecraft:deepslate_tiles
fill 32 64 422 38 64 422 minecraft:polished_blackstone
fill 32 67 422 38 67 422 minecraft:polished_blackstone
setblock 32 64 425 minecraft:lantern
setblock 38 64 425 minecraft:lantern
setblock 34 64 424 minecraft:warped_fungus
setblock 41 64 432 minecraft:air
setblock 41 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.5"}','{"text": "nether"}','{"text": "structures"}','{"text": ""}']}}
setblock 42 64 432 minecraft:air
setblock 42 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde ein"}','{"text": "Bauwerk von"}','{"text": "Dungeons and"}','{"text": "Taverns"}']}}
summon text_display 45.5 71 425.5 {text:'[{"text": "204.5  ", "color": "gold"}, {"text": "nether/structures", "color": "gray"}, {"text": "\\nFinde ein Bauwerk von Dungeons and Taverns", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 42 63 422 48 63 425 minecraft:polished_deepslate
fill 42 64 422 48 67 422 minecraft:deepslate_tiles
fill 42 64 422 48 64 422 minecraft:polished_blackstone
fill 42 67 422 48 67 422 minecraft:polished_blackstone
setblock 42 64 425 minecraft:lantern
setblock 48 64 425 minecraft:lantern
setblock 44 64 424 minecraft:chiseled_polished_blackstone
setblock 51 64 432 minecraft:air
setblock 51 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.6"}','{"text": "nether"}','{"text": "ig_kill"}','{"text": ""}']}}
setblock 52 64 432 minecraft:air
setblock 52 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege Ignis"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 55.5 71 425.5 {text:'[{"text": "204.6  ", "color": "gold"}, {"text": "nether/ig_kill", "color": "gray"}, {"text": "\\nBesiege Ignis", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 52 63 422 58 63 425 minecraft:polished_deepslate
fill 52 64 422 58 67 422 minecraft:deepslate_tiles
fill 52 64 422 58 64 422 minecraft:polished_blackstone
fill 52 67 422 58 67 422 minecraft:polished_blackstone
setblock 52 64 425 minecraft:lantern
setblock 58 64 425 minecraft:lantern
summon glow_item_frame 54 66 423 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"cataclysm:ignitium_ingot",count:1}}
summon cataclysm:ignis 53.5 64 427.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 61 64 432 minecraft:air
setblock 61 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.7"}','{"text": "nether"}','{"text": "nm_kill"}','{"text": ""}']}}
setblock 62 64 432 minecraft:air
setblock 62 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Netherite"}','{"text": "Monstrosity"}','{"text": ""}']}}
summon text_display 65.5 71 425.5 {text:'[{"text": "204.7  ", "color": "gold"}, {"text": "nether/nm_kill", "color": "gray"}, {"text": "\\nBesiege die Netherite Monstrosity", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 62 63 422 68 63 425 minecraft:polished_deepslate
fill 62 64 422 68 67 422 minecraft:deepslate_tiles
fill 62 64 422 68 64 422 minecraft:polished_blackstone
fill 62 67 422 68 67 422 minecraft:polished_blackstone
setblock 62 64 425 minecraft:lantern
setblock 68 64 425 minecraft:lantern
summon glow_item_frame 64 66 423 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"cataclysm:infernal_forge",count:1}}
summon cataclysm:netherite_monstrosity 63.5 64 427.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 71 64 432 minecraft:air
setblock 71 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.8"}','{"text": "nether"}','{"text": "bastion"}','{"text": ""}']}}
setblock 72 64 432 minecraft:air
setblock 72 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Plünder eine"}','{"text": "Bastion"}','{"text": ""}','{"text": ""}']}}
summon text_display 75.5 71 425.5 {text:'[{"text": "204.8  ", "color": "gold"}, {"text": "nether/bastion", "color": "gray"}, {"text": "\\nPlünder eine Bastion", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 72 63 422 78 63 425 minecraft:polished_deepslate
fill 72 64 422 78 67 422 minecraft:deepslate_tiles
fill 72 64 422 78 64 422 minecraft:polished_blackstone
fill 72 67 422 78 67 422 minecraft:polished_blackstone
setblock 72 64 425 minecraft:lantern
setblock 78 64 425 minecraft:lantern
setblock 74 64 424 minecraft:gilded_blackstone
setblock 81 64 432 minecraft:air
setblock 81 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "204.9"}','{"text": "nether"}','{"text": "debris"}','{"text": ""}']}}
setblock 82 64 432 minecraft:air
setblock 82 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Grab Antiken"}','{"text": "Schrott"}','{"text": ""}','{"text": ""}']}}
summon text_display 85.5 71 425.5 {text:'[{"text": "204.9  ", "color": "gold"}, {"text": "nether/debris", "color": "gray"}, {"text": "\\nGrab Antiken Schrott", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 82 63 422 88 63 425 minecraft:polished_deepslate
fill 82 64 422 88 67 422 minecraft:deepslate_tiles
fill 82 64 422 88 64 422 minecraft:polished_blackstone
fill 82 67 422 88 67 422 minecraft:polished_blackstone
setblock 82 64 425 minecraft:lantern
setblock 88 64 425 minecraft:lantern
setblock 84 64 424 minecraft:ancient_debris
