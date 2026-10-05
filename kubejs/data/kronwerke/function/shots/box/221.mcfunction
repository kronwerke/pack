# 221 theurgy/sal_tank, liquefaction, vessels, wire, array, fermentation
fill 160 63 492 221 63 505 minecraft:light_gray_concrete
fill 160 64 492 221 71 492 minecraft:light_gray_concrete
fill 160 64 492 160 71 505 minecraft:light_gray_concrete
setblock 161 64 504 minecraft:air
setblock 161 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "221.1"}','{"text": "theurgy"}','{"text": "sal_tank"}','{"text": ""}']}}
setblock 162 64 504 minecraft:air
setblock 162 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell Tank und"}','{"text": "Akkumulator auf"}','{"text": ""}','{"text": ""}']}}
setblock 162 64 496 theurgy:sal_ammoniac_tank
setblock 164 64 496 theurgy:sal_ammoniac_accumulator
setblock 171 64 504 minecraft:air
setblock 171 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "221.2"}','{"text": "theurgy"}','{"text": "liquefaction"}','{"text": ""}']}}
setblock 172 64 504 minecraft:air
setblock 172 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Löse Sulfur aus"}','{"text": "Raw Iron"}','{"text": ""}','{"text": ""}']}}
setblock 172 64 496 theurgy:liquefaction_cauldron
setblock 174 64 496 minecraft:polished_andesite
summon item_frame 174 64 497 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"theurgy:alchemical_sulfur_iron",count:1}}
setblock 181 64 504 minecraft:air
setblock 181 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "221.3"}','{"text": "theurgy"}','{"text": "vessels"}','{"text": ""}']}}
setblock 182 64 504 minecraft:air
setblock 182 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die drei"}','{"text": "Gefäße auf"}','{"text": ""}','{"text": ""}']}}
setblock 182 64 496 theurgy:incubator_salt_vessel
setblock 184 64 496 theurgy:incubator_sulfur_vessel
setblock 186 64 496 theurgy:incubator_mercury_vessel
setblock 191 64 504 minecraft:air
setblock 191 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "221.4"}','{"text": "theurgy"}','{"text": "wire"}','{"text": ""}']}}
setblock 192 64 504 minecraft:air
setblock 192 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde sie"}','{"text": "mit Kupferdraht"}','{"text": ""}','{"text": ""}']}}
setblock 192 64 496 minecraft:polished_andesite
summon item_frame 192 64 497 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"theurgy:copper_wire",count:1}}
setblock 201 64 504 minecraft:air
setblock 201 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "221.5"}','{"text": "theurgy"}','{"text": "array"}','{"text": ""}']}}
setblock 202 64 504 minecraft:air
setblock 202 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell drei"}','{"text": "Pedestale auf"}','{"text": ""}','{"text": ""}']}}
setblock 205 64 497 theurgy:incubator
setblock 205 64 495 theurgy:incubator_mercury_vessel
setblock 203 64 497 theurgy:incubator_mercury_vessel
setblock 207 64 497 theurgy:incubator_mercury_vessel
setblock 205 64 499 theurgy:incubator_mercury_vessel
setblock 211 64 504 minecraft:air
setblock 211 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "221.6"}','{"text": "theurgy"}','{"text": "fermentation"}','{"text": ""}']}}
setblock 212 64 504 minecraft:air
setblock 212 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Vergär Sulfur"}','{"text": "zu Niter"}','{"text": ""}','{"text": ""}']}}
setblock 212 64 496 theurgy:fermentation_vat
setblock 214 64 496 minecraft:polished_andesite
summon item_frame 214 64 497 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"theurgy:alchemical_niter_gems_common",count:1}}
