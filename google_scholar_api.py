import scholarly


def next_abstract(query, max_results):
    g = scholarly.search_pubs_query(query)

    i = 0
    while i < max_results:
        n = next(g)
        yield n
        i += 1
    return
