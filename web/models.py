from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.email

class Category(models.Model):
    title = models.CharField(max_length=500)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_by')
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='update_by')
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_create_by')
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_update_by')
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.title

