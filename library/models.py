from django.db import models

# Create your models here.
class  User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)