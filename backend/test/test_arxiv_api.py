import unittest
from fokus.backend import arxiv_api


class TestArxivAPI(unittest.TestCase):

    def test_next_article_should_return_max_or_less_articles(self):
        g = arxiv_api.next_article("neural", 10)

        self.assertLessEqual(len(list(g)), 10)

    def test_create_query_should_return_well_formed_query(self):
        keywords = ['one', 'two', 'three']

        query = arxiv_api.create_query(keywords)

        self.assertEqual(query, '(all:"one"+OR+all:"two"+OR+all:"three")')

        keywords_yes = ['one', 'two', 'three']
        keywords_no = ['four', 'five', 'six']

        query = arxiv_api.create_query(keywords_yes, keywords_no)

        self.assertEqual(query, '(all:"one"+OR+all:"two"+OR+all:"three")+ANDNOT+(all:"four"+OR+all:"five"+OR+all:"six")')

        keywords_yes = ['one and a half', 'two and three', 'three']
        keywords_no = ['four', 'five and one', 'six']

        query = arxiv_api.create_query(keywords_yes, keywords_no)

        self.assertEqual(query, '(all:"one+and+a+half"+OR+all:"two+and+three"+OR+all:"three")+ANDNOT+(all:"four"'
                                '+OR+all:"five+and+one"+OR+all:"six")')


if __name__ == '__main__':
    unittest.main()