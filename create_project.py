from pathlib import Path


#current working directory
root = Path(".")


# folders to create
folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests",
]


files = [
    "app/main.py",
    "ingest_sample_kb.py",
    "run.py",
    ".env",
    ".gitignore"
]


for folder in folders:
    (root /folder).mkdir(parents=True, exist_ok=True)

for file in files:
    (root /file).touch(exist_ok=True)


print("Project created successfully")