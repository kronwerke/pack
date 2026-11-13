# 110 occultism_afrit/storage
#area 199 180 222 209
fill 199 64 180 222 91 209 minecraft:air
fill 199 60 180 222 62 209 minecraft:stone
fill 199 63 180 222 63 209 minecraft:light_gray_concrete
fill 203 64 186 222 79 186 minecraft:light_gray_concrete
fill 203 64 186 203 79 203 minecraft:light_gray_concrete
setblock 204 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "110"}','{"text": "occultism_afrit"}','{"text": "storage"}','{"text": ""}']}}
setblock 205 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "storage"}','{"text": "actuator with"}','{"text": "four"}','{"text": "stabilizers"}']}}
fill 217 64 186 217 79 203 minecraft:light_gray_concrete
setblock 206 65 193 occultism:otherstone
setblock 207 65 193 occultism:storage_stabilizer_tier1[facing=east]
setblock 210 65 189 occultism:otherstone
setblock 210 65 190 occultism:storage_stabilizer_tier1[facing=south]
setblock 210 65 196 occultism:storage_stabilizer_tier1[facing=north]
setblock 210 65 197 occultism:otherstone
setblock 213 65 193 occultism:storage_stabilizer_tier1[facing=west]
setblock 214 65 193 occultism:otherstone
setblock 206 64 193 occultism:otherstone
setblock 210 64 189 occultism:otherstone
setblock 210 64 193 occultism:storage_controller
setblock 210 64 197 occultism:otherstone
setblock 214 64 193 occultism:otherstone
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
