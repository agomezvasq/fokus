import urllib.request
import xmltodict


def next_abstract(query, max_results):
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
