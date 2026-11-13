# 065 occultism_afrit/storage
#area 137 142 160 171
fill 137 64 142 160 91 171 minecraft:air
fill 137 60 142 160 62 171 minecraft:stone
fill 137 63 142 160 63 171 minecraft:light_gray_concrete
fill 141 64 148 160 79 148 minecraft:light_gray_concrete
fill 141 64 148 141 79 165 minecraft:light_gray_concrete
setblock 142 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "065"}','{"text": "occultism_afrit"}','{"text": "storage"}','{"text": ""}']}}
setblock 143 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "storage"}','{"text": "actuator with"}','{"text": "four"}','{"text": "stabilizers"}']}}
fill 155 64 148 155 79 165 minecraft:light_gray_concrete
setblock 144 65 155 occultism:otherstone
setblock 145 65 155 occultism:storage_stabilizer_tier1[facing=east]
setblock 148 65 151 occultism:otherstone
setblock 148 65 152 occultism:storage_stabilizer_tier1[facing=south]
setblock 148 65 158 occultism:storage_stabilizer_tier1[facing=north]
setblock 148 65 159 occultism:otherstone
setblock 151 65 155 occultism:storage_stabilizer_tier1[facing=west]
setblock 152 65 155 occultism:otherstone
setblock 144 64 155 occultism:otherstone
setblock 148 64 151 occultism:otherstone
setblock 148 64 155 occultism:storage_controller
setblock 148 64 159 occultism:otherstone
setblock 152 64 155 occultism:otherstone
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
