import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='d8570193-f456-418e-ab20-bae3a783da9c',
  password='pJnMjUVd4yHG',
  version='2018-03-16')


def analyze(text):
    response = natural_language_understanding.analyze(
      text=text,
      features=Features(
        keywords=KeywordsOptions()))
    return json.dumps(response, indent=2)