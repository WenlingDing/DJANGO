from django.db import models

# Create your models here.
class Issue(models.Model):
    subject = models.CharField(max_length=255, blank=False)
    date_published = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    def _str_(self):
        return self.name
    
class User(models.Model):
      name = models.CharField(max_length=255, blank=True)
      issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='user_issue', null=True)
      def _str_(self):
        return self.name
        
class Status(models.Model):
      STATUS =  (
        ('1','todo'),
        ('2','doing'),
        ('3','done'),
       )
      status = models.CharField(max_length=1, choices=STATUS)
      def _str_(self):
        return self.status
        
class IssueAtt(models.Model):
      TYPE = (
        ('1','bugs'),
        ('2','feature requests'),
    )
      type = models.CharField(max_length=1, choices=TYPE)
      minimum_amount = models.PositiveIntegerField(default=0.0)
      def _str_(self):
        return self.name
