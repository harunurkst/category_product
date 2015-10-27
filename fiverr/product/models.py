from django.db import models
from PIL import Image

#category model

class Category(models.Model):
    name = models.CharField('name',max_length=125)
    slug = models.SlugField('slug', unique=True)
    description = models.TextField('description')
    photo = models.ImageField(upload_to="media/",blank=True,null=True)

    def __str__(self):
        return self.name
 
#product model 
        
class MainProduct(models.Model):
	name = models.CharField(max_length=125)
	slug = models.SlugField(unique=True,max_length=255)
	description = models.TextField()
	categories = models.ForeignKey(Category,null=True)
	photo = models.ImageField(upload_to="media/", blank=True,null=True)
	price = models.IntegerField(blank=True,null=True)
	date = models.DateTimeField(auto_now=True, blank=True,null=True)
	YES = 'Y'
	NO = 'N'
	FOR_SALE = (
		(YES,'Yes'),
		(NO,'No'),
	)
	for_sale = models.CharField(max_length=2,
								choices=FOR_SALE,
								default=NO)
	
	class Meta:
		ordering = ['-date']
	
        
	def __str__(self):
		return self.name 
		
   
   
   
   
   
        

