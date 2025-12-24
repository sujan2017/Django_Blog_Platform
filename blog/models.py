from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)



class Tag(models.Model):
    name=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag, blank=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published=models.BooleanField(default=True)

    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug= slugify(self.title)
            slug=base_slug
            counter=1

            while Post.objects.filter(slug=slug).exists():
                slug= f"{base_slug}-{counter}"
                counter +=1

            self.slug=slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    profile_pic=models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username



