from django.db import models
from katysite.models import MainMenu


class CoachMenu(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(null=False, unique=True)
    main_page = models.ForeignKey(MainMenu, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']


class Category(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    post_body = models.TextField(default='')
    comments_mode = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'post_date', 'category']


class PostData(models.Model):
    post = models.OneToOneField(Post, on_delete=models.PROTECT)
    images = models.ImageField(upload_to=f'images/coach/post_{post.primary_key}/')


class PostComments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    author = models.CharField(max_length=90)
    comment = models.TextField()
    comment_date = models.DateField(auto_now_add=True)
    author_ip = models.CharField(max_length=255)


# class PostLikes(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.PROTECT)
#     like_count = models.IntegerField(default=0)
#     user_cookie = models.JSONField(verbose_name='user_cookie')
