# 089 occultism/aviar
#area 11 146 34 175
fill 11 64 146 34 91 175 minecraft:air
fill 11 60 146 34 62 175 minecraft:stone
fill 11 63 146 34 63 175 minecraft:light_gray_concrete
fill 15 64 152 34 79 152 minecraft:light_gray_concrete
fill 15 64 152 15 79 169 minecraft:light_gray_concrete
setblock 16 64 168 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089"}','{"text": "occultism"}','{"text": "aviar"}','{"text": ""}']}}
setblock 17 64 168 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished"}','{"text": "Aviar\'s Circle"}','{"text": "with golden"}','{"text": "bowl, candles"}']}}
setblock 18 64 168 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and sacrificial"}','{"text": "bowls"}','{"text": ""}','{"text": ""}']}}
fill 29 64 152 29 79 169 minecraft:light_gray_concrete
fill 17 63 154 27 63 164 minecraft:smooth_basalt
setblock 19 64 158 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 19 64 159 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 19 64 160 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 20 64 157 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 20 64 159 occultism:chalk_glyph_white[facing=south,sign=7]
setblock 20 64 161 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 21 64 156 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 21 64 158 minecraft:white_candle[candles=1,lit=true]
setblock 21 64 159 occultism:chalk_glyph_white[facing=south,sign=9]
setblock 21 64 160 minecraft:white_candle[candles=1,lit=true]
setblock 21 64 162 occultism:chalk_glyph_white[facing=south,sign=1]
setblock 22 64 156 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 22 64 157 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 22 64 158 occultism:chalk_glyph_white[facing=south,sign=3]
setblock 22 64 159 occultism:golden_sacrificial_bowl
setblock 22 64 160 occultism:chalk_glyph_white[facing=south,sign=8]
setblock 22 64 161 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 22 64 162 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 23 64 156 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 23 64 158 minecraft:white_candle[candles=1,lit=true]
setblock 23 64 159 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 23 64 160 minecraft:white_candle[candles=1,lit=true]
setblock 23 64 162 occultism:chalk_glyph_white[facing=south,sign=7]
setblock 24 64 157 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 24 64 159 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 24 64 161 occultism:chalk_glyph_white[facing=south,sign=9]
setblock 25 64 158 occultism:chalk_glyph_white[facing=south,sign=1]
setblock 25 64 159 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 25 64 160 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 22 64 154 occultism:sacrificial_bowl[facing=up]
setblock 27 64 159 occultism:sacrificial_bowl[facing=up]
setblock 22 64 164 occultism:sacrificial_bowl[facing=up]
setblock 17 64 159 occultism:sacrificial_bowl[facing=up]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
