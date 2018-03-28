import arxiv_api
import watson_nlu

if __name__ == '__main__':
    keywords = {}

    while True:
        good_keywords = [keyword.strip() for keyword in filter(None, input('Good keywords: ').split(','))]
        bad_keywords = [keyword.strip() for keyword in filter(None, input('Bad keywords: ').split(','))]

        articles = arxiv_api.articles(good_keywords, bad_keywords, 10)

        new_keywords = {}
        for article in articles:
            watson_object = watson_nlu.WatsonObject(article['title'] + ": " + article['abstract'])
            new_keywords.update(watson_object.keywords)
        sorted_by_relevance = sorted(new_keywords.items(), key=lambda x: x[1], reverse=True)
        print('Found ' + str(len(new_keywords)) + ' keywords: ' + str(sorted_by_relevance))

        keywords.update({keyword: True for keyword in good_keywords})
        keywords.update({keyword: False for keyword in bad_keywords})

        print('Actual keywords: ' + str(keywords))
