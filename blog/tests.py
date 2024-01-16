from django.test import TestCase

# Create your tests here.
from .models import Post

class BlogTests(TestCase):
    def setUp(self):
        Post.objects.create(
            title="my title",
            body= "body test"
        )
        
    def test_string_representation(self):
        post = Post(title="my title 2")
        self.assertEqual(str(post), post.title)
        
    def test_post_list_view(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "my title")
        self.assertTemplateUsed(response, 'blog/blog.html')
        
    def test_post_detail_view(self):
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "my title")
        self.assertTemplateUsed(response, 'blog/post.html')