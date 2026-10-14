from app.services.ingestion import load_file,chunk_documents


from pathlib import Path
from app.rag.vectorstore import add_documents


docs = load_file(Path("data/sample_kb/service_desk_runbook.md"))
chunks = chunk_documents(docs)


add_documents(docs)


