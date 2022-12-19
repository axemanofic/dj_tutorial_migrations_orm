from django.db import models

# Create your models here.

"""
Post(Статьи)

id          PK int
title       Char
content     Text
created_at  DateTime
photo       "path/to/file"
"""


class Post(models.Model):
    title = models.CharField(null=False, max_length=40)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)
    author = models.ForeignKey("Author", on_delete=models.PROTECT)

    def __repr__(self):
        return f"{self.id} {self.title}"


class Author(models.Model):
    first_name = models.CharField(max_length=150)

    def __repr__(self):
        return f"{self.id} {self.first_name}"
