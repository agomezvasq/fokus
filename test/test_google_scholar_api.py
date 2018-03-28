import unittest
import google_scholar_api


class TestGoogleScholarAPI(unittest.TestCase):

    def test_next_abstract_should_return_max_or_less_abstracts(self):
        g = google_scholar_api.next_abstract("neural", 10)

        self.assertLessEqual(len(list(g)), 10)


if __name__ == '__main__':
    unittest.main()