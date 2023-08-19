import json

with open('dataset.json') as f:
        dataset = json.load(f)
    # Filter out the conversations with less than 2 turns.
dataset = [
    data for data in dataset
    if len(data["conversations"]) >= 2
]
# Only keep the first two turns of each conversation.
dataset = [
    (data["conversations"][0]["value"], data["conversations"][1]["value"])
    for data in dataset
]

# Tokenize the prompts and completions.
prompts = [prompt for prompt, _ in dataset]
completions = [completion for _, completion in dataset]
hola = 1 + 1