from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
def index(request):
    products=Product.objects.all()
    #print(products)
    #n=len(products)
    #nslides=n//4+ceil((n/4)-(n//4))
   # params={'no. of slides':nslides,'product':products,'range':range(1,nslides)}
    #allprods=[[products,range(1,nslides),nslides],
     #         [products, range(1, nslides), nslides]]
    allprods=[]
    catprods=Product.objects.values('category','id')
    print(catprods)
    cats={item['category']for item in catprods}
    print(cats)
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        print(prod)
        n = len(products)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nslides),nslides])
    params = {'allprods': allprods}
    return render(request,"shop/index.html",params)
def about(request):
    return render(request,"shop/about.html")
def contact(request):
    if request.method=="POST":
           name=request.POST.get('name','')
           email=request.POST.get('email','')
           mobile=request.POST.get('mobile','')
           description=request.POST.get('description','')
           contact = Contact(name=name, email=email, mobile=mobile, description=description)
           contact.save()
    return render(request,"shop/contact.html")
def tracker(request):
     if request.method=="POST":
           orderId=request.POST.get('orderId','')
           email=request.POST.get('email','')
           try:
               order=Orders.objects.filter(order_id=orderId,email=email)
               if len(order)>0:
                   update=OrderUpdate.objects.filter(order_id=orderId)
                   updates=[]
                   for item in update:
                       updates.append({'text':item.update_desc,'time':item.timestamp})
                       response=json.dumps(updates,default=str)
                       return HttpResponse(response)
               else:
                    return HttpResponse('error')
           except Exception as e:
                return HttpResponse('error')



     return render(request,"shop/tracker.html")
def searchMatch(query,item):
    if query in item.product_name.lower() or query in item.category.lower() or query in item.description.lower():
         return True
    else:
        return False
def search(request):
    query=request.GET.get('search')
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category']for item in catprods}
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!=0:
            allprods.append([prod,range(1,nslides),nslides])
    params = {'allprods': allprods,"msg":""}
    if len(allprods)==0 or len(query)<4:
        params={"msg":"Please make sure to enter relavant serach query"}
    return render(request,"shop/search.html",params)
def productview(request,myid):
    #Fetch the products using ID
    product = Product.objects.filter(id=myid)
    return render(request,"shop/prodview.html",{'product':product[0]})
def checkout(request):
    if request.method=="POST":
           items_json=request.POST.get('itemsJson','')
           name=request.POST.get('name','')
           email=request.POST.get('email','')
           address=request.POST.get('address1','')+" "+ request.POST.get('address2','')
           city=request.POST.get('city','')
           state=request.POST.get('state','')
           zip_code=request.POST.get('zip_code','')
           phone=request.POST.get('phone','')
           order = Orders(items_json=items_json,name=name, email=email, address=address,city=city,state=state,zip_code=zip_code,phone=phone,)
           order.save()
           update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
           update.save()
           thank=True
           id=order.order_id
           return render(request,"shop/checkout.html",{'thank':thank,'id':id})
    return render(request,"shop/checkout.html")

def list(request):
    listji=Contact.objects.all()
    return render(request,"shop/list.html",{'listji':listji})