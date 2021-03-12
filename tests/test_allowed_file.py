import unittest
from brain_scan import app


class TestAllowedFile(unittest.TestCase):
    def test_allowed_file_true(self):
        good_filenames = ['img.jpg', 'img.png', 'img.jpeg', 'img.gif']
        results = [app.allowed_file(filename) for filename in good_filenames]

        self.assertEqual(results, [True, True, True, True])

    def test_allowed_file_false(self):
        bad_filenames = ['imgjpg', 'img.jp', 'imgpng']
        results = [app.allowed_file(filename) for filename in bad_filenames]

        self.assertEqual(results, [False, False, False])
