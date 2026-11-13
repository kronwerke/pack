# 101 occultism/hedyrin
#area 45 176 68 205
fill 45 64 176 68 91 205 minecraft:air
fill 45 60 176 68 62 205 minecraft:stone
fill 45 63 176 68 63 205 minecraft:light_gray_concrete
fill 49 64 182 68 79 182 minecraft:light_gray_concrete
fill 49 64 182 49 79 199 minecraft:light_gray_concrete
setblock 50 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101"}','{"text": "occultism"}','{"text": "hedyrin"}','{"text": ""}']}}
setblock 51 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hedyrin\'s Lure"}','{"text": "with the yellow"}','{"text": "glyphs"}','{"text": ""}']}}
fill 63 64 182 63 79 199 minecraft:light_gray_concrete
fill 51 63 184 61 63 194 minecraft:smooth_basalt
setblock 53 64 189 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 54 64 188 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 54 64 189 minecraft:white_candle[candles=1,lit=true]
setblock 54 64 190 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 55 64 187 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 55 64 189 occultism:chalk_glyph_gold[facing=south,sign=7]
setblock 55 64 191 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 56 64 186 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 56 64 187 minecraft:white_candle[candles=1,lit=true]
setblock 56 64 188 occultism:chalk_glyph_gold[facing=south,sign=9]
setblock 56 64 189 occultism:golden_sacrificial_bowl
setblock 56 64 190 occultism:chalk_glyph_gold[facing=south,sign=1]
setblock 56 64 191 minecraft:white_candle[candles=1,lit=true]
setblock 56 64 192 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 57 64 187 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 57 64 189 occultism:chalk_glyph_gold[facing=south,sign=3]
setblock 57 64 191 occultism:chalk_glyph_white[facing=south,sign=8]
setblock 58 64 188 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 58 64 189 minecraft:white_candle[candles=1,lit=true]
setblock 58 64 190 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 59 64 189 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 56 64 184 occultism:sacrificial_bowl[facing=up]
setblock 61 64 189 occultism:sacrificial_bowl[facing=up]
setblock 56 64 194 occultism:sacrificial_bowl[facing=up]
setblock 51 64 189 occultism:sacrificial_bowl[facing=up]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
