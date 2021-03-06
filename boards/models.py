from django.db import models
from users.models import CustomUser
# Create your models here.
class SubReddits(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name+'-'+str(self.created_at)

class Posts(models.Model):
    board=models.ForeignKey(SubReddits,on_delete=models.CASCADE,related_name='PostBoard')
    text = models.CharField(max_length=200)
    detail = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    author=models.CharField(max_length=200,default='')

    def __str__(self):
        return self.text + '-' + str(self.created_at)

class Comments(models.Model):
    from_user = models.CharField(max_length=200, default='')
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='CommentPost')
    text=models.TextField()
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.from_user)+'-'+str(self.created_at)

class Subscriptions(models.Model):
    user_id = models.CharField(max_length=200, default='')
    Boards_id=models.ForeignKey(SubReddits,on_delete=models.CASCADE,related_name='SubsBoard')

    def __str__(self):
        return str(self.user_id) + '-' + str(self.Boards_id)

class Votes(models.Model):
    from_id = models.CharField(max_length=200, default='')
    comment_id=models.ForeignKey(Comments,on_delete=models.CASCADE,null=True,blank=True,related_name='VoteComment')    
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, blank=True, related_name='VotePost')
    value=models.IntegerField(default=0)

    def __str__(self):
        return str(self.from_id)+'-'+str(self.value)
