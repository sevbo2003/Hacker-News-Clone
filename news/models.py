from django.db import models
from accounts.models import CustomUser


class News(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='likes', null=True, blank=True)
    savers = models.ManyToManyField(CustomUser, related_name='savers', null=True, blank=True)
    point = models.IntegerField(default=1)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'News'
        verbose_name = 'news'

    def get_absolute_url(self):
        return f"item/{self.id}/"

    def points(self):
        like_point = self.likes.count()
        comment_point = self.comments.all().count() * 2
        return like_point + comment_point

    def number_of_likes(self):
        return self.likes.count()

    def get_link(self):
        if self.url:
            link = self.url.split('/')
            return link[2]

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    text = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.news) + ' | ' + str(self.author)

    class Meta:
        ordering = ('-created',)
