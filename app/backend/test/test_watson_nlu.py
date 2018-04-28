import unittest
from app.backend import watson_nlu


class TestWatsonNLU(unittest.TestCase):

    def test_analyze_with_default_text_should_return_eight_keywords(self):
        text = 'IBM is an American multinational technology company ' \
               'headquartered in Armonk, New York, United States, ' \
               'with operations in over 170 countries.'

        watson_object = watson_nlu.WatsonObject(text)

        n_keywords = len(watson_object.keywords)

        self.assertEqual(n_keywords, 8)