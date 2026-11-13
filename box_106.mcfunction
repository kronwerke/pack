# 106 occultism_afrit/storage
#area 199 176 222 205
fill 199 64 176 222 91 205 minecraft:air
fill 199 60 176 222 62 205 minecraft:stone
fill 199 63 176 222 63 205 minecraft:light_gray_concrete
fill 203 64 182 222 79 182 minecraft:light_gray_concrete
fill 203 64 182 203 79 199 minecraft:light_gray_concrete
setblock 204 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106"}','{"text": "occultism_afrit"}','{"text": "storage"}','{"text": ""}']}}
setblock 205 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "storage"}','{"text": "actuator with"}','{"text": "four"}','{"text": "stabilizers"}']}}
fill 217 64 182 217 79 199 minecraft:light_gray_concrete
setblock 206 65 189 occultism:otherstone
setblock 207 65 189 occultism:storage_stabilizer_tier1[facing=east]
setblock 210 65 185 occultism:otherstone
setblock 210 65 186 occultism:storage_stabilizer_tier1[facing=south]
setblock 210 65 192 occultism:storage_stabilizer_tier1[facing=north]
setblock 210 65 193 occultism:otherstone
setblock 213 65 189 occultism:storage_stabilizer_tier1[facing=west]
setblock 214 65 189 occultism:otherstone
setblock 206 64 189 occultism:otherstone
setblock 210 64 185 occultism:otherstone
setblock 210 64 189 occultism:storage_controller
setblock 210 64 193 occultism:otherstone
setblock 214 64 189 occultism:otherstone
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
