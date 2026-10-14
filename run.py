from app.services.ingestion import load_file,chunk_documents


from pathlib import Path

docs = load_file(Path("data/sample_kb/service_desk_runbook.md"))
docs = chunk_documents(docs)


