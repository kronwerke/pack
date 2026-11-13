# 090 occultism/hedyrin
#area 45 146 68 175
fill 45 64 146 68 91 175 minecraft:air
fill 45 60 146 68 62 175 minecraft:stone
fill 45 63 146 68 63 175 minecraft:light_gray_concrete
fill 49 64 152 68 79 152 minecraft:light_gray_concrete
fill 49 64 152 49 79 169 minecraft:light_gray_concrete
setblock 50 64 168 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090"}','{"text": "occultism"}','{"text": "hedyrin"}','{"text": ""}']}}
setblock 51 64 168 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hedyrin\'s Lure"}','{"text": "with the yellow"}','{"text": "glyphs"}','{"text": ""}']}}
fill 63 64 152 63 79 169 minecraft:light_gray_concrete
fill 51 63 154 61 63 164 minecraft:smooth_basalt
setblock 53 64 159 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 54 64 158 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 54 64 159 minecraft:white_candle[candles=1,lit=true]
setblock 54 64 160 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 55 64 157 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 55 64 159 occultism:chalk_glyph_gold[facing=south,sign=7]
setblock 55 64 161 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 56 64 156 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 56 64 157 minecraft:white_candle[candles=1,lit=true]
setblock 56 64 158 occultism:chalk_glyph_gold[facing=south,sign=9]
setblock 56 64 159 occultism:golden_sacrificial_bowl
setblock 56 64 160 occultism:chalk_glyph_gold[facing=south,sign=1]
setblock 56 64 161 minecraft:white_candle[candles=1,lit=true]
setblock 56 64 162 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 57 64 157 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 57 64 159 occultism:chalk_glyph_gold[facing=south,sign=3]
setblock 57 64 161 occultism:chalk_glyph_white[facing=south,sign=8]
setblock 58 64 158 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 58 64 159 minecraft:white_candle[candles=1,lit=true]
setblock 58 64 160 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 59 64 159 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 56 64 154 occultism:sacrificial_bowl[facing=up]
setblock 61 64 159 occultism:sacrificial_bowl[facing=up]
setblock 56 64 164 occultism:sacrificial_bowl[facing=up]
setblock 51 64 159 occultism:sacrificial_bowl[facing=up]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
