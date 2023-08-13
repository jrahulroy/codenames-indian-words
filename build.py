import importlib
listGenerator = importlib.import_module("list-generator")

listGenerator.concatenate_file(
    "./generated-lists/list-of-hyderabad-culture-words.txt", "./word-lists/list-of-hyderabad-culture-words.txt")
listGenerator.concatenate_file(
    "./generated-lists/list-of-indian-culture-words.txt", "./word-lists/list-of-indian-culture-words.txt")
