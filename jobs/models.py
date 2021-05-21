from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class JobPost(models.Model):
    company	= models.CharField(max_length=200,null=True,blank=True)
    joblocation_address = models.CharField(max_length=200,null=True,blank=True)
    jobtitle = models.CharField(max_length=200,null=True,blank=True)
    link=models.URLField(max_length = 200,default=None,null=True)

    class Meta:
        managed = True
        db_table = 'job_post'


class JobApply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    jobid = models.ForeignKey(JobPost,on_delete=models.CASCADE)

    class Meta:
        managed=True
        db_table = 'job_applied'
        
    