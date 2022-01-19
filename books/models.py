from django.db import models

class Authors(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
        
    def __str__(self):
        return self.last_name


class Books(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author_book = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title