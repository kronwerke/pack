# 125 occultism_afrit/storage
#area 214 184 237 213
fill 214 64 184 237 91 213 minecraft:air
fill 214 60 184 237 62 213 minecraft:stone
fill 214 63 184 237 63 213 minecraft:light_gray_concrete
fill 218 64 190 237 79 190 minecraft:light_gray_concrete
fill 218 64 190 218 79 207 minecraft:light_gray_concrete
setblock 219 64 206 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125"}','{"text": "occultism_afrit"}','{"text": "storage"}','{"text": ""}']}}
setblock 220 64 206 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "storage"}','{"text": "actuator with"}','{"text": "four"}','{"text": "stabilizers"}']}}
fill 232 64 190 232 79 207 minecraft:light_gray_concrete
setblock 221 65 197 occultism:otherstone
setblock 222 65 197 occultism:storage_stabilizer_tier1[facing=east]
setblock 225 65 193 occultism:otherstone
setblock 225 65 194 occultism:storage_stabilizer_tier1[facing=south]
setblock 225 65 200 occultism:storage_stabilizer_tier1[facing=north]
setblock 225 65 201 occultism:otherstone
setblock 228 65 197 occultism:storage_stabilizer_tier1[facing=west]
setblock 229 65 197 occultism:otherstone
setblock 221 64 197 occultism:otherstone
setblock 225 64 193 occultism:otherstone
setblock 225 64 197 occultism:storage_controller
setblock 225 64 201 occultism:otherstone
setblock 229 64 197 occultism:otherstone
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
