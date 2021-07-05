from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)

  def __str__(self):
      return self.name

class Photo(models.Model):
  # if a category is deleted the photo is not deleted. Its just set to NULL
  category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True, blank=True)
  image = models.ImageField(null=False, blank=False)
  description = models.TextField()

  def __str__(self):
      return self.description