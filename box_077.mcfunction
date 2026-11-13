# 077 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 187 177 346 218
fill 187 64 177 204 106 218 minecraft:air
fill 205 64 177 222 106 218 minecraft:air
fill 223 64 177 240 106 218 minecraft:air
fill 241 64 177 258 106 218 minecraft:air
fill 259 64 177 276 106 218 minecraft:air
fill 277 64 177 294 106 218 minecraft:air
fill 295 64 177 312 106 218 minecraft:air
fill 313 64 177 330 106 218 minecraft:air
fill 331 64 177 346 106 218 minecraft:air
fill 187 60 177 346 62 218 minecraft:stone
fill 187 63 177 346 63 218 minecraft:light_gray_concrete
fill 191 64 183 346 94 183 minecraft:light_gray_concrete
fill 191 64 183 191 94 212 minecraft:light_gray_concrete
setblock 192 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 193 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 201 64 183 201 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 194 64 186 none
kw testworld use 196 65 188 south immersiveengineering:hammer
execute unless block 196 65 188 immersiveengineering:steel_fence
setblock 202 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 203 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 211 64 183 211 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 205 64 186 none
kw testworld use 206 65 186 south immersiveengineering:hammer
execute unless block 206 65 186 minecraft:piston
setblock 212 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 213 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 221 64 183 221 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 215 64 186 none
kw testworld use 216 65 187 south immersiveengineering:hammer
execute unless block 216 65 187 immersiveengineering:wooden_barrel
setblock 222 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 223 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 231 64 183 231 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 225 64 186 none
kw testworld use 226 65 187 south immersiveengineering:hammer
execute unless block 226 65 187 minecraft:cauldron
setblock 232 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 233 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 241 64 183 241 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 235 64 186 none
kw testworld use 236 65 187 south immersiveengineering:hammer
execute unless block 236 65 187 immersiveengineering:sheetmetal_iron
setblock 242 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 243 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 251 64 183 251 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 245 64 186 none
kw testworld use 246 65 187 south immersiveengineering:hammer
execute unless block 246 65 187 immersiveengineering:conveyor_basic
setblock 252 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 253 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 261 64 183 261 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 254 64 186 none
kw testworld use 256 64 190 south immersiveengineering:hammer
execute unless block 256 64 190 minecraft:cauldron
setblock 262 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 263 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 271 64 183 271 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 264 64 186 none
kw testworld use 266 65 188 south immersiveengineering:hammer
execute unless block 266 65 188 immersiveengineering:heavy_engineering
setblock 272 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 273 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 281 64 183 281 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 275 64 186 none
kw testworld use 276 65 190 south immersiveengineering:hammer
execute unless block 276 65 190 immersiveengineering:generator
setblock 282 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 283 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 291 64 183 291 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 284 64 186 none
kw testworld use 286 64 188 south immersiveengineering:hammer
execute unless block 286 64 188 immersiveengineering:sheetmetal_iron
setblock 292 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 293 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 301 64 183 301 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 295 64 186 none
kw testworld use 296 65 188 south immersiveengineering:hammer
execute unless block 296 65 188 immersiveengineering:conveyor_basic
setblock 302 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 303 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 311 64 183 311 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 305 64 186 none
kw testworld use 306 65 188 south immersiveengineering:hammer
execute unless block 306 65 188 immersiveengineering:slab_treated_wood_horizontal
setblock 312 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 313 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 321 64 183 321 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 315 64 186 none
kw testworld use 316 65 191 south immersiveengineering:hammer
execute unless block 316 65 191 immersiveengineering:heavy_engineering
setblock 322 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 323 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 331 64 183 331 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 325 64 186 none
kw testworld use 326 65 188 south immersiveengineering:hammer
execute unless block 326 65 188 immersiveengineering:light_engineering
setblock 332 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 333 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 341 64 183 341 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 334 64 186 none
kw testworld use 336 65 191 south immersiveengineering:hammer
execute unless block 336 65 191 immersiveengineering:rs_engineering
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
