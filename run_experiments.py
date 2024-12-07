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
sequential = (
    "python main_sequential.py evaluate_multi_choice data/{dataset}.json "
    "--model_name gpt4o "
    "--prompt_name cot_multi_extract "
)

# multi-agent debate
multi_agent_debate = (
    "python main_debate.py evaluate_multi_choice data/{dataset}.json "
    "--model_name gpt4o "
    "--prompt_name cot_multi_extract "
    "--num_agents 2 "
    "--rounds 3 "
)

# single agent
single = (
    "python main_single.py evaluate_multi_choice data/{dataset}.json "
    "--model_name gpt4o "
    "--prompt_name cot_multi_extract "
)

# self-consistency
consistency = (
    "python main_consistency.py evaluate_multi_choice data/{dataset}.json "
    "--model_name gpt4o "
    "--prompt_name cot_multi_extract "
    "--num_samples 6 "
)

# 순차적으로 명령어 실행
for dataset in datasets:
    command = sequential.format(dataset=dataset)
    print(f"Running: {command}")
    os.system(command)

