short_term_memory=[]
long_term_memory=[]
def add_to_short_term(message):
    short_term_memory.append(message)
def get_short_term():
    return short_term_memory[-5:]
def add_to_long_term(data):
    long_term_memory.append(data)
def search_long_term(query):
    results = []
    for item in long_term_memory:
        if query.lower() in item.lower():
            results.append(item)
    return results