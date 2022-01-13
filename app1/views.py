from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views.generic import TemplateView
from app1.models import *


class Home(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "home.html")


class Products(TemplateView):
    def get(self, request, **kwargs):
        context = dict()
        list_data = list(
            Product.objects.values('title', 'mrp', 'buy_price', 'sell_price', 'code', 'is_delete', 'item',
                                   'merchant_id','bill_no','margin','sold_out','created_at'))
        print(list_data)

        for i in list_data:
            m_name = Merchant.objects.filter(id=i["merchant_id"]).values("name")
            if m_name:
                list_data[list_data.index(i)].update({"merchant_name": m_name[0]["name"]})
            else:
                list_data[list_data.index(i)].update({"merchant_name": None})
            try:
                pl = float(i["sell_price"]) - (float(i["mrp"] * i['item']))
                list_data[list_data.index(i)].update({"profit": pl})
            except Exception:
                list_data[list_data.index(i)].update({"profit": None})
                pass
        context["video_data"] = list_data
        return render(request, "product.html", context=context)


class AddProduct(TemplateView):
    def get(self, request, **kwargs):
        context = dict()
        merchants = Merchant.objects.values("name", "code")
        context["merchants"] = merchants
        return render(request, "product_add.html", context=context)

    def post(self, request, **kwargs):
        buy = float(request.POST.get("buy"))
        margin = float(request.POST.get("margin"))
        mrp = float(request.POST.get("mrp"))
        title = request.POST.get("title")
        merchantss = Merchant.objects.filter(code=request.POST.get("merchant"), is_delete=False).first()
        item = request.POST.get("items")
        bill_no = request.POST.get("bill_no")
        code = get_random_string(length=10, allowed_chars=title.replace(" ", '')).lower()
        product_obj = Product(buy_price=buy, mrp=mrp, title=title, code=code, item=int(item),bill_no=bill_no,margin=margin)
        product_obj.merchant = merchantss
        product_obj.save()
        messages.info(request, "Successfully subscribe it.")
        return redirect("/product/")


class UpdateProduct(TemplateView):
    def get(self, request, **kwargs):
        code = request.GET.get("code")
        list_data = Product.objects.values('title', 'mrp', 'buy_price', 'sell_price', 'code', 'item').filter(
            code=code)
        context = {"datas": list_data[0]}
        return render(request, "update.html", context=context)

    def post(self, request, **kwargs):

        delete_code = request.POST.get("delete_code")
        if delete_code:
            Product.objects.filter(code=delete_code).update(is_delete=True)
            messages.info(request, "Deleted successfully")
        else:
            code = request.GET.get("code")
            sell = request.POST.get("sell")
            Product.objects.filter(code=code).update(sell_price=sell)
        return redirect("/product/")


class Merchants(TemplateView):
    def get(self, request, **kwargs):
        details = list(Merchant.objects.values("code", 'name', 'address', 'mo_number', 'gst_number', 'created_at'))
        print(details)
        context = dict()
        context["m_detail"] = details
        return render(request, "merchant.html", context=context)


class MerchantDetail(TemplateView):
    def get(self, request, **kwargs):
        context = dict()
        merchant_code = kwargs.get("code")
        merchant_details = Merchant.objects.filter(code=merchant_code).values('name', 'address', 'mo_number', 'gst_number', 'created_at','id')
        print(merchant_details)
        if merchant_details:
            merchant_product_detail = Product.objects.filter(merchant_id=int(merchant_details[0]['id'])).values('title', 'mrp', 'buy_price', 'sell_price', 'code', 'is_delete', 'item',)
            context["mp_detail"] = merchant_details[0]
            context["video_data"] = merchant_product_detail
        else:
            context["wrong"] = True
            context["message"] = "Sorry you are entered wrong detail."
        return render(request, "merchant_detail.html", context=context)


class AddMerchant(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "merchant_add.html")

    def post(self, request, **kwargs):
        name = request.POST.get("name")
        address = request.POST.get("address")
        mo_number = request.POST.get("mo_number")
        gst_number = request.POST.get("gst_number")
        code = get_random_string(length=10, allowed_chars=name.replace(" ", '')).lower()
        Merchant(name=name, address=address, mo_number=mo_number, code=code, gst_number=gst_number).save()
        messages.info(request, "Successfully subscribe it.")
        return redirect("/merchant/")
