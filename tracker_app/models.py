from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create status about issue.       
class Status(models.Model):
      status = models.CharField(max_length=255, default='to do')
      
      def __str__(self):
          return self.status
        
class Issue(models.Model):
    subject = models.CharField(max_length=255, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=False)
# Create 2 types of issues, and each issue have a minimum cost, for bugs set it to 0, for feature request developer can change the amount.    
    # TYPE = (
    #     ('1','bugs'),
    #     ('2','feature requests')
    # )
    
    upvote=models.IntegerField(default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status_issue',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_issue', null=False)
    def _str_(self):
        return self.subject
        
              
# each user upvote in type2, they need input liketopay amount,when upvote bugs,liketopay default 0.
class Feature(models.Model):
        subject = models.CharField(max_length=255, blank=False)
        date = models.DateTimeField(auto_now_add=True)
        description = models.CharField(max_length=255, blank=False)
        paid = models.PositiveIntegerField(default=0.0)
        upvote=models.IntegerField(default=0)
        status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status_feature',null=True, blank=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_feature', null=False)
        def _str_(self):
            return self.subject

      
