import json

data = [
    {"text": "Hello contract A"},
    {"text": "Hello contract B"}
]

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("File created successfully")