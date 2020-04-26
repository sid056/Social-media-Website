from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Userprofile(models.Model):
    usere = models.OneToOneField(User,on_delete=models.CASCADE)

class Post(models.Model):
    postid = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    post_time = models.DateTimeField(auto_now=True)

class Following_list(models.Model) :
    username = models.ForeignKey(User,related_name="following_list_userid",on_delete=models.CASCADE)
    following = models.ForeignKey(User,related_name="followingid",on_delete=models.CASCADE)

    def following_list(self,user):
        
        result = self.objects.all().filter(username=user)
        return result 

class Follower_list(models.Model)  :
    username = models.ForeignKey(User,related_name="follower_list_userid",on_delete=models.CASCADE)
    follower = models.ForeignKey(User,related_name="followerid" , on_delete=models.CASCADE)

    def follower_list(self,user) :

        result = self.objects.all().filter(username=user)
        return result 


def update_followers(sender , created , instance , **kwargs) :
    if created :
        follower = Follower_list.objects.create(username=instance.following,follower=instance.username)



post_save.connect(update_followers , sender=Following_list)





