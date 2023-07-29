from django.db import models




class PostType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Posts(models.Model):
    post_type = models.ForeignKey(PostType , on_delete=models.CASCADE , null=True , blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')