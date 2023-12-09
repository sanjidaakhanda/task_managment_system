from django.db import models
from datetime import date
from category_app.models import Category
from task_author.models import Author

class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_Assign_Date = models.DateField(default=date.today)
    Category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
     return self.taskTitle
   
