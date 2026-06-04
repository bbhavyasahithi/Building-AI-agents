from memory import add_to_short_term, get_short_term, add_to_long_term
from rag_pipeline import build_index
from tools import document_search, meeting_notes_tool
with open("data/clients.txt","r") as f:
    clients=[line.strip() for line in f.readlines()]
with open("data/emails.txt", "r") as f:
    emails=[line.strip() for line in f.readlines()]
with open("data/meeting_notes.txt", "r") as f:
    meeting_notes=[line.strip() for line in f.readlines()]
docs=clients+emails
notes_db=meeting_notes
index,docs=build_index(docs)
def generate_brief(query):
    add_to_short_term(query)
    rag_results=document_search(query,index,docs)
    notes=meeting_notes_tool(notes_db,query)
    context=get_short_term()
    brief=f"""
=========================================
MEETING PREPARATION BRIEF
=========================================
User Query: {query}
KEY CLIENT INFO:
{[r[0] for r in rag_results]}
PREVIOUS NOTES:
{notes}
CONVERSATION CONTEXT:
{context}
NEXT STEPS:
1. Review client history
2. Check previous meeting notes
3. Follow up on pending action items
4. Prepare discussion points
"""
    add_to_long_term(brief)
    return brief
print("=========================================")
print("Client Meeting Preparation Agent")
print("Type 'exit' to quit")
print("=========================================")
while True:
    q = input("\nAsk Agent: ").strip()
    if q.lower() == "exit":
        print("Goodbye")
        break
    print(generate_brief(q))