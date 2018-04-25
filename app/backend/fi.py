from fokus.backend import watson_nlu, arxiv_api, google_scholar_api

if __name__ == '__main__':
    keywords = {}

    while True:
        good_keywords = [keyword.strip() for keyword in filter(None, input('Good keywords: ').split(','))]
        bad_keywords = [keyword.strip() for keyword in filter(None, input('Bad keywords: ').split(','))]

        keywords.update({keyword: True for keyword in good_keywords})
        keywords.update({keyword: False for keyword in bad_keywords})

        print('Actual keywords: ' + str(keywords))

        articles = []
        articles.extend(arxiv_api.articles([x for x in keywords.keys() if keywords[x]],
                                           [x for x in keywords.keys() if not keywords[x]],
                                           10))
        articles.extend(google_scholar_api.articles([x for x in keywords.keys() if keywords[x]],
                                                    [x for x in keywords.keys() if not keywords[x]],
                                                    10))

        new_keywords = {}
        for article in articles:
            watson_object = watson_nlu.WatsonObject(article['title'] + ": " + article['abstract'])
            new_keywords.update(watson_object.keywords)
        sorted_by_relevance = sorted(new_keywords.items(), key=lambda x: x[1], reverse=True)

        print('Found ' + str(len(new_keywords)) + ' keywords: ' + str(sorted_by_relevance))

        print('Found articles: ' + str([article['title'] for article in articles]))