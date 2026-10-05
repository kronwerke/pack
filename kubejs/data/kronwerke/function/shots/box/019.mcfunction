# 019 farms/s2_xp
fill 147 63 27 158 63 40 minecraft:light_gray_concrete
fill 147 64 27 158 71 27 minecraft:light_gray_concrete
fill 147 64 27 147 71 40 minecraft:light_gray_concrete
setblock 148 64 39 minecraft:air
setblock 148 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "019"}','{"text": "farms"}','{"text": "s2_xp"}','{"text": ""}']}}
setblock 149 64 39 minecraft:air
setblock 149 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "grindstone"}','{"text": "drain stack"}','{"text": "with experience"}','{"text": "hatch on a tank"}']}}
setblock 150 64 39 minecraft:air
setblock 150 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schleifstein-Abfluss"}','{"text": "auf den Tank"}','{"text": "setzen"}','{"text": ""}']}}
setblock 151 64 32 create:fluid_tank
setblock 151 65 32 create:fluid_tank
setblock 151 66 32 create_enchantment_industry:experience_hatch
setblock 153 64 32 create:millstone
setblock 155 64 35 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create_enchantment_industry:grindstone_drain",count:1},{Slot:1b,id:"create_enchantment_industry:experience_hatch",count:1}]}
