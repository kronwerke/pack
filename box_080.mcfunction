# 080 occultism_afrit/storage
#area 137 144 160 173
fill 137 64 144 160 91 173 minecraft:air
fill 137 60 144 160 62 173 minecraft:stone
fill 137 63 144 160 63 173 minecraft:light_gray_concrete
fill 141 64 150 160 79 150 minecraft:light_gray_concrete
fill 141 64 150 141 79 167 minecraft:light_gray_concrete
setblock 142 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080"}','{"text": "occultism_afrit"}','{"text": "storage"}','{"text": ""}']}}
setblock 143 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "storage"}','{"text": "actuator with"}','{"text": "four"}','{"text": "stabilizers"}']}}
fill 155 64 150 155 79 167 minecraft:light_gray_concrete
setblock 144 65 157 occultism:otherstone
setblock 145 65 157 occultism:storage_stabilizer_tier1[facing=east]
setblock 148 65 153 occultism:otherstone
setblock 148 65 154 occultism:storage_stabilizer_tier1[facing=south]
setblock 148 65 160 occultism:storage_stabilizer_tier1[facing=north]
setblock 148 65 161 occultism:otherstone
setblock 151 65 157 occultism:storage_stabilizer_tier1[facing=west]
setblock 152 65 157 occultism:otherstone
setblock 144 64 157 occultism:otherstone
setblock 148 64 153 occultism:otherstone
setblock 148 64 157 occultism:storage_controller
setblock 148 64 161 occultism:otherstone
setblock 152 64 157 occultism:otherstone
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
