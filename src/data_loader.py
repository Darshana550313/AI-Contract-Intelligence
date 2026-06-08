import json

file_path = "data/CUAD/train_separate_questions.json"

with open(file_path, "r", encoding="utf-8") as f:
                                                 data = json.load(f)

print("Dataset loaded successfully!")

# Print first few records
if isinstance(data, list):
                         print(data[:3])
else:
    print(list(data.items())[:3])