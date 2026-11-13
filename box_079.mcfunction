# 079 occultism/hedyrin
#area 30 144 53 173
fill 30 64 144 53 91 173 minecraft:air
fill 30 60 144 53 62 173 minecraft:stone
fill 30 63 144 53 63 173 minecraft:light_gray_concrete
fill 34 64 150 53 79 150 minecraft:light_gray_concrete
fill 34 64 150 34 79 167 minecraft:light_gray_concrete
setblock 35 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "occultism"}','{"text": "hedyrin"}','{"text": ""}']}}
setblock 36 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hedyrin\'s Lure"}','{"text": "with the yellow"}','{"text": "glyphs"}','{"text": ""}']}}
fill 48 64 150 48 79 167 minecraft:light_gray_concrete
fill 36 63 152 46 63 162 minecraft:smooth_basalt
setblock 38 64 157 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 39 64 156 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 39 64 157 minecraft:white_candle[candles=1,lit=true]
setblock 39 64 158 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 40 64 155 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 40 64 157 occultism:chalk_glyph_gold[facing=south,sign=7]
setblock 40 64 159 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 41 64 154 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 41 64 155 minecraft:white_candle[candles=1,lit=true]
setblock 41 64 156 occultism:chalk_glyph_gold[facing=south,sign=9]
setblock 41 64 157 occultism:golden_sacrificial_bowl
setblock 41 64 158 occultism:chalk_glyph_gold[facing=south,sign=1]
setblock 41 64 159 minecraft:white_candle[candles=1,lit=true]
setblock 41 64 160 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 42 64 155 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 42 64 157 occultism:chalk_glyph_gold[facing=south,sign=3]
setblock 42 64 159 occultism:chalk_glyph_white[facing=south,sign=8]
setblock 43 64 156 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 43 64 157 minecraft:white_candle[candles=1,lit=true]
setblock 43 64 158 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 44 64 157 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 41 64 152 occultism:sacrificial_bowl[facing=up]
setblock 46 64 157 occultism:sacrificial_bowl[facing=up]
setblock 41 64 162 occultism:sacrificial_bowl[facing=up]
setblock 36 64 157 occultism:sacrificial_bowl[facing=up]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
