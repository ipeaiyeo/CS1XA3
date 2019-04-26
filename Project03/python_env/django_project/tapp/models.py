from django.db import models
from django.contrib.auth.models import User

class UsersInformation(models.Manager):
    def create_user_in(self, username, password, info):
        user = User.objects.create_user(username=username,password=password)
        userinfo = self.create(user=user,info=info)

        return userinfo

class UserInfo(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)

    info = models.CharField(max_length=30)

    objects = UsersInformation()
















