# 099 occultism/aviar
#area 11 176 34 205
fill 11 64 176 34 91 205 minecraft:air
fill 11 60 176 34 62 205 minecraft:stone
fill 11 63 176 34 63 205 minecraft:light_gray_concrete
fill 15 64 182 34 79 182 minecraft:light_gray_concrete
fill 15 64 182 15 79 199 minecraft:light_gray_concrete
setblock 16 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099"}','{"text": "occultism"}','{"text": "aviar"}','{"text": ""}']}}
setblock 17 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished"}','{"text": "Aviar\'s Circle"}','{"text": "with golden"}','{"text": "bowl, candles"}']}}
setblock 18 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and sacrificial"}','{"text": "bowls"}','{"text": ""}','{"text": ""}']}}
fill 29 64 182 29 79 199 minecraft:light_gray_concrete
fill 17 63 184 27 63 194 minecraft:smooth_basalt
setblock 19 64 188 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 19 64 189 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 19 64 190 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 20 64 187 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 20 64 189 occultism:chalk_glyph_white[facing=south,sign=7]
setblock 20 64 191 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 21 64 186 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 21 64 188 minecraft:white_candle[candles=1,lit=true]
setblock 21 64 189 occultism:chalk_glyph_white[facing=south,sign=9]
setblock 21 64 190 minecraft:white_candle[candles=1,lit=true]
setblock 21 64 192 occultism:chalk_glyph_white[facing=south,sign=1]
setblock 22 64 186 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 22 64 187 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 22 64 188 occultism:chalk_glyph_white[facing=south,sign=3]
setblock 22 64 189 occultism:golden_sacrificial_bowl
setblock 22 64 190 occultism:chalk_glyph_white[facing=south,sign=8]
setblock 22 64 191 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 22 64 192 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 23 64 186 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 23 64 188 minecraft:white_candle[candles=1,lit=true]
setblock 23 64 189 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 23 64 190 minecraft:white_candle[candles=1,lit=true]
setblock 23 64 192 occultism:chalk_glyph_white[facing=south,sign=7]
setblock 24 64 187 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 24 64 189 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 24 64 191 occultism:chalk_glyph_white[facing=south,sign=9]
setblock 25 64 188 occultism:chalk_glyph_white[facing=south,sign=1]
setblock 25 64 189 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 25 64 190 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 22 64 184 occultism:sacrificial_bowl[facing=up]
setblock 27 64 189 occultism:sacrificial_bowl[facing=up]
setblock 22 64 194 occultism:sacrificial_bowl[facing=up]
setblock 17 64 189 occultism:sacrificial_bowl[facing=up]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
