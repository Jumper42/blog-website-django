from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=150)
    image = models.ImageField(upload_to="images/", null=True)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(20)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, related_name="post")

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    email = models.EmailField()
    text = models.TextField(
        validators=[MinLengthValidator(10), MaxLengthValidator(500)])
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
