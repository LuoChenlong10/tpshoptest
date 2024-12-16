
import json
def read_json():
    with open('../data/login.json', 'r',encoding='utf-8') as f:
        return json.load(f)

    """
        问题：
            需求格式：[(), ()] 或 [[], []]
        解决：
            1、新建空列表 arrs = []
            2、读取现有的 json 值，存放到列表中
    """
def write_json():
    l_data = []
    data = read_json()
    for key,value in data.items():
        l_data.append((value["username"],value["password"],value["verify_code"],value["status"],value["except_result"]))
    return l_data




