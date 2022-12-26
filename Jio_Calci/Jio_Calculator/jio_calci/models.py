from django.db import models

class Category1(models.Model):
    name = models.CharField(max_length=100,blank =100,null = True)
    def __str__(self):
        return self.name

class SubCategory1(models.Model):
    category = models.ForeignKey(Category1,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,blank=100,null=True)
    def __str__(self):
        return self.name

class Product_Name1(models.Model):
    subcategory = models.ForeignKey(SubCategory1,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,blank=100,null =True)
    def __str__(self):
        return self.name

class SKuName1(models.Model):
    productname = models.ForeignKey(Product_Name1,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,blank=100,null =True)
    def __str__(self):
        return self.name
class fixedrate(models.Model):
    skuname = models.ForeignKey(SKuName1,on_delete=models.CASCADE,null=True)
    name = models.FloatField(max_length=1.0,blank=100,null=True)
    def __int__(self):
        return self.name
    
    



        

# Create your models here.
