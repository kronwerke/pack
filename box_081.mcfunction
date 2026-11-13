# 081 storage/drawers_4, controller, vault_big
#area 23 231 63 256
fill 23 64 231 63 91 256 minecraft:air
fill 23 60 231 63 62 256 minecraft:stone
fill 23 63 231 63 63 256 minecraft:light_gray_concrete
fill 27 64 237 63 79 237 minecraft:light_gray_concrete
fill 27 64 237 27 79 250 minecraft:light_gray_concrete
setblock 28 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.1"}','{"text": "storage"}','{"text": "drawers_4"}','{"text": ""}']}}
setblock 29 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Schubladenwand"}','{"text": ""}','{"text": ""}']}}
fill 37 64 237 37 79 250 minecraft:light_gray_concrete
fill 31 64 241 33 66 241 minecraft:oak_planks
kw testworld use 31 64 241 south functionalstorage:oak_4
execute unless block 31 64 242 minecraft:air
kw testworld use 31 64 242 south minecraft:iron_ingot
kw testworld use 32 64 241 south functionalstorage:oak_4
execute unless block 32 64 242 minecraft:air
kw testworld use 32 64 242 south minecraft:copper_ingot
kw testworld use 33 64 241 south functionalstorage:oak_4
execute unless block 33 64 242 minecraft:air
kw testworld use 33 64 242 south minecraft:gold_ingot
kw testworld use 31 65 241 south functionalstorage:oak_4
execute unless block 31 65 242 minecraft:air
kw testworld use 31 65 242 south minecraft:redstone
kw testworld use 32 65 241 south functionalstorage:oak_4
execute unless block 32 65 242 minecraft:air
kw testworld use 32 65 242 south minecraft:coal
kw testworld use 33 65 241 south functionalstorage:oak_4
execute unless block 33 65 242 minecraft:air
kw testworld use 33 65 242 south minecraft:lapis_lazuli
kw testworld use 31 66 241 south functionalstorage:oak_4
execute unless block 31 66 242 minecraft:air
kw testworld use 31 66 242 south minecraft:diamond
kw testworld use 32 66 241 south functionalstorage:oak_4
execute unless block 32 66 242 minecraft:air
kw testworld use 32 66 242 south minecraft:quartz
kw testworld use 33 66 241 south functionalstorage:oak_4
execute unless block 33 66 242 minecraft:air
kw testworld use 33 66 242 south minecraft:bone
setblock 38 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.2"}','{"text": "storage"}','{"text": "controller"}','{"text": ""}']}}
setblock 39 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Lagerkern"}','{"text": ""}','{"text": ""}']}}
fill 47 64 237 47 79 250 minecraft:light_gray_concrete
setblock 42 64 242 sophisticatedstorage:controller
setblock 40 64 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 41 64 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 43 64 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 41 65 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 42 65 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 43 65 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 48 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.3"}','{"text": "storage"}','{"text": "vault_big"}','{"text": ""}']}}
setblock 49 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "großen Tresor"}','{"text": ""}','{"text": ""}']}}
fill 58 64 237 58 79 250 minecraft:light_gray_concrete
fill 50 64 241 55 66 243 create:item_vault[axis=x,large=false]
