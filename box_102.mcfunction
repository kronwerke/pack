# 102 occultism/hedyrin
#area 45 182 68 211
fill 45 64 182 68 91 211 minecraft:air
fill 45 60 182 68 62 211 minecraft:stone
fill 45 63 182 68 63 211 minecraft:light_gray_concrete
fill 49 64 188 68 79 188 minecraft:light_gray_concrete
fill 49 64 188 49 79 205 minecraft:light_gray_concrete
setblock 50 64 204 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102"}','{"text": "occultism"}','{"text": "hedyrin"}','{"text": ""}']}}
setblock 51 64 204 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hedyrin\'s Lure"}','{"text": "with the yellow"}','{"text": "glyphs"}','{"text": ""}']}}
fill 63 64 188 63 79 205 minecraft:light_gray_concrete
fill 51 63 190 61 63 200 minecraft:smooth_basalt
setblock 53 64 195 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 54 64 194 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 54 64 195 minecraft:white_candle[candles=1,lit=true]
setblock 54 64 196 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 55 64 193 occultism:chalk_glyph_white[facing=south,sign=2]
setblock 55 64 195 occultism:chalk_glyph_gold[facing=south,sign=7]
setblock 55 64 197 occultism:chalk_glyph_white[facing=south,sign=12]
setblock 56 64 192 occultism:chalk_glyph_white[facing=south,sign=4]
setblock 56 64 193 minecraft:white_candle[candles=1,lit=true]
setblock 56 64 194 occultism:chalk_glyph_gold[facing=south,sign=9]
setblock 56 64 195 occultism:golden_sacrificial_bowl
setblock 56 64 196 occultism:chalk_glyph_gold[facing=south,sign=1]
setblock 56 64 197 minecraft:white_candle[candles=1,lit=true]
setblock 56 64 198 occultism:chalk_glyph_white[facing=south,sign=6]
setblock 57 64 193 occultism:chalk_glyph_white[facing=south,sign=11]
setblock 57 64 195 occultism:chalk_glyph_gold[facing=south,sign=3]
setblock 57 64 197 occultism:chalk_glyph_white[facing=south,sign=8]
setblock 58 64 194 occultism:chalk_glyph_white[facing=south,sign=0]
setblock 58 64 195 minecraft:white_candle[candles=1,lit=true]
setblock 58 64 196 occultism:chalk_glyph_white[facing=south,sign=5]
setblock 59 64 195 occultism:chalk_glyph_white[facing=south,sign=10]
setblock 56 64 190 occultism:sacrificial_bowl[facing=up]
setblock 61 64 195 occultism:sacrificial_bowl[facing=up]
setblock 56 64 200 occultism:sacrificial_bowl[facing=up]
setblock 51 64 195 occultism:sacrificial_bowl[facing=up]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
