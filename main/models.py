from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.


class Illness(models.Model):
    illness_name = models.CharField(max_length=100)
    description=  models.TextField(null=True)
    image = CloudinaryField('image',null=True)
    symptoms = models.TextField(null=True)
    recommndations = models.TextField(null=True)
    
    
    def save_illness(self):
        self.save()

    def delete_illness(self):
        self.delete()
        
    @classmethod
    def get_illness_by_id(cls,id):
        illness = Illness.objects.filter(pk=id)
        return illness
    
    @classmethod
    def search_illness_by_search_term(cls,search_term):
        return cls.objects.filter(name__icontains=search_term).all()
    
    
    def __str__(self):
        return self.illness_name
    
    
class Drug(models.Model):
    drug_name = models.CharField(max_length=100)
    description=  models.TextField(null=True)
    usage_information = models.TextField(null=True)
    side_effects= models.TextField(null=True)
    
    
    def save_drug(self):
        self.save()

    def delete_drug(self):
        self.delete()
        
    @classmethod
    def get_drug_by_id(cls,id):
        drug = Drug.objects.filter(pk=id)
        return drug
    
    @classmethod
    def search_drug_by_search_term(cls,search_term):
        return cls.objects.filter(name__icontains=search_term).all()
    
    
    def __str__(self):
        return self.drug_name



# posted_at = models.DateTimeField(auto_now_add=True, null=True)
