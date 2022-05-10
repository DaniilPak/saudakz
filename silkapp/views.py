
from decimal import Decimal
from django.shortcuts import render
from .models import *

# Redirect dependencies
from django.http import HttpResponseRedirect
from django.urls import reverse

# Auth dependencies
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Form dependence
from .forms import *
from django.views.generic.edit import FormView
# Multifilter
from django.db.models import Q

# Seria
from django.core import serializers
import json

# Create your views here.

def index(request):
    catalog = Catalog.objects.all()
    all_catalogs = []
    for cat in catalog:
        catalog = cat
        category = Category.objects.filter(catalog=catalog)
        local = [catalog, category]
        all_catalogs.append(local)

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    # Получаем рекомендуемые товары

    last_prods = Product.objects.all()[:20]

    # Получаем категории
    category_object = SubCategory.objects.all()[:15]

    context = {
        'title': 'Каталог товаров - Дерево',
        'all_catalogs': all_catalogs,
        'user': request.user,
        'isauth': isauth,
        'object': category_object,
        'last_prods': last_prods,
    }
    return render(request, 'silkapp/index.html', context)

def category_view(request, slug):
    category = Category.objects.get(slug=slug)
    sub_category = SubCategory.objects.filter(category=category)

    # Breadcumb 
    c_title = str(category.title)
    title = 'Категория ' + c_title
    category_bread = Category.objects.get(slug=slug)

    # Default data for left menu
    catalog = Catalog.objects.all()
    all_catalogs = []
    for cat in catalog:
        catalog = cat
        category = Category.objects.filter(catalog=catalog)
        local = [catalog, category]
        all_catalogs.append(local)

    # is auth?
    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    context = {
        'title': title,
        'desc': title,
        'all_catalogs': all_catalogs,
        'object': sub_category,
        'category_bread': category_bread,

        'user': request.user,
        'isauth': isauth,
    }
    return render(request, 'silkapp/sub_category_overview.html', context)

def products_view(request, slug):
    catalog = Catalog.objects.all()
    all_catalogs = []
    for cat in catalog:
        catalog = cat
        category = Category.objects.filter(catalog=catalog)
        local = [catalog, category]
        all_catalogs.append(local)

    sub_category = SubCategory.objects.get(slug=slug)
    products = Product.objects.filter(sub_category=sub_category)

    # is auth?
    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    title = sub_category.title

    context = {
        'title': title,
        'desc': title,
        'all_catalogs': all_catalogs,
        'products': products,
        'sub_category': sub_category,
        # is auth?
        'user': request.user,
        'isauth': isauth,
    }
    return render(request, 'silkapp/products_overview.html', context)

def product_overview(request, product_slug):
    # Default data for left menu
    catalog = Catalog.objects.all()
    all_catalogs = []
    for cat in catalog:
        catalog = cat
        category = Category.objects.filter(catalog=catalog)
        local = [catalog, category]
        all_catalogs.append(local)

    product = Product.objects.get(slug=product_slug)
    # Check division
    # and fix
    x = product.rate
    second_digit = 0
    srate = '0'

    min = [1, 2, 3, 4]
    max = [6, 7, 8, 9]

    if float(x) % 0.5 == 0:
        pass
    else:
        temp_second_digit = str(x)[2:]
        td = int(temp_second_digit)
        x = int(format(x, '0.0f'))
        if td in min:
            x += 0.5
            srate = str(x)[2:]
        elif td in max:
            srate = '0'

    le = product.comment.all()   

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    context = {
        'product': product,
        'all_catalogs': all_catalogs,
        'commentlength': len(le),
        'isauth': isauth,

        # For rate
        'frate': str(x)[:1],
        'srate': srate,
    }
    return render(request, 'silkapp/product.html', context)


