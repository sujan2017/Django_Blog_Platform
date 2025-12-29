from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category, Comment

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.category = Category.objects.create(name="Tech")

        self.post = Post.objects.create(
            category=self.category,
            title="Test Post",
            content="This is a test post",
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")

    def test_comment_creation(self):
        comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            content="Nice Post"
        )
        self.assertEqual(comment.content, "Nice Post")

    def test_post_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)