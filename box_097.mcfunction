# 097 occultism_afrit/storage
#area 199 146 222 175
fill 199 64 146 222 91 175 minecraft:air
fill 199 60 146 222 62 175 minecraft:stone
fill 199 63 146 222 63 175 minecraft:light_gray_concrete
fill 203 64 152 222 79 152 minecraft:light_gray_concrete
fill 203 64 152 203 79 169 minecraft:light_gray_concrete
setblock 204 64 168 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097"}','{"text": "occultism_afrit"}','{"text": "storage"}','{"text": ""}']}}
setblock 205 64 168 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "storage"}','{"text": "actuator with"}','{"text": "four"}','{"text": "stabilizers"}']}}
fill 217 64 152 217 79 169 minecraft:light_gray_concrete
setblock 206 65 159 occultism:otherstone
setblock 207 65 159 occultism:storage_stabilizer_tier1[facing=east]
setblock 210 65 155 occultism:otherstone
setblock 210 65 156 occultism:storage_stabilizer_tier1[facing=south]
setblock 210 65 162 occultism:storage_stabilizer_tier1[facing=north]
setblock 210 65 163 occultism:otherstone
setblock 213 65 159 occultism:storage_stabilizer_tier1[facing=west]
setblock 214 65 159 occultism:otherstone
setblock 206 64 159 occultism:otherstone
setblock 210 64 155 occultism:otherstone
setblock 210 64 159 occultism:storage_controller
setblock 210 64 163 occultism:otherstone
setblock 214 64 159 occultism:otherstone
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
