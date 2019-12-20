import OpenHowNet
#OpenHowNet.download()  #下载数据
hownet_dict = OpenHowNet.HowNetDict()
result_list = hownet_dict.get("苹果")
print(len(result_list))
print(result_list[0])
hownet_dict.visualize_sememe_trees("苹果", 2)