def commentNrate(request, product_slug):
    rate = request.POST['rating']
    commentText = request.POST['comment-text']

    p1 = Product.objects.get(slug=product_slug)
    p1.comment.create(text=commentText, rate=rate, author=request.user.username)
    
    total_rate = Decimal(rate)
    for com in p1.comment.all():
        total_rate += Decimal(com.rate)
    avg = Decimal(total_rate)/Decimal(len(p1.comment.all()) + 1)
    p1.rate = Decimal(avg)
    p1.save()

    return HttpResponseRedirect(reverse('product_overview', kwargs={'product_slug': product_slug}))

def mySign(request):
    return render(request, 'silkapp/sign.html')

def myRegister(request):
    email = request.POST['email']
    name = request.POST['name']
    password = request.POST['password']
    phone = request.POST['phone']
    # seller = request.POST['seller']

    user = User.objects.create_user(email, email, password, first_name=name, last_name=phone)
    user.save()
    login(request, user)

    return HttpResponseRedirect(reverse('index'))

def enterAccount(request):
    user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect(reverse(index))
    else:
        return HttpResponseRedirect(reverse(index))

def myLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))

def mySettings(request):
    catalog = Catalog.objects.all()
    all_catalogs = []
    for cat in catalog:
        catalog = cat
        category = Category.objects.filter(catalog=catalog)
        local = [catalog, category]
        all_catalogs.append(local)

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    context = {
        'all_catalogs': all_catalogs,
        # left menu
        'user': request.user,
        'isauth': isauth,
    }

    return render(request, 'silkapp/settings.html', context)

def myNotifications(request):
    # left menu
    catalog = Catalog.objects.all()
    all_catalogs = []
    for cat in catalog:
        catalog = cat
        category = Category.objects.filter(catalog=catalog)
        local = [catalog, category]
        all_catalogs.append(local)

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    # Notifications hook
    my_notifs = Notification.objects.filter(owner=request.user)

    context = {
        'user': request.user,
        'isauth': isauth,
        'my_notifs': my_notifs,

        'all_catalogs': all_catalogs,
    }

    return render(request, 'silkapp/notifications.html', context)

# if client is buyer
def myBidsView(request):
    # left menu
    catalog = Catalog.objects.all()
    all_catalogs = []
    for cat in catalog:
        catalog = cat
        category = Category.objects.filter(catalog=catalog)
        local = [catalog, category]
        all_catalogs.append(local)

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    cats = Category.objects.all()

    # Hook user's bids
    mybids = Bid.objects.filter(owner=request.user)

    context = {
        'user': request.user,
        'isauth': isauth,
        'cats': cats,
        'mybids': mybids,

        'all_catalogs': all_catalogs,
    }

    return render(request, 'silkapp/bids.html', context)

def addBid(request):
    bidname = request.POST['bidname']
    biddesc = request.POST['biddesc']
    bidtype = request.POST['bidtype']

    # Hooking Category from bidtype
    c1 = Category.objects.get(slug=bidtype)

    b1 = Bid(bidname=bidname,
            biddesc=biddesc,
            bidtype=c1,
            owner=request.user
            )
    b1.save()

    # Hooking all members
    # who have products in
    # this category
    selected_subs = SubCategory.objects.filter(category=c1)
    p1 = Product.objects.filter(sub_category__in=selected_subs)
    actual_owners_with_duplicates = [x.owner for x in p1]
    owners_no_duoplicates = list(set(actual_owners_with_duplicates))
    for x in owners_no_duoplicates:
        n1 = Notification(owner=x, title=bidname, initiator=request.user)
        n1.save()

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    subs = SubCategory.objects.all()

    context = {
        'user': request.user,
        'isauth': isauth,
        'subs': subs,
    }
    return HttpResponseRedirect(reverse('bids'))


def myGoods(request):
    catalog = Catalog.objects.all()
    all_catalogs = []
    for cat in catalog:
        catalog = cat
        category = Category.objects.filter(catalog=catalog)
        local = [catalog, category]
        all_catalogs.append(local)

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    subs = SubCategory.objects.all()

    # get users goods
    u_goods = Product.objects.filter(owner=request.user)

    context = {
        'user': request.user,
        'isauth': isauth,
        'subs': subs,
        'ugoods': u_goods,

        'all_catalogs': all_catalogs,
    }

    return render(request, 'silkapp/goods.html', context)


symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")
tr = {ord(a):ord(b) for a, b in zip(*symbols)}

class ImageFieldFormView(FormView):
    form_class = UploadImageForm
    template_name = ''
    success_url = '/user/goods'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('image')
        # if form is okay
        if form.is_valid():
            # slug from rus to en
            a = request.POST['title']
            a = str(a.translate(tr))
            a = a.replace(' ','-')
            # subcategory select
            sc = SubCategory.objects.get(slug=request.POST['ptype'])
            # create a new Product
            p1 = Product(title=request.POST['title'],
                        price=request.POST['price'],
                        desc=request.POST['desc'],
                        rate=0,
                        sub_category=sc,
                        slug=a,
                        owner=request.user
                        )
            p1.save()

            for f in files:
                pi = ProductImage(img=f)
                pi.save()
                p1.img.add(pi)
   
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def chatView(request):
    catalog = Catalog.objects.all()
    all_catalogs = []
    for cat in catalog:
        catalog = cat
        category = Category.objects.filter(catalog=catalog)
        local = [catalog, category]
        all_catalogs.append(local)
    
    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    # Get user's chats 
    myChats = ChatFriends.objects.filter(friend1=request.user)

    context = {
        'user': request.user,
        'isauth': isauth,
        # ... chats
        'mychats': myChats,

        'all_catalogs': all_catalogs,
    }

    return render(request, 'silkapp/chat.html', context)

def chatUser(request, username):
    catalog = Catalog.objects.all()
    all_catalogs = []
    for cat in catalog:
        catalog = cat
        category = Category.objects.filter(catalog=catalog)
        local = [catalog, category]
        all_catalogs.append(local)

    # Get user's chats 
    myChats = ChatFriends.objects.filter(friend1=request.user)
    uInChats = ChatFriends.objects.filter(friend2=request.user)

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    usr = User.objects.get(username=username)

    # Get messages involved
    msgs = ChatMessage.objects.filter(Q(sender=request.user) | Q(receiver=request.user)).filter(Q(sender=usr) | Q(receiver=usr)).order_by('time')

    context = {
        'user': request.user,
        'isauth': isauth,
        'usr': usr,
        'msgs': msgs,
        # ... chats
        'mychats': myChats,
        'uinchats': uInChats,

        'all_catalogs': all_catalogs,
    }

    return render(request, 'silkapp/chatuser.html', context)\
        

def addMsg(request, username):
    usr = User.objects.get(username=username)
    # new msg
    if request.method == 'POST' and request.POST['message'].strip() != '':
        newmsgtxt = request.POST['message']
        try:
            nmsg = ChatMessage(sender=request.user, receiver=usr, text=newmsgtxt)
            nmsg.save()
            return HttpResponseRedirect(reverse('chatuser', kwargs={'username': usr.username}))
        except BaseException:
            return HttpResponseRedirect(reverse('chatuser', kwargs={'username': usr.username}))
    else: 
        return HttpResponseRedirect(reverse('chatuser', kwargs={'username': usr.username}))

def contactButton(request, username):
    usr_to_contact = User.objects.get(username=username)
    chat_friend = ChatFriends(friend1=request.user, friend2=usr_to_contact)
    chat_friend.save()
    chat_friend2 = ChatFriends(friend2=request.user, friend1=usr_to_contact)
    chat_friend2.save()
    return HttpResponseRedirect(reverse('chatuser', kwargs={'username': usr_to_contact.username}))

# Search 

def productSearch(request):

    res = request.GET['keyword']
    res = str(res).lower()

    search_results = Product.objects.filter(title__icontains=res)[:7]

    json_data_object = serializers.serialize('json', search_results)

    context = {
        'data': json_data_object,
    }

    return render(request, 'silkapp/api.html', context)