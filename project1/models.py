from django.db import models

class CustomPostManager (models.Manager):
    def get_queryset(self):
        qs = super().get_queryset().filter(title = 'cool post')
        return qs

class Author(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Post(models.Model):
    class Choices(models.TextChoices):
        published = 'pb', 'published'
        draft = 'dr', 'draft'
        rejected = 'rj', 'rejected'

    title = models.CharField(max_length=250)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=Choices.choices, default=Choices.draft)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()
    contain_post = CustomPostManager()
    def __str__(self):
        return self.title

class Ticket(models.Model):
    class Choices(models.TextChoices):
        bog = 'bog', 'bog'
        principle = 'pirincimpe', 'pirincimpe'
        nothing = 'nothing', 'nothing'
    name = models.CharField(max_length=250)
    email = models.EmailField()
    description = models.TextField()
    type = models.CharField(choices=Choices.choices )

class Comment (models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)