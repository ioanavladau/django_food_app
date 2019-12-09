from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model): # 1-to-1 relationship, 1 user will have 1 profile
    user = models.OneToOneField(User, on_delete=models.CASCADE) # on user deletion, also delete the profile
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    # adding string representation of the model
    def __str__(self):
        return self.user.username
