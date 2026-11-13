# 110 occultism_afrit/storage
#area 199 182 222 211
fill 199 64 182 222 91 211 minecraft:air
fill 199 60 182 222 62 211 minecraft:stone
fill 199 63 182 222 63 211 minecraft:light_gray_concrete
fill 203 64 188 222 79 188 minecraft:light_gray_concrete
fill 203 64 188 203 79 205 minecraft:light_gray_concrete
setblock 204 64 204 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "110"}','{"text": "occultism_afrit"}','{"text": "storage"}','{"text": ""}']}}
setblock 205 64 204 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "storage"}','{"text": "actuator with"}','{"text": "four"}','{"text": "stabilizers"}']}}
fill 217 64 188 217 79 205 minecraft:light_gray_concrete
setblock 206 65 195 occultism:otherstone
setblock 207 65 195 occultism:storage_stabilizer_tier1[facing=east]
setblock 210 65 191 occultism:otherstone
setblock 210 65 192 occultism:storage_stabilizer_tier1[facing=south]
setblock 210 65 198 occultism:storage_stabilizer_tier1[facing=north]
setblock 210 65 199 occultism:otherstone
setblock 213 65 195 occultism:storage_stabilizer_tier1[facing=west]
setblock 214 65 195 occultism:otherstone
setblock 206 64 195 occultism:otherstone
setblock 210 64 191 occultism:otherstone
setblock 210 64 195 occultism:storage_controller
setblock 210 64 199 occultism:otherstone
setblock 214 64 195 occultism:otherstone
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
