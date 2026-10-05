# 056 create_trains/obelisk_line
fill 250 63 69 265 63 84 minecraft:light_gray_concrete
fill 250 64 69 265 71 69 minecraft:light_gray_concrete
fill 250 64 69 250 71 84 minecraft:light_gray_concrete
setblock 251 64 83 minecraft:air
setblock 251 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "056"}','{"text": "create_trains"}','{"text": "obelisk_line"}','{"text": ""}']}}
setblock 252 64 83 minecraft:air
setblock 252 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spawn station"}','{"text": "unloading into"}','{"text": "the obelisk"}','{"text": "feeder"}']}}
fill 253 64 72 257 64 76 minecraft:polished_deepslate
setblock 255 65 74 kronwerke:obelisk
setblock 255 64 77 kronwerke:obelisk_intake
fill 251 63 78 263 63 78 minecraft:gravel
fill 251 64 78 263 64 78 create:track[shape=xo]
setblock 259 64 77 create:track_station
setblock 257 64 77 create:portable_storage_interface[facing=west]
