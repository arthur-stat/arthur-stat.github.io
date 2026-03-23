import os
from aaa_config import SETTINGS
from PIL import Image
from pathlib import Path

def process_screenshots(input_folder, output_folder, input_resolution, output_resolution, compaction_quality, clear_original_files, exception):

    # 创建输出目录
    output_dir = Path(input_folder) / output_folder
    output_dir.mkdir(exist_ok=True)
    
    # 计算放缩比例
    scale_factor = output_resolution[0]/input_resolution[0]

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png') and filename not in exception:
            input_path = os.path.join(input_folder, filename)
            
            try:
                with Image.open(input_path) as img:
                    # 转换颜色模式
                    if img.mode in ('RGBA', 'P'):
                        img = img.convert('RGB')
                    
                    # 获取实际分辨率，动态计算目标尺寸
                    original_width, original_height = img.size
                    new_width = int(original_width * scale_factor)
                    new_height = int(original_height * scale_factor)
                    
                    # 执行等比例缩放
                    resized_img = img.resize(
                        (new_width, new_height),
                        resample=Image.LANCZOS  # 最佳抗锯齿算法
                    )
                    
                    # 构建输出路径
                    output_name = os.path.splitext(filename)[0] + '.jpg'
                    output_path = os.path.join(output_dir, output_name)
                    
                    # 保存优化
                    resized_img.save(
                        output_path,
                        'JPEG',
                        quality=compaction_quality,
                        optimize=True,
                        progressive=True
                    )
                    
                    # 删除原文件
                    if clear_original_files:
                        try:
                            os.remove(input_path)
                            # print(f"删除原始文件: {filename}")
                        except PermissionError:
                            print(f"权限不足，无法删除 {filename}")
                        except FileNotFoundError:
                            print(f"文件 {filename} 不存在")
                        except Exception as e:
                            print(f"删除 {filename} 失败 | 错误: {str(e)}")
                    
            except Exception as e:
                print(f"处理 {filename} 失败 | 错误: {str(e)}")

if __name__ == "__main__":
    process_screenshots(**SETTINGS)