# 201 pneumaticcraft/chamber, refinery, vortex, elevator, safety, plastic, etching
fill 227 63 358 298 63 371 minecraft:light_gray_concrete
fill 227 64 358 298 71 358 minecraft:light_gray_concrete
fill 227 64 358 227 71 371 minecraft:light_gray_concrete
setblock 228 64 370 minecraft:air
setblock 228 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "201.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 229 64 370 minecraft:air
setblock 229 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
setblock 229 64 362 pneumaticcraft:pressure_chamber_wall
setblock 238 64 370 minecraft:air
setblock 238 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "201.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 239 64 370 minecraft:air
setblock 239 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
setblock 239 64 362 pneumaticcraft:refinery
setblock 241 64 362 pneumaticcraft:refinery_output
setblock 248 64 370 minecraft:air
setblock 248 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "201.3"}','{"text": "pneumaticcraft"}','{"text": "vortex"}','{"text": ""}']}}
setblock 249 64 370 minecraft:air
setblock 249 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wirbelrohr"}','{"text": ""}','{"text": ""}']}}
setblock 249 64 362 pneumaticcraft:vortex_tube
setblock 258 64 370 minecraft:air
setblock 258 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "201.4"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 259 64 370 minecraft:air
setblock 259 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
setblock 259 64 362 pneumaticcraft:elevator_base
setblock 261 64 362 pneumaticcraft:elevator_frame
setblock 263 64 362 pneumaticcraft:elevator_caller
setblock 268 64 370 minecraft:air
setblock 268 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "201.5"}','{"text": "pneumaticcraft"}','{"text": "safety"}','{"text": ""}']}}
setblock 269 64 370 minecraft:air
setblock 269 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein"}','{"text": "Sicherheitsventil"}','{"text": ""}','{"text": ""}']}}
setblock 269 64 362 minecraft:polished_andesite
summon item_frame 269 64 363 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"pneumaticcraft:safety_tube_module",count:1}}
setblock 271 64 362 minecraft:polished_andesite
summon item_frame 271 64 363 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"pneumaticcraft:pressure_gauge_module",count:1}}
setblock 278 64 370 minecraft:air
setblock 278 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "201.6"}','{"text": "pneumaticcraft"}','{"text": "plastic"}','{"text": ""}']}}
setblock 279 64 370 minecraft:air
setblock 279 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Koch Kunststoff"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
setblock 279 64 362 pneumaticcraft:plastic
setblock 288 64 370 minecraft:air
setblock 288 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "201.7"}','{"text": "pneumaticcraft"}','{"text": "etching"}','{"text": ""}']}}
setblock 289 64 370 minecraft:air
setblock 289 64 370 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ätze die"}','{"text": "Platine"}','{"text": ""}','{"text": ""}']}}
setblock 289 64 362 pneumaticcraft:etching_tank
setblock 291 64 362 minecraft:polished_andesite
summon item_frame 291 64 363 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"pneumaticcraft:unassembled_pcb",count:1}}
