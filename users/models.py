from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
"""*args:
This syntax is used to capture any additional
positional arguments that might be passed to 
the save method. In the context of your code, 
it's not explicitly used within the method 
body. However, it allows your overridden 
save method to accept any arguments that the
original save method might accept.

**kwargs:
Similar to *args, **kwargs captures any additional
keyword arguments that might be passed to the save
method. Again, it's not used explicitly in your
code, but it allows your method to accept any 
keyword arguments that the original save method might
accept."""