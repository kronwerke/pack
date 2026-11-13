# 084 occultism/aviar
#area 11 144 34 173
fill 11 64 144 34 91 173 minecraft:air
fill 11 60 144 34 62 173 minecraft:stone
fill 11 63 144 34 63 173 minecraft:light_gray_concrete
fill 15 64 150 34 79 150 minecraft:light_gray_concrete
fill 15 64 150 15 79 167 minecraft:light_gray_concrete
setblock 16 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084"}','{"text": "occultism"}','{"text": "aviar"}','{"text": ""}']}}
setblock 17 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished"}','{"text": "Aviar\'s Circle"}','{"text": "with golden"}','{"text": "bowl, candles"}']}}
setblock 18 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and sacrificial"}','{"text": "bowls"}','{"text": ""}','{"text": ""}']}}
fill 29 64 150 29 79 167 minecraft:light_gray_concrete
fill 17 63 152 27 63 162 minecraft:smooth_basalt
setblock 19 64 156 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 19 64 157 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 19 64 158 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 20 64 155 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 20 64 157 occultism:chalk_glyph_white[facing=south,sign=7]
setblock 20 64 159 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 21 64 154 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 21 64 156 minecraft:white_candle[candles=1,lit=true]
setblock 21 64 157 occultism:chalk_glyph_white[facing=south,sign=9]
setblock 21 64 158 minecraft:white_candle[candles=1,lit=true]
setblock 21 64 160 occultism:chalk_glyph_white[facing=south,sign=1]
setblock 22 64 154 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 22 64 155 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 22 64 156 occultism:chalk_glyph_white[facing=south,sign=3]
setblock 22 64 157 occultism:golden_sacrificial_bowl
setblock 22 64 158 occultism:chalk_glyph_white[facing=south,sign=8]
setblock 22 64 159 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 22 64 160 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 23 64 154 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 23 64 156 minecraft:white_candle[candles=1,lit=true]
setblock 23 64 157 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 23 64 158 minecraft:white_candle[candles=1,lit=true]
setblock 23 64 160 occultism:chalk_glyph_white[facing=south,sign=7]
setblock 24 64 155 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 24 64 157 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 24 64 159 occultism:chalk_glyph_white[facing=south,sign=9]
setblock 25 64 156 occultism:chalk_glyph_white[facing=south,sign=1]
setblock 25 64 157 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 25 64 158 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 22 64 152 occultism:sacrificial_bowl[facing=up]
setblock 27 64 157 occultism:sacrificial_bowl[facing=up]
setblock 22 64 162 occultism:sacrificial_bowl[facing=up]
setblock 17 64 157 occultism:sacrificial_bowl[facing=up]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
