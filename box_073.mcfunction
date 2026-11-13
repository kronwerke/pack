# 073 storage/drawers_4, controller, vault_big
#area -4 212 36 237
fill -4 64 212 36 91 237 minecraft:air
fill -4 60 212 36 62 237 minecraft:stone
fill -4 63 212 36 63 237 minecraft:light_gray_concrete
fill 0 64 218 36 79 218 minecraft:light_gray_concrete
fill 0 64 218 0 79 231 minecraft:light_gray_concrete
setblock 1 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073.1"}','{"text": "storage"}','{"text": "drawers_4"}','{"text": ""}']}}
setblock 2 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Schubladenwand"}','{"text": ""}','{"text": ""}']}}
fill 10 64 218 10 79 231 minecraft:light_gray_concrete
fill 4 64 222 6 66 222 minecraft:oak_planks
kw testworld use 4 64 222 south functionalstorage:oak_4
execute unless block 4 64 223 minecraft:air
kw testworld use 4 64 223 south minecraft:iron_ingot
kw testworld use 5 64 222 south functionalstorage:oak_4
execute unless block 5 64 223 minecraft:air
kw testworld use 5 64 223 south minecraft:copper_ingot
kw testworld use 6 64 222 south functionalstorage:oak_4
execute unless block 6 64 223 minecraft:air
kw testworld use 6 64 223 south minecraft:gold_ingot
kw testworld use 4 65 222 south functionalstorage:oak_4
execute unless block 4 65 223 minecraft:air
kw testworld use 4 65 223 south minecraft:redstone
kw testworld use 5 65 222 south functionalstorage:oak_4
execute unless block 5 65 223 minecraft:air
kw testworld use 5 65 223 south minecraft:coal
kw testworld use 6 65 222 south functionalstorage:oak_4
execute unless block 6 65 223 minecraft:air
kw testworld use 6 65 223 south minecraft:lapis_lazuli
kw testworld use 4 66 222 south functionalstorage:oak_4
execute unless block 4 66 223 minecraft:air
kw testworld use 4 66 223 south minecraft:diamond
kw testworld use 5 66 222 south functionalstorage:oak_4
execute unless block 5 66 223 minecraft:air
kw testworld use 5 66 223 south minecraft:quartz
kw testworld use 6 66 222 south functionalstorage:oak_4
execute unless block 6 66 223 minecraft:air
kw testworld use 6 66 223 south minecraft:bone
setblock 11 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073.2"}','{"text": "storage"}','{"text": "controller"}','{"text": ""}']}}
setblock 12 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Lagerkern"}','{"text": ""}','{"text": ""}']}}
fill 20 64 218 20 79 231 minecraft:light_gray_concrete
setblock 15 64 223 sophisticatedstorage:controller
setblock 13 64 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 14 64 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 16 64 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 14 65 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 15 65 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 16 65 223 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 21 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073.3"}','{"text": "storage"}','{"text": "vault_big"}','{"text": ""}']}}
setblock 22 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "großen Tresor"}','{"text": ""}','{"text": ""}']}}
fill 31 64 218 31 79 231 minecraft:light_gray_concrete
fill 23 64 222 28 66 224 create:item_vault[axis=x,large=false]
