from django.db import models
from config.models import BaseModel
from authapp.models import User
from subsidiaries.models import Subsidiaries
from django.core.validators import FileExtensionValidator

class Employees(BaseModel):
    EMP_CHOICES=(
        ('full_time','Full Time'),
        ('part_time','Part Time'),
        ('freelancer','Freelancer'),
                 )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    subsidiary = models.ForeignKey(Subsidiaries,on_delete=models.CASCADE)
    phone_no= models.IntegerField(unique=False)
    emp_type=models.CharField(choices=EMP_CHOICES,max_length=20)
    profile_image=models.ImageField(upload_to='employees/profile_images/',null=True,default='static/profile_images/default.png',validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif','webp'])])
    
    def __str__(self):
        return self.user.username