from django.db import models
from django.utils import timezone
from django.conf import settings


class Category(models.Model):

    name = models.CharField(max_length=100)
    # here we return a string representation
    # for instance, in a database 
    def __str__(self):
        return self.name 


class Post(models.Model):
    # managing the filtering of displaying only posts
    # that have been published 
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # one_delete=models.PROTECT is added here so no category can ever be deleted 
    # to define many-toone relationship, we use ForeignKey 
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.CharField(max_length=10, choices=options, default='published')

    # Managers are interfaces through which database query operations are provided to Django models. 
    # every model in Django has at least one Manager.

    # renaming default manager
    objects = models.Manager() 
    # custom manager
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published', )

    def __str__(self):
        return self.title 