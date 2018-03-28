import unittest
import arxiv_api


class TestArxivAPI(unittest.TestCase):

    def test_next_abstract_should_return_max_or_less_abstracts(self):
        g = arxiv_api.next_abstract("neural", 10)

        self.assertLessEqual(len(list(g)), 10)


if __name__ == '__main__':
    unittest.main()