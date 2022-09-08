import pykakasi
kks = pykakasi.kakasi()
text = "花火"
result = kks.convert(text)
for item in result:
    print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))
