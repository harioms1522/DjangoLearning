from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=500)
    image =  models.CharField(max_length=50)
    date = models.DateField()
    slug = models.SlugField(db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(*args, **kwargs).save()
        


    def get_absolute_url(self):
        return reverse("single-post", kwargs={"slug": self.slug})
    

    def __str__(self) -> str:
        return f"{self.title}"

