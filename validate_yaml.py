#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
验证 publications.yaml 文件格式
"""
import yaml
import sys
import os

def validate_yaml(file_path):
    """验证 YAML 文件格式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        print("=" * 60)
        print("YAML 格式验证结果")
        print("=" * 60)
        print(f"✓ 文件格式正确！")
        print()
        
        if 'publications' in data:
            pubs = data['publications']
            print(f"找到 {len(pubs)} 个条目:")
            print()
            
            for i, pub in enumerate(pubs, 1):
                print(f"{i}. {pub.get('title', 'No title')[:70]}")
                print(f"   作者: {', '.join(pub.get('authors', []))[:50]}...")
                print(f"   期刊: {pub.get('journal', 'N/A')}")
                print(f"   年份: {pub.get('year', 'N/A')}")
                print(f"   URL: {pub.get('url', 'N/A')[:50]}...")
                
                # 检查必需字段
                required_fields = ['title', 'authors', 'journal', 'year', 'url']
                missing = [f for f in required_fields if not pub.get(f)]
                if missing:
                    print(f"   ⚠ 缺少必需字段: {', '.join(missing)}")
                
                print()
        else:
            print("⚠ 警告: 未找到 'publications' 键")
            print(f"文件中的顶级键: {list(data.keys())}")
        
        print("=" * 60)
        return True
        
    except yaml.YAMLError as e:
        print("=" * 60)
        print("❌ YAML 格式错误！")
        print("=" * 60)
        print(f"错误信息: {e}")
        if hasattr(e, 'problem_mark'):
            mark = e.problem_mark
            print(f"错误位置: 第 {mark.line + 1} 行, 第 {mark.column + 1} 列")
        return False
        
    except FileNotFoundError:
        print(f"❌ 文件未找到: {file_path}")
        return False
        
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return False

if __name__ == "__main__":
    # 默认文件路径
    file_path = "data/publications.yaml"
    
    # 如果提供了命令行参数，使用该路径
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"❌ 文件不存在: {file_path}")
        sys.exit(1)
    
    # 验证文件
    success = validate_yaml(file_path)
    sys.exit(0 if success else 1)

