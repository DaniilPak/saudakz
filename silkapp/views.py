
from decimal import Decimal
from re import sub
from unicodedata import category
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

import requests

def send_simple_message(mail_to, subject, message):
	return requests.post(
		"https://api.mailgun.net/v3/nsk-candies.paksol.ru/messages",
		auth=("api", "b2cda00c72ac874ace95d624c939ed75-100b5c8d-5a314c32"),
		data={"from": "Daniil Pak from Сауда.kz <daniilpak@nsk-candies.paksol.ru>",
			"to": [mail_to, "daniilpak@nsk-candies.paksol.ru"],
			"subject": subject,
			"html": message })

# Create your views here.

def index(request):

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    # Email sending
    #text1 = 'Some custom text'
    #text2 = 'Denchik krut eldar net'
    #html_code = '<!DOCTYPE html><html lang="en" dir="ltr" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" style="color-scheme:light dark;supported-color-schemes:light dark;"><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width,initial-scale=1 user-scalable=yes"><meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no"><meta name="x-apple-disable-message-reformatting"><meta name="color-scheme" content="light dark"><meta name="supported-color-schemes" content="light dark"><title></title><!--[if mso]> <noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]--><!--[if mso]><style>table,tr,td,p,span,a{mso-line-height-rule:exactly !important;line-height:120% !important;mso-table-lspace:0 !important;mso-table-rspace:0 !important;}</style><![endif]--><style>a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}u+#body a{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}#MessageViewBody a{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}:root{color-scheme:light dark;supported-color-schemes:light dark;}tr{vertical-align:middle;}p,a,li{color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;}p:first-child{margin-top:0!important;}p:last-child{margin-bottom:0!important;}a{text-decoration:underline;font-weight:bold;color:#0000ff}@media only screen and (max-width:599px){.full-width-mobile{width:100%!important;height:auto!important;}.mobile-padding{padding-left:10px!important;padding-right:10px!important;}.mobile-stack{display:block!important;width:100%!important;}}@media (prefers-color-scheme:dark){body,div,table,tr,td{background-color:#000000!important;color:#ffffff!important;}.content{background-color:#222222!important;}p,li{color:#B3BDC4!important;}a{color:#84cfe2!important;}}</style></head><body class="body" style="background-color:#f4f4f4;"><div style="display:none;font-size:1px;color:#f4f4f4;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"></div><span style="display:none!important;visibility:hidden;mso-hide:all;font-size:1px;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</span><div role="article" aria-roledescription="email" aria-label="Your Email" lang="en" dir="ltr" style="font-size:16px;font-size:1rem;font-size:max(16px,1rem);background-color:#f4f4f4;"><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse;max-width:600px;width:100%;background-color:#f4f4f4;"><tr style="vertical-align:middle;" valign="middle"><td><!--[if mso]><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse:collapse;"><tr><td align="center"></td></tr><tr style="vertical-align:middle;" valign="middle"><td align="center" style="padding:30px 0;"><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse:collapse;max-width:600px;width:100%;background-color:#fffffe;"><tr style="vertical-align:middle;" valign="middle"><td align="center" style="padding:30px;" class="content"><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse:collapse;max-width:600px;width:100%;background-color:#fffffe;"><tr style="vertical-align:middle;" valign="middle"><td class="content"><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;margin-top:0!important;">' + text1 + '</p><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;">' + text2 + '</p><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;"><a href="https://сауда.kz/" style="font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;text-decoration:underline;font-weight:bold;color:#0000ff;">Перейти на сайт Сауда.kz&nbsp;</a></p><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;margin-bottom:0!important;">&mdash; С уважением, команда&nbsp;Сауда.kz</p></td></tr></table></td></tr></table></td></tr></table></td></tr><!--[if mso]></td></tr></table></table></div></body></html>'
    #send_simple_message(request.user.email, 'Eldar', message=html_code)
    # email sending end

    # Получаем рекомендуемые товары

    last_prods = Product.objects.all()[:20]

    # Получаем Сабкатегории
    category_object = SubCategory.objects.all()[:15]

    # Категории получаем
    categories = Category.objects.all()

    context = {
        'title': 'Каталог товаров - Дерево',
        'categories': categories,
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

    categories = Category.objects.all()

    # is auth?
    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    context = {
        'title': title,
        'desc': title,
        'categories': categories,
        'object': sub_category,
        'category_bread': category_bread,

        'user': request.user,
        'isauth': isauth,
    }
    return render(request, 'silkapp/sub_category_overview.html', context)

def products_view(request, slug):

    sub_category = SubCategory.objects.get(slug=slug)
    products = Product.objects.filter(sub_category=sub_category)

    # is auth?
    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    title = sub_category.title

    # Getting categories
    categories = Category.objects.all()

    context = {
        'title': title,
        'desc': title,
        'categories': categories,
        'products': products,
        'sub_category': sub_category,
        # is auth?
        'user': request.user,
        'isauth': isauth,
    }
    return render(request, 'silkapp/products_overview.html', context)

def product_overview(request, product_slug):

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

    # Categories getting
    categories = Category.objects.all()

    context = {
        'product': product,
        'categories': categories,
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

    # Add rate to user's profile 
    ud = UserData.objects.get(owner=p1.owner)
    ud.commentnrate.create(text=commentText, rate=rate, author=request.user.username)
    # user's rate
    total_rate2 = Decimal(rate)
    for com in ud.commentnrate.all():
        total_rate2 += Decimal(com.rate)
    avg2 = Decimal(total_rate2)/Decimal(len(ud.commentnrate.all()) + 1)
    ud.rate = Decimal(avg2)
    # end rate user's profile

    ud.save()

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

    # Create User Data
    user_data = UserData.objects.create(owner=user)
    user_data.save()

    # Email sending
    text1 = 'Вы зарегистрировались на сайте - Сауда.kz!'
    text2 = 'Добро пожаловать, ' + name + '!' + '<br>Размещайте свои товары, или ищите нужные вам быстро и бесплатно.'
    html_code = '<!DOCTYPE html><html lang="en" dir="ltr" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" style="color-scheme:light dark;supported-color-schemes:light dark;"><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width,initial-scale=1 user-scalable=yes"><meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no"><meta name="x-apple-disable-message-reformatting"><meta name="color-scheme" content="light dark"><meta name="supported-color-schemes" content="light dark"><title></title><!--[if mso]> <noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]--><!--[if mso]><style>table,tr,td,p,span,a{mso-line-height-rule:exactly !important;line-height:120% !important;mso-table-lspace:0 !important;mso-table-rspace:0 !important;}</style><![endif]--><style>a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}u+#body a{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}#MessageViewBody a{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}:root{color-scheme:light dark;supported-color-schemes:light dark;}tr{vertical-align:middle;}p,a,li{color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;}p:first-child{margin-top:0!important;}p:last-child{margin-bottom:0!important;}a{text-decoration:underline;font-weight:bold;color:#0000ff}@media only screen and (max-width:599px){.full-width-mobile{width:100%!important;height:auto!important;}.mobile-padding{padding-left:10px!important;padding-right:10px!important;}.mobile-stack{display:block!important;width:100%!important;}}@media (prefers-color-scheme:dark){body,div,table,tr,td{background-color:#000000!important;color:#ffffff!important;}.content{background-color:#222222!important;}p,li{color:#B3BDC4!important;}a{color:#84cfe2!important;}}</style></head><body class="body" style="background-color:#f4f4f4;"><div style="display:none;font-size:1px;color:#f4f4f4;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"></div><span style="display:none!important;visibility:hidden;mso-hide:all;font-size:1px;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</span><div role="article" aria-roledescription="email" aria-label="Your Email" lang="en" dir="ltr" style="font-size:16px;font-size:1rem;font-size:max(16px,1rem);background-color:#f4f4f4;"><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse;max-width:600px;width:100%;background-color:#f4f4f4;"><tr style="vertical-align:middle;" valign="middle"><td><!--[if mso]><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse:collapse;"><tr><td align="center"></td></tr><tr style="vertical-align:middle;" valign="middle"><td align="center" style="padding:30px 0;"><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse:collapse;max-width:600px;width:100%;background-color:#fffffe;"><tr style="vertical-align:middle;" valign="middle"><td align="center" style="padding:30px;" class="content"><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse:collapse;max-width:600px;width:100%;background-color:#fffffe;"><tr style="vertical-align:middle;" valign="middle"><td class="content"><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;margin-top:0!important;">' + text1 + '</p><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;">' + text2 + '</p><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;"><a href="https://сауда.kz/" style="font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;text-decoration:underline;font-weight:bold;color:#0000ff;">Перейти на сайт Сауда.kz&nbsp;</a></p><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;margin-bottom:0!important;">&mdash; С уважением, команда&nbsp;Сауда.kz</p></td></tr></table></td></tr></table></td></tr></table></td></tr><!--[if mso]></td></tr></table></table></div></body></html>'
    send_simple_message(email, 'Спасибо за регистрацию!', message=html_code)
    # email sending end

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

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    # Ctg get
    categories = Category.objects.all()
    
    context = {
        'categories': categories,
        # left menu
        'user': request.user,
        'isauth': isauth,
    }

    return render(request, 'silkapp/settings.html', context)

def myNotifications(request):

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    # Notifications hook
    my_notifs = Notification.objects.filter(owner=request.user)

    # Ctg
    categories = Category.objects.all()

    context = {
        'user': request.user,
        'isauth': isauth,
        'my_notifs': my_notifs,

        'categories': categories,
    }

    return render(request, 'silkapp/notifications.html', context)

# if client is buyer
def myBidsView(request):

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    cats = Category.objects.all()

    # Hook user's bids
    mybids = Bid.objects.filter(owner=request.user)

    # Ctg
    categories = Category.objects.all()

    context = {
        'user': request.user,
        'isauth': isauth,
        'cats': cats,
        'mybids': mybids,

        'categories': categories,
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
        # Email sending
        text1 = 'Заявка: ' + bidname + ' <br> ' + biddesc
        text2 = 'Email заявителя: ' + request.user.first_name + '<br>' + 'Номер телефона заявителя: ' + request.user.last_name
        html_code = '<!DOCTYPE html><html lang="en" dir="ltr" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" style="color-scheme:light dark;supported-color-schemes:light dark;"><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width,initial-scale=1 user-scalable=yes"><meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no"><meta name="x-apple-disable-message-reformatting"><meta name="color-scheme" content="light dark"><meta name="supported-color-schemes" content="light dark"><title></title><!--[if mso]> <noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]--><!--[if mso]><style>table,tr,td,p,span,a{mso-line-height-rule:exactly !important;line-height:120% !important;mso-table-lspace:0 !important;mso-table-rspace:0 !important;}</style><![endif]--><style>a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}u+#body a{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}#MessageViewBody a{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}:root{color-scheme:light dark;supported-color-schemes:light dark;}tr{vertical-align:middle;}p,a,li{color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;}p:first-child{margin-top:0!important;}p:last-child{margin-bottom:0!important;}a{text-decoration:underline;font-weight:bold;color:#0000ff}@media only screen and (max-width:599px){.full-width-mobile{width:100%!important;height:auto!important;}.mobile-padding{padding-left:10px!important;padding-right:10px!important;}.mobile-stack{display:block!important;width:100%!important;}}@media (prefers-color-scheme:dark){body,div,table,tr,td{background-color:#000000!important;color:#ffffff!important;}.content{background-color:#222222!important;}p,li{color:#B3BDC4!important;}a{color:#84cfe2!important;}}</style></head><body class="body" style="background-color:#f4f4f4;"><div style="display:none;font-size:1px;color:#f4f4f4;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"></div><span style="display:none!important;visibility:hidden;mso-hide:all;font-size:1px;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;"> &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</span><div role="article" aria-roledescription="email" aria-label="Your Email" lang="en" dir="ltr" style="font-size:16px;font-size:1rem;font-size:max(16px,1rem);background-color:#f4f4f4;"><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse;max-width:600px;width:100%;background-color:#f4f4f4;"><tr style="vertical-align:middle;" valign="middle"><td><!--[if mso]><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse:collapse;"><tr><td align="center"></td></tr><tr style="vertical-align:middle;" valign="middle"><td align="center" style="padding:30px 0;"><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse:collapse;max-width:600px;width:100%;background-color:#fffffe;"><tr style="vertical-align:middle;" valign="middle"><td align="center" style="padding:30px;" class="content"><table align="center" role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse:collapse;max-width:600px;width:100%;background-color:#fffffe;"><tr style="vertical-align:middle;" valign="middle"><td class="content"><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;margin-top:0!important;">' + text1 + '</p><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;">' + text2 + '</p><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;"><a href="https://сауда.kz/" style="font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;text-decoration:underline;font-weight:bold;color:#0000ff;">Перейти на сайт Сауда.kz&nbsp;</a></p><p style="color:#000000;font-size:16px;mso-line-height-rule:exactly;line-height:24px;font-family:Arial,sans-serif;margin-bottom:0!important;">&mdash; С уважением, команда&nbsp;Сауда.kz</p></td></tr></table></td></tr></table></td></tr></table></td></tr><!--[if mso]></td></tr></table></table></div></body></html>'
        send_simple_message(x.email, 'Eldar', message=html_code)
        # email sending end
        
        # Creating Notification
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

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    # For adding item
    categories = Category.objects.all()

    # get users goods
    u_goods = Product.objects.filter(owner=request.user)

    # ctg
    categories = Category.objects.all()

    context = {
        'user': request.user,
        'isauth': isauth,
        'categories': categories,
        'ugoods': u_goods,

        'categories': categories,
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
            sc = SubCategory.objects.get(id=request.POST['ptype'])
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
    
    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    # Get user's chats 
    myChats = ChatFriends.objects.filter(friend1=request.user)

    # Ctg
    categories = Category.objects.all()

    context = {
        'user': request.user,
        'isauth': isauth,
        # ... chats
        'mychats': myChats,

        'categories': categories,
    }

    return render(request, 'silkapp/chat.html', context)

def chatUser(request, username):

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

    categories = Category.objects.all()

    context = {
        'user': request.user,
        'isauth': isauth,
        'usr': usr,
        'msgs': msgs,
        # ... chats
        'mychats': myChats,
        'uinchats': uInChats,

        'categories': categories,
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

# Choose category

def chooseCategory(request):

    id = request.GET['id']
    id = int(id)

    category = Category.objects.get(id=id)
    search_results = SubCategory.objects.filter(category=category)

    json_data_object = serializers.serialize('json', search_results)

    context = {
        'data': json_data_object,
    }

    return render(request, 'silkapp/api.html', context)

def chooseSubCategory(request):

    id = request.GET['id']
    id = int(id)

    category = Category.objects.get(id=id)
    search_results = SubCategory.objects.filter(category=category)

    json_data_object = serializers.serialize('json', search_results)

    context = {
        'data': json_data_object,
    }

    return render(request, 'silkapp/api.html', context)

# Profile

def profile(request, username):

    # Profile
    profile = User.objects.get(username=username)

    if request.user.is_authenticated:
        isauth = True
    else: 
        isauth = False

    ud = UserData.objects.get(owner=profile)

    # Check division
    # and fix
    x = ud.rate
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
    # end division fix

    categories = Category.objects.all()

    context = {
        'title': 'Каталог товаров - Дерево',
        'categories': categories,
        'user': request.user,
        'isauth': isauth,

        'profile': profile,
        'userdata': ud,

        # For rate
        'frate': str(x)[:1],
        'srate': srate,
    }

    return render(request, 'silkapp/profile.html', context)




