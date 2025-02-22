import os
import sys
import time
import concurrent.futures
from .parser.cpp_parser import parse_cpp_files, parse_cpp
from .parser.java_parser import parse_java_files, parse_java
from .graph.diagram_converter import save_diagrams

def parse_file_with_metadata(file_path):
    """解析单个文件并收集元数据"""
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext == ".java":
        java_data = parse_java_files([file_path])
        save_diagrams(java_data, file_path + "_java")
    elif file_ext in ['.cpp', '.h', '.hpp', '.cc']:
        cpp_data = parse_java_files([file_path])
        save_diagrams(java_data, file_path + "_cpp")
    else:
        raise ValueError(f"Unsupported file type: {file_ext}")
    
    return {
        'java': java_data,
        'cpp': cpp_data
    }

def process_input(input_path):
    """统一处理输入路径（文件或目录）"""
    if not os.path.isabs(input_path):
        input_path = os.path.join(os.getcwd(), input_path)
    print(f"Processing input path: {input_path}")
    if os.path.isdir(input_path):
        return handle_directory(input_path)
    elif os.path.isfile(input_path):
        return handle_file(input_path)
    else:
        raise ValueError(f"Invalid input path: {input_path}")

def handle_directory(directory):
    """处理目录输入，按语言类型分线程解析"""
    java_files = []
    cpp_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                print(f"Processing file: {file}")
                java_files.append(os.path.join(root, file))
            elif file.endswith(".cpp") or file.endswith(".h") or file.endswith(".hpp") or file.endswith(".cc"):
                print(f"Processing file: {file}")
                cpp_files.append(os.path.join(root, file))
    cpp_results = {}
    java_results = {}
    # 并行解析
    with concurrent.futures.ThreadPoolExecutor() as executor:
        if len(java_files) != 0:
            java_results = parse_java_files(java_files)
            save_diagrams(java_results, directory + "/code2uml_java")
        if len(cpp_files) != 0:
            cpp_results = parse_cpp_files(cpp_files)
            save_diagrams(cpp_results, directory + "/code2uml_cpp")
    
    return {
        "java": java_results,
        "cpp": cpp_results
    }

def handle_file(file_path):
    """处理文件输入，按文件类型解析"""
    return parse_file_with_metadata(file_path)

import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate UML diagrams from source code')
    parser.add_argument('--input', help='Input file, directory', default=".")
    args = parser.parse_args()
    
    if args.input is None:
        parser.usage()
        exit()
    
    print("path:", args.input)
    
    total_lines = 0
    total_time = time.time()
    
    results = process_input(args.input)
    if 'java' in results:
        if 'lines' in results['java']:
            total_lines += results['java']['lines']
    if 'cpp' in results:
        if 'lines' in results['cpp']:
            total_lines += results['cpp']['lines']

    total_time = time.time() - total_time
    # 打印统计信息
    print(f"\n=== Parsed Summary ===")
    print(f"Total Lines: {total_lines}")
    print(f"Total Time: {total_time:.2f}s")

if __name__ == "__main__":
    main()