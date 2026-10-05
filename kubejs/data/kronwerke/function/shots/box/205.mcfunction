# 205 the_end/arrival, crystals, dragon, egg, respawn, elytra, cg_find, cg_kill, st_aviary, draconium
fill 95 63 402 196 63 415 minecraft:light_gray_concrete
fill 95 64 402 196 71 402 minecraft:light_gray_concrete
fill 95 64 402 95 71 415 minecraft:light_gray_concrete
setblock 96 64 414 minecraft:air
setblock 96 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.1"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 97 64 414 minecraft:air
setblock 97 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Aufnahme in the"}','{"text": "end"}','{"text": ""}','{"text": ""}']}}
setblock 97 64 406 minecraft:end_stone
setblock 106 64 414 minecraft:air
setblock 106 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.2"}','{"text": "the_end"}','{"text": "crystals"}','{"text": ""}']}}
setblock 107 64 414 minecraft:air
setblock 107 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zerstör die"}','{"text": "Endkristalle"}','{"text": ""}','{"text": ""}']}}
setblock 107 64 406 minecraft:polished_andesite
summon item_frame 107 64 407 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:end_crystal",count:1}}
setblock 116 64 414 minecraft:air
setblock 116 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.3"}','{"text": "the_end"}','{"text": "dragon"}','{"text": ""}']}}
setblock 117 64 414 minecraft:air
setblock 117 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Enderdrachen"}','{"text": ""}','{"text": ""}']}}
setblock 117 64 406 minecraft:dragon_head
setblock 126 64 414 minecraft:air
setblock 126 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.4"}','{"text": "the_end"}','{"text": "egg"}','{"text": ""}']}}
setblock 127 64 414 minecraft:air
setblock 127 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol das"}','{"text": "Drachenei"}','{"text": ""}','{"text": ""}']}}
fill 128 64 405 132 64 409 minecraft:bedrock
setblock 130 65 407 minecraft:dragon_egg
summon minecraft:end_crystal 130.5 64 404.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
summon minecraft:end_crystal 130.5 64 410.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
summon minecraft:end_crystal 127.5 64 407.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
summon minecraft:end_crystal 133.5 64 407.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
setblock 136 64 414 minecraft:air
setblock 136 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.5"}','{"text": "the_end"}','{"text": "respawn"}','{"text": ""}']}}
setblock 137 64 414 minecraft:air
setblock 137 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Beschwör den"}','{"text": "Drachen neu"}','{"text": ""}','{"text": ""}']}}
fill 138 64 405 142 64 409 minecraft:bedrock
setblock 140 65 407 minecraft:dragon_egg
summon minecraft:end_crystal 140.5 64 404.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
summon minecraft:end_crystal 140.5 64 410.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
summon minecraft:end_crystal 137.5 64 407.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
summon minecraft:end_crystal 143.5 64 407.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
setblock 146 64 414 minecraft:air
setblock 146 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.6"}','{"text": "the_end"}','{"text": "elytra"}','{"text": ""}']}}
setblock 147 64 414 minecraft:air
setblock 147 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mit Elytra"}','{"text": "fliegen"}','{"text": ""}','{"text": ""}']}}
setblock 154 64 411 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:elytra",count:1}]}
setblock 156 64 414 minecraft:air
setblock 156 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.7"}','{"text": "the_end"}','{"text": "cg_find"}','{"text": ""}']}}
setblock 157 64 414 minecraft:air
setblock 157 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde die"}','{"text": "Ruined Citadel"}','{"text": ""}','{"text": ""}']}}
setblock 157 64 406 minecraft:polished_andesite
summon item_frame 157 64 407 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"cataclysm:void_eye",count:1}}
setblock 166 64 414 minecraft:air
setblock 166 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.8"}','{"text": "the_end"}','{"text": "cg_kill"}','{"text": ""}']}}
setblock 167 64 414 minecraft:air
setblock 167 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Ender Guardian"}','{"text": ""}','{"text": ""}']}}
setblock 167 64 406 minecraft:polished_andesite
summon item_frame 167 64 407 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"cataclysm:gauntlet_of_guard",count:1}}
summon cataclysm:ender_guardian 168.5 64 409.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 176 64 414 minecraft:air
setblock 176 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.9"}','{"text": "the_end"}','{"text": "st_aviary"}','{"text": ""}']}}
setblock 177 64 414 minecraft:air
setblock 177 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde die"}','{"text": "Voliere"}','{"text": ""}','{"text": ""}']}}
setblock 177 64 406 minecraft:polished_andesite
summon item_frame 177 64 407 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:feather",count:1}}
setblock 186 64 414 minecraft:air
setblock 186 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.10"}','{"text": "the_end"}','{"text": "draconium"}','{"text": ""}']}}
setblock 187 64 414 minecraft:air
setblock 187 64 414 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "ab"}','{"text": ""}','{"text": ""}']}}
setblock 187 64 406 minecraft:polished_andesite
summon item_frame 187 64 407 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"draconicevolution:draconium_dust",count:1}}
setblock 189 64 406 minecraft:polished_andesite
summon item_frame 189 64 407 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"draconicevolution:draconium_ingot",count:1}}
