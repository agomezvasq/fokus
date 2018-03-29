import scholarly


def next_article(query, max_results):
    g = scholarly.search_pubs_query(query)

    i = 0
    while i < max_results:
        n = next(g)
        yield n
        i += 1
    return


def create_query(keywords_yes, keywords_no=[]):
    query = ' OR '.join(['"' + keyword + '"' for keyword in keywords_yes])
    if keywords_no:
        query += ' ' + ' '.join(['-' + '"' + keyword + '"' for keyword in keywords_no])
    return query


def articles(keywords_yes, keywords_no, max_results, ids=True, titles=True, abstracts=True):
    query = create_query(keywords_yes, keywords_no)
    print(query)
    article_list = list(next_article(query, max_results))
    results = []
    for article in article_list:
        dct = {}
        if ids:
            dct['id'] = article.id_scholarcitedby
        if titles:
            dct['title'] = article.bib['title']
        if abstracts:
            if 'abstract' in article.bib:
                dct['abstract'] = article.bib['abstract']
            else:
                continue
        results.append(dct)
    return results
