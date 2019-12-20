import OpenHowNet
hownet_dict_advanced = OpenHowNet.HowNetDict(use_sim=True)
hownet_dict_advanced.initialize_sememe_similarity_calculation()
query_result = hownet_dict_advanced.get_nearest_words_via_sememes("苹果",12)
example = query_result[0]
print("wordname", example["word"])
print("id", example["id"])
print("synset and corresonding word&id&score:")
print(example["synset"])