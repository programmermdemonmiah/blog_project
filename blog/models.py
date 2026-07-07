from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=False, null=False)
    content = RichTextField()
    image = models.ImageField(upload_to="blog/", null=True, blank=True)
    status = models.CharField(choices={
        'Published': 'Published',
        'Unpublished': 'Unpublished'
    })
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def slug_make(self):
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1

        while Blog.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def save(self, *args, **keywords):
        if not self.slug:
            self.slug = self.slug_make()
        super().save(*args, **keywords)

    class Meta: 
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = "Blogs"
    