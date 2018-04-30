import urllib.request
import xmltodict


class ArxivAPIQueryObject:

    def __init__(self, query, max_results):
        self.query = query


def next_article(query, max_results):
    query_encoded = urllib.request.quote(query, safe='~()*!.\'')
    url = 'http://export.arxiv.org/api/query?search_query=' + query_encoded + '&start=0&max_results=' + str(max_results)
    data = urllib.request.urlopen(url).read()
    o = xmltodict.parse(data)
    entries = o["feed"]["entry"]
    it = iter(entries)
    i = 0
    while i < max_results:
        yield next(it)
        i += 1
    return


def create_query(keywords_yes, keywords_no=[]):
    query = '(' + '+OR+'.join(['all:' + '"' + keyword.replace(' ', '+') + '"' for keyword in keywords_yes]) + ')'
    if keywords_no:
        query += '+ANDNOT+' + '(' + '+OR+'.join(
            ['all:' + '"' + keyword.replace(' ', '+') + '"' for keyword in keywords_no]
        ) + ')'
    return query


def articles(keywords_yes, keywords_no, max_results, ids=True, titles=True, abstracts=True, links=True):
    query = create_query(keywords_yes, keywords_no)
    print(query)
    url = 'http://export.arxiv.org/api/query?search_query=' + query + '&start=0&max_results=' + str(max_results)
    data = urllib.request.urlopen(url).read()
    o = xmltodict.parse(data)
    entries = o['feed']['entry']
    results = []
    for entry in entries:
        dct = {}
        if ids:
            dct['id'] = entry['id']
        if titles:
            dct['title'] = entry['title']
        if abstracts:
            dct['abstract'] = entry['summary']
        if links:
            for link in entry['link']:
                if '@title' in link and link['@title'] == 'pdf':
                    dct['link'] = link['@href']
                    break
        results.append(dct)
    return results
