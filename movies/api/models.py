from django.db import models

class Movies(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.TextField()
    director = models.CharField(max_length=200)
    release_year = models.DateField()

    def __str__(self):
        return self.title
