# 100 occultism/aviar
#area 11 180 34 209
fill 11 64 180 34 91 209 minecraft:air
fill 11 60 180 34 62 209 minecraft:stone
fill 11 63 180 34 63 209 minecraft:light_gray_concrete
fill 15 64 186 34 79 186 minecraft:light_gray_concrete
fill 15 64 186 15 79 203 minecraft:light_gray_concrete
setblock 16 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100"}','{"text": "occultism"}','{"text": "aviar"}','{"text": ""}']}}
setblock 17 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished"}','{"text": "Aviar\'s Circle"}','{"text": "with golden"}','{"text": "bowl, candles"}']}}
setblock 18 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and sacrificial"}','{"text": "bowls"}','{"text": ""}','{"text": ""}']}}
fill 29 64 186 29 79 203 minecraft:light_gray_concrete
fill 17 63 188 27 63 198 minecraft:smooth_basalt
setblock 19 64 192 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 19 64 193 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 19 64 194 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 20 64 191 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 20 64 193 occultism:chalk_glyph_white[facing=south,sign=7]
setblock 20 64 195 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 21 64 190 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 21 64 192 minecraft:white_candle[candles=1,lit=true]
setblock 21 64 193 occultism:chalk_glyph_white[facing=south,sign=9]
setblock 21 64 194 minecraft:white_candle[candles=1,lit=true]
setblock 21 64 196 occultism:chalk_glyph_white[facing=south,sign=1]
setblock 22 64 190 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 22 64 191 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 22 64 192 occultism:chalk_glyph_white[facing=south,sign=3]
setblock 22 64 193 occultism:golden_sacrificial_bowl
setblock 22 64 194 occultism:chalk_glyph_white[facing=south,sign=8]
setblock 22 64 195 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 22 64 196 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 23 64 190 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 23 64 192 minecraft:white_candle[candles=1,lit=true]
setblock 23 64 193 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 23 64 194 minecraft:white_candle[candles=1,lit=true]
setblock 23 64 196 occultism:chalk_glyph_white[facing=south,sign=7]
setblock 24 64 191 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 24 64 193 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 24 64 195 occultism:chalk_glyph_white[facing=south,sign=9]
setblock 25 64 192 occultism:chalk_glyph_white[facing=south,sign=1]
setblock 25 64 193 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 25 64 194 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 22 64 188 occultism:sacrificial_bowl[facing=up]
setblock 27 64 193 occultism:sacrificial_bowl[facing=up]
setblock 22 64 198 occultism:sacrificial_bowl[facing=up]
setblock 17 64 193 occultism:sacrificial_bowl[facing=up]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
