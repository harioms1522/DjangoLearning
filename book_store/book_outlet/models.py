from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.street + ", " + self.city + ", " + self.postal_code
    
    class Meta: 
        verbose_name_plural: "Address"

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "countries"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, related_name="author")

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name() 

class Book(models.Model):
    title = models.CharField(max_length=100)
    ratings = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)

    # One TO Many
    author = models.ForeignKey(to=Author, db_column="author-id", on_delete=models.SET_NULL, null=True, related_name="books")

    # Many TO Many
    # This will create an intermediate table and no on delete operation is allowed here
    published_countries = models.ManyToManyField(Country, related_name="books")

    # overwriting save to add a slug field
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        if(self.slug and self.slug is not ""):
            return reverse("book-detail-slug", kwargs={"slug": self.slug})
        else:
            return reverse("book-detail", kwargs={"book_id": self.id})

    def __str__(self):
        return f"{self.title} ({self.ratings})"