# 210 eternal_starlight/orb, portal, starfire, desert, forge, golem, garden, monstrosity
fill 192 63 421 275 63 436 minecraft:light_gray_concrete
fill 192 64 421 275 71 421 minecraft:light_gray_concrete
fill 192 64 421 192 71 436 minecraft:light_gray_concrete
setblock 193 64 435 minecraft:air
setblock 193 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "210.1"}','{"text": "eternal_starlight"}','{"text": "orb"}','{"text": ""}']}}
setblock 194 64 435 minecraft:air
setblock 194 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Gatekeeper"}','{"text": ""}','{"text": ""}']}}
setblock 194 64 425 minecraft:polished_andesite
summon item_frame 194 64 426 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"eternal_starlight:orb_of_prophecy",count:1}}
setblock 203 64 435 minecraft:air
setblock 203 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "210.2"}','{"text": "eternal_starlight"}','{"text": "portal"}','{"text": ""}']}}
setblock 204 64 435 minecraft:air
setblock 204 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne das"}','{"text": "Portal"}','{"text": ""}','{"text": ""}']}}
place template eternal_starlight:portal_ruins/common 204 64 423 none
setblock 215 64 435 minecraft:air
setblock 215 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "210.3"}','{"text": "eternal_starlight"}','{"text": "starfire"}','{"text": ""}']}}
setblock 216 64 435 minecraft:air
setblock 216 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol Starfire"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
setblock 216 64 425 minecraft:polished_andesite
summon item_frame 216 64 426 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"eternal_starlight:starfire",count:1}}
setblock 225 64 435 minecraft:air
setblock 225 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "210.4"}','{"text": "eternal_starlight"}','{"text": "desert"}','{"text": ""}']}}
setblock 226 64 435 minecraft:air
setblock 226 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Plünder die"}','{"text": "Kristallwüste"}','{"text": ""}','{"text": ""}']}}
setblock 226 64 425 minecraft:polished_andesite
summon item_frame 226 64 426 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"eternal_starlight:blue_starlight_crystal_shard",count:1}}
setblock 235 64 435 minecraft:air
setblock 235 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "210.5"}','{"text": "eternal_starlight"}','{"text": "forge"}','{"text": ""}']}}
setblock 236 64 435 minecraft:air
setblock 236 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Find eine"}','{"text": "Golemschmiede"}','{"text": ""}','{"text": ""}']}}
setblock 236 64 425 minecraft:polished_andesite
summon item_frame 236 64 426 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"eternal_starlight:frozen_tube",count:1}}
setblock 245 64 435 minecraft:air
setblock 245 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "210.6"}','{"text": "eternal_starlight"}','{"text": "golem"}','{"text": ""}']}}
setblock 246 64 435 minecraft:air
setblock 246 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Starlight Golem"}','{"text": ""}','{"text": ""}']}}
setblock 246 64 425 minecraft:polished_andesite
summon item_frame 246 64 426 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"eternal_starlight:energy_sword",count:1}}
summon eternal_starlight:starlight_golem 247.5 64 428.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 255 64 435 minecraft:air
setblock 255 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "210.7"}','{"text": "eternal_starlight"}','{"text": "garden"}','{"text": ""}']}}
setblock 256 64 435 minecraft:air
setblock 256 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Cursed Garden"}','{"text": ""}','{"text": ""}']}}
setblock 256 64 425 minecraft:polished_andesite
summon item_frame 256 64 426 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:flint_and_steel",count:1}}
setblock 258 64 425 eternal_starlight:tangled_skull
summon eternal_starlight:tangled 257.5 64 428.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 265 64 435 minecraft:air
setblock 265 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "210.8"}','{"text": "eternal_starlight"}','{"text": "monstrosity"}','{"text": ""}']}}
setblock 266 64 435 minecraft:air
setblock 266 64 435 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Lunar"}','{"text": "Monstrosity"}','{"text": ""}']}}
setblock 266 64 425 minecraft:polished_andesite
summon item_frame 266 64 426 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"eternal_starlight:crescent_spear",count:1}}
summon eternal_starlight:lunar_monstrosity 267.5 64 428.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
