import os

# 데이터셋 이름 리스트
datasets = [
    "circle_size_number",
    "color_grid",
    "color_hexagon",
    "color_number_hexagon",
    "color_overlap_squares",
    "color_size_circle",
    "grid_number_color",
    "grid_number",
    "polygon_sides_color",
    "polygon_sides_number",
    "rectangle_height_color",
    "rectangle_height_number",
    "shape_morph",
    "shape_reflect",
    "shape_size_grid",
    "shape_size_hexagon",
    "size_cycle",
    "size_grid",
    "triangle",
    "venn"
]

# sequential reasoning
sequential_command = (
    "python main_debate.py evaluate_multi_choice_sequential data/{dataset}.json "
    "--model_name gpt4o "
    "--prompt_name cot_multi_extract "
)

# single agent
dynamic = (
    "python main_dynamic.py evaluate_multi_choice data/{dataset}.json "
    "--model_name gpt4o "
    "--prompt_name cot_multi_extract "
)



# 순차적으로 명령어 실행
for dataset in datasets:
    command = dynamic.format(dataset=dataset)
    print(f"Running: {command}")
    os.system(command)

# 순차적으로 명령어 실행
# for dataset in datasets:
#     command = sequential_command.format(dataset=dataset)
#     print(f"Running: {command}")
#     os.system(command)
