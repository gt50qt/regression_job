import yaml
import os


def read_yaml_data(yaml_path):
    '''读取yaml文件'''
    f = open(yaml_path, "r", encoding="utf-8")
    cfg = f.read()
    print(cfg)

    # 转python dict

    d = yaml.load(cfg)
    return d

if __name__ == '__main__':
    # print(__file__)  # D:/soft/kecheng202004/ke11/read_yaml.py
    cur_path = os.path.dirname(os.path.realpath(__file__))
    # print(cur_path)
    yaml_path = os.path.join(os.path.dirname(cur_path), "testdata", "test_data.yml")
    print(yaml_path)
    d = read_yaml_data(yaml_path)
    print(d)
