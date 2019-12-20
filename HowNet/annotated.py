import OpenHowNet
hownet_dict = OpenHowNet.HowNetDict()
# 获得hownet中的所有注释
#zh_word_list = hownet_dict.get_zh_words()
#print(zh_word_list[:30])
#print(hownet_dict.get_sememes_by_word("苹果", structured=False, lang="zh", merge=False))
#print(hownet_dict.get_sememes_by_word("苹果", structured=True))[0]["tree"]
print(hownet_dict["苹果"][0]["syn"])
print(len(hownet_dict.get_all_sememes()))
print(hownet_dict.get_sememe_relation("材料","材质"))
print(hownet_dict.get_sememe_via_relation("健康","antonym"))
