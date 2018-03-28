import unittest
import watson_nlu
import json


class TestWatsonNLU(unittest.TestCase):

    def test_analyze_with_default_text_should_return_eight_keywords(self):
        text = 'IBM is an American multinational technology company ' \
               'headquartered in Armonk, New York, United States, ' \
               'with operations in over 170 countries.'

        response = json.loads(watson_nlu.analyze(text))

        n_keywords = len(response["keywords"])

        self.assertEqual(n_keywords, 8)