from django.shortcuts import render
from jio_calci.models import Category1,SubCategory1,Product_Name1,SKuName1,fixedrate 
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
import json
from jio_calci.templates import *
import xlwt
def dependentField(request):
    category = Category1.objects.all()
    #print(category)
    categoryid = request.GET.get('category',None)
    subcategoryid = request.GET.get('subcategory',None)
    productnameid = request.GET.get('productname',None)
    skunameid = request.GET.get('skuname',None)
    rateid = request.GET.get('FixedRate',None)
    productname = None
    skuname = None
    getcategory =None
    getsubcategory =None
    getproductname =None
    getskuname =None
    rateid =None
    my_items_list =[]
    

    
    #print(my_items_list) 
    addestimate=request.GET.get('addestimate',None)
    if categoryid:
        getcategory = Category1.objects.get(id = categoryid)
        #print(getcategory)
        subcategory = SubCategory1.objects.filter(category= getcategory) 
   
    if subcategoryid:
        getsubcategory = SubCategory1.objects.get(id = subcategoryid)
        #print(getsubcategory)
        productname = Product_Name1.objects.filter(subcategory = getsubcategory)

    if productnameid:
        getproductname = Product_Name1.objects.get(id = productnameid)
        #print(getproductname)
        skuname = SKuName1.objects.filter(productname = getproductname)

    if skunameid:
        getskuname = SKuName1.objects.get(id= skunameid)
        #print(getskuname)
        rateid = fixedrate.objects.values_list('name',flat=True).get(id = skunameid)
        #print(rateid)
    if addestimate:
        my_items = {'category':getcategory,'subcategory':getsubcategory,'productname':getproductname,'skuname':getskuname,'Rate':rateid}
        print(my_items)
        my_items_list.append(my_items)
        


      
        #print("In add items")


    return render(request,'calci.html',locals())
    
    
    

