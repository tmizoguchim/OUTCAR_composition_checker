import os
import random

def read_composition(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("POSCAR ="):
                return line.strip().split('=')[1].strip()
    return None

def main():
    folder_path = '.'  # 現在のフォルダ
    files = [f for f in os.listdir(folder_path) if f.startswith('OUTCAR_for_mace')]
    
    composition_dict = {}
    
    for file in files:
        composition = read_composition(file)
        if composition:
            if composition not in composition_dict:
                composition_dict[composition] = []
            composition_dict[composition].append(file)
    
    for composition, file_list in composition_dict.items():
        print(f"Composition: {composition}, Count: {len(file_list)}")
    
    selected_files = []
    for composition, file_list in composition_dict.items():
        num_to_select = min(120, len(file_list))  # ここで選択する数を指定
        selected_files.extend(random.sample(file_list, num_to_select))
    
    selected_files_str = " ".join(selected_files)
    print("Selected files:")
    print(selected_files_str)
    
    with open('selected_outcar_files.txt', 'w') as output_file:
        output_file.write(selected_files_str)

if __name__ == "__main__":
    main()
