import os

folders = [
    "notebooks",
    "data",
    "app",
    "tests",
    "experiments"
]

files = {
    "README.md": "# Chinese Flashcards App\n\nMVP to learn Chinese with games and flashcards.",
    ".gitignore": "__pycache__/\n.ipynb_checkpoints/\ndata/*.json",
    "requirements.txt": "ipywidgets\npandas\nnumpy\n",
    "app/__init__.py": "",
    "app/ui.py": "# UI components go here",
    "app/logic.py": "# Game logic and word selection",
    "app/translator.py": "# Translation lookup logic",
    "tests/test_logic.py": "# Unit tests",
    "data/word_bank.json": "[]"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Repo structure created.")
