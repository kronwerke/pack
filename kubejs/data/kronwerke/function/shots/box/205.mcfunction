# 205 the_end/arrival, crystals, dragon, egg, respawn, elytra, cg_find, cg_kill, st_aviary, draconium
fill 95 63 420 196 63 433 minecraft:light_gray_concrete
fill 95 64 420 196 71 420 minecraft:light_gray_concrete
fill 95 64 420 95 71 433 minecraft:light_gray_concrete
setblock 96 64 432 minecraft:air
setblock 96 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.1"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 97 64 432 minecraft:air
setblock 97 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Aufnahme in the"}','{"text": "end"}','{"text": ""}','{"text": ""}']}}
summon text_display 100.5 71 425.5 {text:'[{"text": "205.1  ", "color": "gold"}, {"text": "the_end/arrival", "color": "gray"}, {"text": "\\nBetritt das End", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 97 63 422 103 63 425 minecraft:polished_deepslate
fill 97 64 422 103 67 422 minecraft:deepslate_tiles
fill 97 64 422 103 64 422 minecraft:polished_blackstone
fill 97 67 422 103 67 422 minecraft:polished_blackstone
setblock 97 64 425 minecraft:lantern
setblock 103 64 425 minecraft:lantern
setblock 99 64 424 minecraft:end_stone
setblock 106 64 432 minecraft:air
setblock 106 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.2"}','{"text": "the_end"}','{"text": "crystals"}','{"text": ""}']}}
setblock 107 64 432 minecraft:air
setblock 107 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zerstör die"}','{"text": "Endkristalle"}','{"text": ""}','{"text": ""}']}}
summon text_display 110.5 71 425.5 {text:'[{"text": "205.2  ", "color": "gold"}, {"text": "the_end/crystals", "color": "gray"}, {"text": "\\nZerstör die Endkristalle", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 107 63 422 113 63 425 minecraft:polished_deepslate
fill 107 64 422 113 67 422 minecraft:deepslate_tiles
fill 107 64 422 113 64 422 minecraft:polished_blackstone
fill 107 67 422 113 67 422 minecraft:polished_blackstone
setblock 107 64 425 minecraft:lantern
setblock 113 64 425 minecraft:lantern
summon glow_item_frame 109 66 423 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:end_crystal",count:1}}
setblock 116 64 432 minecraft:air
setblock 116 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.3"}','{"text": "the_end"}','{"text": "dragon"}','{"text": ""}']}}
setblock 117 64 432 minecraft:air
setblock 117 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Enderdrachen"}','{"text": ""}','{"text": ""}']}}
summon text_display 120.5 71 425.5 {text:'[{"text": "205.3  ", "color": "gold"}, {"text": "the_end/dragon", "color": "gray"}, {"text": "\\nBesiege den Enderdrachen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 117 63 422 123 63 425 minecraft:polished_deepslate
fill 117 64 422 123 67 422 minecraft:deepslate_tiles
fill 117 64 422 123 64 422 minecraft:polished_blackstone
fill 117 67 422 123 67 422 minecraft:polished_blackstone
setblock 117 64 425 minecraft:lantern
setblock 123 64 425 minecraft:lantern
setblock 119 64 424 minecraft:dragon_head
setblock 126 64 432 minecraft:air
setblock 126 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.4"}','{"text": "the_end"}','{"text": "egg"}','{"text": ""}']}}
setblock 127 64 432 minecraft:air
setblock 127 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol das"}','{"text": "Drachenei"}','{"text": ""}','{"text": ""}']}}
summon text_display 130.5 71 425.5 {text:'[{"text": "205.4  ", "color": "gold"}, {"text": "the_end/egg", "color": "gray"}, {"text": "\\nHol das Drachenei", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 128 64 423 132 64 427 minecraft:bedrock
setblock 130 65 425 minecraft:dragon_egg
setblock 130 64 422 minecraft:obsidian
setblock 130 65 422 minecraft:bedrock
summon minecraft:end_crystal 130.5 66 422.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
setblock 130 64 428 minecraft:obsidian
setblock 130 65 428 minecraft:bedrock
summon minecraft:end_crystal 130.5 66 428.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
setblock 127 64 425 minecraft:obsidian
setblock 127 65 425 minecraft:bedrock
summon minecraft:end_crystal 127.5 66 425.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
setblock 133 64 425 minecraft:obsidian
setblock 133 65 425 minecraft:bedrock
summon minecraft:end_crystal 133.5 66 425.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
setblock 136 64 432 minecraft:air
setblock 136 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.5"}','{"text": "the_end"}','{"text": "respawn"}','{"text": ""}']}}
setblock 137 64 432 minecraft:air
setblock 137 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Beschwör den"}','{"text": "Drachen neu"}','{"text": ""}','{"text": ""}']}}
summon text_display 140.5 71 425.5 {text:'[{"text": "205.5  ", "color": "gold"}, {"text": "the_end/respawn", "color": "gray"}, {"text": "\\nBeschwör den Drachen neu", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 138 64 423 142 64 427 minecraft:bedrock
setblock 140 65 425 minecraft:dragon_egg
setblock 140 64 422 minecraft:obsidian
setblock 140 65 422 minecraft:bedrock
summon minecraft:end_crystal 140.5 66 422.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
setblock 140 64 428 minecraft:obsidian
setblock 140 65 428 minecraft:bedrock
summon minecraft:end_crystal 140.5 66 428.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
setblock 137 64 425 minecraft:obsidian
setblock 137 65 425 minecraft:bedrock
summon minecraft:end_crystal 137.5 66 425.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
setblock 143 64 425 minecraft:obsidian
setblock 143 65 425 minecraft:bedrock
summon minecraft:end_crystal 143.5 66 425.5 {PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f],ShowBottom:0b}
setblock 146 64 432 minecraft:air
setblock 146 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.6"}','{"text": "the_end"}','{"text": "elytra"}','{"text": ""}']}}
setblock 147 64 432 minecraft:air
setblock 147 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mit Elytra"}','{"text": "fliegen"}','{"text": ""}','{"text": ""}']}}
summon text_display 150.5 71 425.5 {text:'[{"text": "205.6  ", "color": "gold"}, {"text": "the_end/elytra", "color": "gray"}, {"text": "\\nHol dir Elytren", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 154 64 429 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:elytra",count:1}]}
setblock 156 64 432 minecraft:air
setblock 156 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.7"}','{"text": "the_end"}','{"text": "cg_find"}','{"text": ""}']}}
setblock 157 64 432 minecraft:air
setblock 157 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde die"}','{"text": "Ruined Citadel"}','{"text": ""}','{"text": ""}']}}
summon text_display 160.5 71 425.5 {text:'[{"text": "205.7  ", "color": "gold"}, {"text": "the_end/cg_find", "color": "gray"}, {"text": "\\nFinde die Ruined Citadel", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 157 63 422 163 63 425 minecraft:polished_deepslate
fill 157 64 422 163 67 422 minecraft:deepslate_tiles
fill 157 64 422 163 64 422 minecraft:polished_blackstone
fill 157 67 422 163 67 422 minecraft:polished_blackstone
setblock 157 64 425 minecraft:lantern
setblock 163 64 425 minecraft:lantern
summon glow_item_frame 159 66 423 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"cataclysm:void_eye",count:1}}
setblock 166 64 432 minecraft:air
setblock 166 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.8"}','{"text": "the_end"}','{"text": "cg_kill"}','{"text": ""}']}}
setblock 167 64 432 minecraft:air
setblock 167 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Ender Guardian"}','{"text": ""}','{"text": ""}']}}
summon text_display 170.5 71 425.5 {text:'[{"text": "205.8  ", "color": "gold"}, {"text": "the_end/cg_kill", "color": "gray"}, {"text": "\\nBesiege den Ender Guardian", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 167 63 422 173 63 425 minecraft:polished_deepslate
fill 167 64 422 173 67 422 minecraft:deepslate_tiles
fill 167 64 422 173 64 422 minecraft:polished_blackstone
fill 167 67 422 173 67 422 minecraft:polished_blackstone
setblock 167 64 425 minecraft:lantern
setblock 173 64 425 minecraft:lantern
summon glow_item_frame 169 66 423 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"cataclysm:gauntlet_of_guard",count:1}}
summon cataclysm:ender_guardian 168.5 64 427.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 176 64 432 minecraft:air
setblock 176 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.9"}','{"text": "the_end"}','{"text": "st_aviary"}','{"text": ""}']}}
setblock 177 64 432 minecraft:air
setblock 177 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde die"}','{"text": "Voliere"}','{"text": ""}','{"text": ""}']}}
summon text_display 180.5 71 425.5 {text:'[{"text": "205.9  ", "color": "gold"}, {"text": "the_end/st_aviary", "color": "gray"}, {"text": "\\nFinde die Voliere", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 177 63 422 183 63 425 minecraft:polished_deepslate
fill 177 64 422 183 67 422 minecraft:deepslate_tiles
fill 177 64 422 183 64 422 minecraft:polished_blackstone
fill 177 67 422 183 67 422 minecraft:polished_blackstone
setblock 177 64 425 minecraft:lantern
setblock 183 64 425 minecraft:lantern
summon glow_item_frame 179 66 423 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:feather",count:1}}
setblock 186 64 432 minecraft:air
setblock 186 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "205.10"}','{"text": "the_end"}','{"text": "draconium"}','{"text": ""}']}}
setblock 187 64 432 minecraft:air
setblock 187 64 432 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "ab"}','{"text": ""}','{"text": ""}']}}
summon text_display 190.5 71 425.5 {text:'[{"text": "205.10  ", "color": "gold"}, {"text": "the_end/draconium", "color": "gray"}, {"text": "\\nBau Draconium ab", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 187 63 422 193 63 425 minecraft:polished_deepslate
fill 187 64 422 193 67 422 minecraft:deepslate_tiles
fill 187 64 422 193 64 422 minecraft:polished_blackstone
fill 187 67 422 193 67 422 minecraft:polished_blackstone
setblock 187 64 425 minecraft:lantern
setblock 193 64 425 minecraft:lantern
summon glow_item_frame 188 66 423 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"draconicevolution:draconium_dust",count:1}}
summon glow_item_frame 190 66 423 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"draconicevolution:draconium_ingot",count:1}}
