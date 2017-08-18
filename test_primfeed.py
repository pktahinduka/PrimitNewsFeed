import unittest
import primfeed as pf
from primfeed import Post
from primfeed import Comment

class PrimfeedTestCases(unittest.TestCase):
    def setUp(self):
        self.test_post = Post('test_post_title', 'This is a test body.')
        self.test_comment = Comment(23, 'test_comment_title', 'This is a comment body')
    def test_make_post(self):
        self.assertEqual(pf.make_post(self.test_post.title, self.test_post.body), '<Response [201]>', msg='make_post failed')
    def test_make_comment(self):
        self.assertEqual(pf.make_comment(self.test_comment.post_ID, self.test_comment.title, self.test_comment.body), '<Response [201]>', msg='make_comment failed')
    def test_view_posts(self):
        self.assertTrue(pf.view_posts(), msg='view_posts failed')
