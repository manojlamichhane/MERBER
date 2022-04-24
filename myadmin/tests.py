from django.test import TestCase
from myadmin.models import User
from myadmin.models import Category
from myadmin.models import Product
from myadmin.models import Orders
from myadmin.models import OrderDetail
from datetime import datetime
# Create your tests here.

class test_models (TestCase):
    def test_createuser(self):
        user = User.objects.create(username="username",password="password",email="sample@sample.com",address="1234",status="1",create_at = datetime.now(),update_at =datetime.now())
        user.save()
        self.assertEqual(str(user),"username")

    def test_createcategory(self):
        category = Category.objects.create(shop_id ="1",name="general",status="1",create_at = datetime.now(),update_at =datetime.now())
        category.save()
        self.assertEqual(str(category),"general")

    def test_createproduct(self):
        product = Product.objects.create(shop_id ="1",category_id ="2",cover_pic= "sdjsdjkjnksdjk",name="Acyclovir",price="20",status="1",create_at = datetime.now(),update_at =datetime.now())
        product.save()
        self.assertEqual(str(product),"Acyclovir")        

    def test_createorders(self):
        orders = Orders.objects.create(shop_id ="1",member_id ="2",user_id ="2",name ="Acyclovir",address ="rue de",phone_number="1234567890",money="2.2",status="1",payment_status="1",create_at = datetime.now(),update_at =datetime.now())
        orders.save()
        self.assertEqual(str(orders),"Acyclovir")

    def test_createorderdetail(self):
        orderdetail = OrderDetail.objects.create(order_id="1",product_id ="2",product_name ="Acyclovir",price="2.2",quantity="2",status="1")
        orderdetail.save()
        self.assertEqual(str(orderdetail),"Acyclovir")    
