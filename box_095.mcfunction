# 095 occultism_afrit/storage
#area 199 144 222 173
fill 199 64 144 222 91 173 minecraft:air
fill 199 60 144 222 62 173 minecraft:stone
fill 199 63 144 222 63 173 minecraft:light_gray_concrete
fill 203 64 150 222 79 150 minecraft:light_gray_concrete
fill 203 64 150 203 79 167 minecraft:light_gray_concrete
setblock 204 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095"}','{"text": "occultism_afrit"}','{"text": "storage"}','{"text": ""}']}}
setblock 205 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "storage"}','{"text": "actuator with"}','{"text": "four"}','{"text": "stabilizers"}']}}
fill 217 64 150 217 79 167 minecraft:light_gray_concrete
setblock 206 65 157 occultism:otherstone
setblock 207 65 157 occultism:storage_stabilizer_tier1[facing=east]
setblock 210 65 153 occultism:otherstone
setblock 210 65 154 occultism:storage_stabilizer_tier1[facing=south]
setblock 210 65 160 occultism:storage_stabilizer_tier1[facing=north]
setblock 210 65 161 occultism:otherstone
setblock 213 65 157 occultism:storage_stabilizer_tier1[facing=west]
setblock 214 65 157 occultism:otherstone
setblock 206 64 157 occultism:otherstone
setblock 210 64 153 occultism:otherstone
setblock 210 64 157 occultism:storage_controller
setblock 210 64 161 occultism:otherstone
setblock 214 64 157 occultism:otherstone
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
