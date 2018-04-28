import unittest
from app.backend import google_scholar_api


class TestGoogleScholarAPI(unittest.TestCase):

    def test_next_article_should_return_max_or_less_articles(self):
        g = google_scholar_api.next_article("neural", 10)

        self.assertLessEqual(len(list(g)), 10)

    def test_create_query_should_return_well_formed_query(self):
        keywords = ['one', 'two', 'three']

        query = google_scholar_api.create_query(keywords)

        self.assertEqual(query, '"one" OR "two" OR "three"')

        keywords_yes = ['one', 'two', 'three']
        keywords_no = ['four', 'five', 'six']

        query = google_scholar_api.create_query(keywords_yes, keywords_no)

        self.assertEqual(query, '"one" OR "two" OR "three" -"four" -"five" -"six"')

        keywords_yes = ['one and a half', 'two and three', 'three']
        keywords_no = ['four', 'five and one', 'six']

        query = google_scholar_api.create_query(keywords_yes, keywords_no)

        self.assertEqual(query, '"one and a half" OR "two and three" OR "three" -"four" -"five and one" -"six"')


if __name__ == '__main__':
    unittest.main()