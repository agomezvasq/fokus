import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='d8570193-f456-418e-ab20-bae3a783da9c',
  password='pJnMjUVd4yHG',
  version='2018-03-16')


class WatsonObject:

    def __init__(self, text):
        self.text = text
        self.object = WatsonObject.analyze(text)
        self.keywords = {keyword['text']: keyword['relevance'] for keyword in self.object['keywords']}

    @staticmethod
    def analyze(text):
        response = natural_language_understanding.analyze(
          text=text,
          features=Features(
            keywords=KeywordsOptions()))
        return json.loads(json.dumps(response))