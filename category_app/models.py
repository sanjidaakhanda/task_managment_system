
from django.db import models
# from task_app.models import Task

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    # tasks = models.ManyToManyField(Task)

    def __str__(self):
      return self. categoryName