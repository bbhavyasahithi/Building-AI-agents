from rag_pipeline import search
def document_search(query,index,docs):
    return search(query,index,docs)
def meeting_notes_tool(notes_db,query):
    return [n for n in notes_db if query.lower() in n.lower()]