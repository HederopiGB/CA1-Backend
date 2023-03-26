from django.test import TestCase
from blog.models import Category, Post, Comment
from django.utils import timezone

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Category1')
        Category.objects.create(name='Category2')

    def test_name_max_length(self):
        # Test if the maximum length of the name field is 20
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_name_label(self):
        # Test if the verbose name of the name field is 'name'
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category = Category.objects.create(name='Category1')
        Post.objects.create(title='Post1', body='Body1', created_on=timezone.now(), last_modified=timezone.now())
        Post.objects.create(title='Post2', body='Body2', created_on=timezone.now(), last_modified=timezone.now())

    def test_title_max_length(self):
        # Test if the maximum length of the title field is 255
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_categories_related_name(self):
        # Test if the related name of the categories field is 'posts'
        category = Category.objects.get(id=1)
        post = Post.objects.get(id=1)
        post.categories.add(category)
        self.assertEquals(category.posts.first(), post)


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category = Category.objects.create(name='Category1')
        post = Post.objects.create(title='Post1', body='Body1', created_on=timezone.now(), last_modified=timezone.now())
        Comment.objects.create(author='Author1', body='Body1', created_on=timezone.now(), post=post)

    def test_post_foreign_key(self):
        # Test if the foreign key to Post in Comment is working properly
        comment = Comment.objects.get(id=1)
        post = Post.objects.get(id=1)
        self.assertEquals(comment.post, post)