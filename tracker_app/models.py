from django.db import models

# Create your models here.
class Bug(models.Model):
    subject = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    UPVOTE = (
        ('bugs'),
        (' feature requests'),
    )
    upvote = models.CharField(max_length=1, choices=UPVOTE)
    STATUS =  (
        ('todo'),
        ('doing'),
        ('done'),
    )
    status = models.CharField(max_length=1, choices=UPVOTE)
    
class User(models.Model):
      name = models.CharField(max_length=255, blank=True)
      
      def _str_(self):
        return self.name
        
