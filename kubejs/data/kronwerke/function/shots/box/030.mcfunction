# 030 create/frogport
fill 168 63 48 183 63 61 minecraft:light_gray_concrete
fill 168 64 48 183 71 48 minecraft:light_gray_concrete
fill 168 64 48 168 71 61 minecraft:light_gray_concrete
setblock 169 64 60 minecraft:air
setblock 169 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030"}','{"text": "create"}','{"text": "frogport"}','{"text": ""}']}}
setblock 170 64 60 minecraft:air
setblock 170 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chain conveyor"}','{"text": "with a frogport"}','{"text": "carrying a"}','{"text": "package"}']}}
setblock 171 64 60 minecraft:air
setblock 171 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Kette zwischen"}','{"text": "den Förderern"}','{"text": "ziehen, Frosch"}','{"text": "anhängen"}']}}
setblock 171 64 53 create:shaft[axis=y]
setblock 171 65 53 create:chain_conveyor
setblock 179 64 53 create:shaft[axis=y]
setblock 179 65 53 create:chain_conveyor
setblock 173 64 55 create:package_frogport
setblock 181 64 57 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:chain",count:1},{Slot:1b,id:"create:package_frogport",count:1},{Slot:2b,id:"create:cardboard_block",count:1}]}
