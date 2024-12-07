## **Setup**
***

```
conda create -n puzzle python=3.10 -y
conda activate puzzle
pip install -r requirements.txt
```


## Openai api key
***
Put your openai api key in
- [.env](https://github.com/Minseo10/sequential-multi-agent/blob/main/.env): `OPENAI_KEY=your_api_key` 
- [key.json](https://github.com/Minseo10/sequential-multi-agent/blob/main/key.json): `"OPENAI_API_KEY": "your_openai_key"` 

## Dataset
***
- from [PuzzleVQA](https://github.com/declare-lab/LLM-PuzzleTest)

### Current List of Puzzle Name

- `circle_size_number`
- `color_grid`
- `color_hexagon`
- `color_number_hexagon`
- `color_overlap_squares`
- `color_size_circle`
- `grid_number_color`
- `grid_number`
- `polygon_sides_color`
- `polygon_sides_number`
- `rectangle_height_color`
- `rectangle_height_number`
- `shape_morph`
- `shape_reflect`
- `shape_size_grid`
- `shape_size_hexagon`
- `size_cycle`
- `size_grid`
- `triangle`
- `venn`


## Run
***
### Sequential Multi-Agent (Our method)
```
# Evaluate
python main_sequential.py evaluate_multi_choice data/{puzzle_name}.json --model_name gpt4o --prompt_name cot_multi_extract
```
- puzzle_name: name of one of the puzzles. 
```
# Print to see the average performance
python main_sequential.py print_results outputs_sequential/*/*/*.jsonl
```
- outputs are saved in "outputs_sequential"

### Multi-Agent Debate (Society of Mind)
```
# Evaluate
python main_debate.py evaluate_multi_choice data/{puzzle_name}.json --model_name gpt4o --prompt_name cot_multi_extract --num_agents 2 --rounds 3
```
- puzzle_name: name of one of the puzzles
- num_agents: number of the agents per round
- rounds: number of total rounds
```
# Print to see the average performance
python main_debate.py print_results outputs_debate/*/*/*.jsonl
```
- outputs are saved in "outputs_debate"

### Self-Consistency
```
# Evaluate
# Print to see the average performance
python main_consistency.py evaluate_multi_choice data/{puzzle_name}.json --model_name gpt4o --prompt_name cot_multi_extract --num_samples 6
```
- puzzle_name: name of one of the puzzles
- num_samples: number of the samples of VLM responses
```
# Print to see the average performance
python main_consistency.py print_results outputs_consistency/*/*/*.jsonl
```
- outputs are saved in "outputs_consistency"

### Single-Agent
```
# Evaluate
python main_single.py evaluate_multi_choice data/{puzzle_name}.json --model_name gpt4o --prompt_name cot_multi_extract
```
- puzzle_name: name of one of the puzzles
```
# Print to see the average performance
python main_single.py print_results outputs_single/*/*/*.jsonl
```
- outputs are saved in "outputs_single"

