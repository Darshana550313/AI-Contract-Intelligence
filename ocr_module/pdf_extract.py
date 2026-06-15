import fitz

pdf = fitz.open("data/sample_contract.pdf")

text = ""

for page in pdf:
                text += page.get_text()

with open("output/contract_text.txt", "w", encoding="utf-8") as f:
                                                                  f.write(text)

print("Text saved successfully!")