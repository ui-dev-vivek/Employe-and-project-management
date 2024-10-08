from django.db import models
from config.models import BaseModel
from django.core.validators import FileExtensionValidator

class Organizations(BaseModel):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    description=models.TextField(blank=True)
    logo=models.ImageField(upload_to="organization/logos/",default="default-logo.png",null=True,validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    
    def __str__(self):
        return self.name


# One TO Many Relation : Orinization -> Subsidiary
class Subsidiaries(BaseModel):
    organization=models.ForeignKey(Organizations, on_delete=models.CASCADE,related_name="organization")   
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    description=models.TextField(blank=True)
    logo=models.ImageField(upload_to="subsidiary/logos/",default="default-logo.png",null=True,validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    
    def __str__(self):
        return f"{self.organization.name} - {self.name}"


# One TO Many Relation : Subsidiary -> Budget

class Budgetx(BaseModel):
    subsidiary=models.ForeignKey(Subsidiaries, on_delete=models.CASCADE,related_name="subsidiary")
    year=models.IntegerField()
    ammount=models.FloatField()
    
    
    def __str__(self):
        return f"{self.subsidiary.name} - {self.year}"

