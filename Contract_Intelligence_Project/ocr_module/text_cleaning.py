

with open("output/ocr_result.txt", "r", encoding="utf-8") as f:
                                                               text = f.read()

clean_text = text.replace("\n", " ")

with open("output/final_text.txt", "w", encoding="utf-8") as f:
                                                               f.write(clean_text)

print("Text cleaned successfully!")
