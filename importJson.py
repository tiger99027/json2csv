import json
import csv

# 读取并解析 JSON 文件(文件路径请根据实际情况修改)
with open('D:\\code\\test\\py\\arch.json', 'r', encoding='utf-8') as f:
    data1 = json.load(f)

# 找到 _source 的数据
hits1 = data1["hits"]["hits"]

# 准备一个空字典，用于存储所有的_source数据，以 'id' 为键
source_data_dict = {}

# 需要的键值
keys_needed = ["id", "decisionStage", "researchStage", "title", "track", "desc"]

# 循环遍历每一条hit
for hit in hits1:
    source_data = hit["_source"]

    # 创建一个新的字典，只包含需要的键值对
    new_data = {key: source_data.get(key, "") for key in keys_needed}

    # 将处理后的数据添加到字典中
    source_data_dict[new_data['id']] = new_data


# 再次读取并解析 JSON 文件
with open('D:\\code\\test\\py\\track.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)

# 找到 _source 的数据
hits2 = data2["hits"]["hits"]

# 准备一个空列表，用于存储所有的_source数据
source_data_list = []

# 循环遍历每一条hit
for hit in hits2:
    source_data = hit["_source"]

    # 将处理后的数据添加到列表中
    source_data_list.append(source_data)

    # 查找相关联的数据
    related_data = source_data_dict.get(source_data["architecturalId"], {})

    # 合并相关联的数据
    source_data.update(related_data)

# 确定所有可能的字段名
all_keys = set().union(*[d.keys() for d in source_data_list])

# 将数据写入 CSV(文件路径根据实际修改)
with open('D:\\code\\test\\py\\arch_track.csv', 'w', newline='', encoding='utf_8_sig') as f:
    writer = csv.DictWriter(f, fieldnames=all_keys)
    writer.writeheader()
    for source_data in source_data_list:
        writer.writerow(source_data)
