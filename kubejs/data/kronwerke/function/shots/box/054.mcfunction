# 054 create_trains/cargo
fill 220 63 69 231 63 82 minecraft:light_gray_concrete
fill 220 64 69 231 71 69 minecraft:light_gray_concrete
fill 220 64 69 220 71 82 minecraft:light_gray_concrete
setblock 221 64 81 minecraft:air
setblock 221 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "create_trains"}','{"text": "cargo"}','{"text": ""}']}}
setblock 222 64 81 minecraft:air
setblock 222 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a portable"}','{"text": "storage"}','{"text": "interface pair"}','{"text": "at a platform"}']}}
fill 221 63 74 229 63 74 minecraft:gravel
fill 221 64 74 229 64 74 create:track[shape=xo]
setblock 225 64 76 create:portable_storage_interface[facing=north]
setblock 225 64 77 minecraft:chest
