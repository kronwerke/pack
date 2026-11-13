# 070 storage/drawers_4, vault_big
#area -4 212 26 237
fill -4 64 212 26 91 237 minecraft:air
fill -4 60 212 26 62 237 minecraft:stone
fill -4 63 212 26 63 237 minecraft:light_gray_concrete
fill 0 64 218 26 79 218 minecraft:light_gray_concrete
fill 0 64 218 0 79 231 minecraft:light_gray_concrete
setblock 1 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070.1"}','{"text": "storage"}','{"text": "drawers_4"}','{"text": ""}']}}
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
setblock 11 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070.2"}','{"text": "storage"}','{"text": "vault_big"}','{"text": ""}']}}
setblock 12 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "großen Tresor"}','{"text": ""}','{"text": ""}']}}
fill 21 64 218 21 79 231 minecraft:light_gray_concrete
fill 13 64 222 18 66 224 create:item_vault[axis=x,large=false]
