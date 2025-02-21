"""步骤二：识别礼包内容并将结果保存到 Excel"""
import os
import json
import logging
import pandas as pd
from paddleocr import PaddleOCR

def set_logging_level(level):
    """设置日志输出级别"""
    logger = logging.getLogger()
    logger.setLevel(level)

def recognize_text(image_path):
    """识别图像中的文本并返回识别到的内容"""
    set_logging_level(logging.WARNING)  # 调整日志级别以隐藏调试信息

    ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 设置语言为中文
    result = ocr.ocr(image_path)

    # 提取识别到的文字内容
    texts = []
    for line in result:
        for word_info in line:
            texts.append(word_info[1][0])  # 提取文本内容

    return texts

def generate_empty_tip_dict(directory):
    """生成空的 tip_dict.json 文件"""
    # <editor-fold desc="Description">
    tip_dict = {}
    tip_dict_file = os.path.join(directory, 'tip_dict.json')
    with open(tip_dict_file, 'w', encoding='utf-8') as f:
        json.dump(tip_dict, f, ensure_ascii=False, indent=4)
    print(f"已生成空的 tip_dict.json 文件: {tip_dict_file}")
    # </editor-fold>

# 在 process_images_in_directory 函数中调用
def process_images_in_directory(directory):
    tip_dict_file = os.path.join(directory, 'tip_dict.json')
    if not os.path.exists(tip_dict_file):
        generate_empty_tip_dict(directory)

    else:
        tip_dict = {}
        print("未找到 tip_dict.json 文件")

    ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 设置语言为中文
    data = []

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(directory, filename)
            recognized_texts = recognize_text(image_path)
            combined_text = '、'.join(recognized_texts)  # 使用"、"分隔文本

            # 移除文件扩展名
            game_name = os.path.splitext(filename)[0]

            # 获取对应的 tip 内容
            tip_content = tip_dict.get(filename, "无 tip 内容")   # 如果找不到对应的 tip，返回默认值

            # 将礼包名称、礼包内容和 tip 内容添加到数据中
            data.append([game_name, combined_text, tip_content])
        else:
            logging.warning(f"文件名格式不正确: {filename}")

    return data


def save_to_excel(data, output_file):
    """将识别到的文字内容和 tip 内容保存到 Excel"""
    df = pd.DataFrame(data, columns=['礼包名称', '礼包内容', 'tip 内容'])  # 创建 DataFrame，增加 tip 列
    df.to_excel(output_file, index=False)  # 保存为 Excel 文件
    print(f"OCR 结果和 tip 内容已保存到: {output_file}")

if __name__ == "__main__":
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    output_dir = config["image_save_dir"]  # 更新为实际的目录路径
    data = process_images_in_directory(output_dir)

    ocr_output_file = config["ocr_results_file"]  # 定义输出的 Excel 文件名
    save_to_excel(data, ocr_output_file)
