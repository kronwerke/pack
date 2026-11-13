# 078 storage/drawers_4, controller, vault_big
#area 23 212 63 237
fill 23 64 212 63 91 237 minecraft:air
fill 23 60 212 63 62 237 minecraft:stone
fill 23 63 212 63 63 237 minecraft:light_gray_concrete
fill 27 64 218 63 79 218 minecraft:light_gray_concrete
fill 27 64 218 27 79 231 minecraft:light_gray_concrete
setblock 28 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078.1"}','{"text": "storage"}','{"text": "drawers_4"}','{"text": ""}']}}
setblock 29 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Schubladenwand"}','{"text": ""}','{"text": ""}']}}
fill 37 64 218 37 79 231 minecraft:light_gray_concrete
fill 31 64 222 33 66 222 minecraft:oak_planks
kw testworld use 31 64 222 south functionalstorage:oak_4
execute unless block 31 64 223 minecraft:air
kw testworld use 31 64 223 south minecraft:iron_ingot
kw testworld use 32 64 222 south functionalstorage:oak_4
execute unless block 32 64 223 minecraft:air
kw testworld use 32 64 223 south minecraft:copper_ingot
kw testworld use 33 64 222 south functionalstorage:oak_4
execute unless block 33 64 223 minecraft:air
kw testworld use 33 64 223 south minecraft:gold_ingot
kw testworld use 31 65 222 south functionalstorage:oak_4
execute unless block 31 65 223 minecraft:air
kw testworld use 31 65 223 south minecraft:redstone
kw testworld use 32 65 222 south functionalstorage:oak_4
execute unless block 32 65 223 minecraft:air
kw testworld use 32 65 223 south minecraft:coal
kw testworld use 33 65 222 south functionalstorage:oak_4
execute unless block 33 65 223 minecraft:air
kw testworld use 33 65 223 south minecraft:lapis_lazuli
kw testworld use 31 66 222 south functionalstorage:oak_4
execute unless block 31 66 223 minecraft:air
kw testworld use 31 66 223 south minecraft:diamond
kw testworld use 32 66 222 south functionalstorage:oak_4
execute unless block 32 66 223 minecraft:air
kw testworld use 32 66 223 south minecraft:quartz
kw testworld use 33 66 222 south functionalstorage:oak_4
execute unless block 33 66 223 minecraft:air
kw testworld use 33 66 223 south minecraft:bone
setblock 38 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078.2"}','{"text": "storage"}','{"text": "controller"}','{"text": ""}']}}
setblock 39 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Lagerkern"}','{"text": ""}','{"text": ""}']}}
fill 47 64 218 47 79 231 minecraft:light_gray_concrete
setblock 42 64 223 sophisticatedstorage:controller
setblock 40 64 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 41 64 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 43 64 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 41 65 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 42 65 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 43 65 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 48 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078.3"}','{"text": "storage"}','{"text": "vault_big"}','{"text": ""}']}}
setblock 49 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "großen Tresor"}','{"text": ""}','{"text": ""}']}}
fill 58 64 218 58 79 231 minecraft:light_gray_concrete
fill 50 64 222 55 66 224 create:item_vault[axis=x,large=false]
