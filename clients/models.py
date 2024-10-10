from django.db import models
from config.models import BaseModel
from authapp.models import User
from subsidiaries.models import Subsidiaries
from django.core.validators import FileExtensionValidator

class Clients(BaseModel):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    subsidiary=models.ForeignKey(Subsidiaries,on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    phone_no = models.IntegerField(unique=False)
    profile_image=models.ImageField(upload_to='clients/profile_images/',null=True,default='static/profile_images/default.png',validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif','webp'])])
    
    
    def __str__(self):
        return self.user.first_name
                                                                                
                                                                                                                                     
