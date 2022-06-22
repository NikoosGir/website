from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from jdm.models import Post, Brand, Car, Body, Transmission, DriveType, Author, Comment



class RegistrationTest(TestCase):
    def setUp(self):
        self.register = reverse('registration')
        self.redirect = reverse('main')
        User.objects.all().delete()
        
    def test_reg_page(self):
        response = self.client.get(self.register)
        self.assertEqual(response.status_code, 200)
                                
    def test_reg(self):
        self.assertEqual(User.objects.count(), 0)
        response = self.client.post(self.register, {
            'username' :'test_user',
            'password1':'Qazw1234',
            'password2':'Qazw1234'}, follow=False)
        self.assertEqual(self.redirect, response.headers['Location'])
        self.assertEqual(response.status_code, 302)
        user = User.objects.first()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.username, 'test_user')



class LoginTest(TestCase):
    def setUp(self):
        self.login = reverse('login')
        self.data = {
            'username': 'test_user',
            'password': 'Qazw1234'}
        User.objects.create_user(**self.data) 
        
    def test_login(self):
        self.assertEqual(User.objects.count(), 1)
        response = self.client.post(self.login, self.data, follow=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context['user'].is_authenticated)



class LogoutTest(TestCase):
    def setUp(self):
        self.logout = reverse('logout')
        self.redirect = reverse('main') 
        
    def test_logout(self):
        response = self.client.post(self.logout, follow=False)
        self.assertEqual(302, response.status_code)
        self.assertEqual(self.redirect, response.headers['Location'])
  
  
        
class MainPageTest(TestCase):
    def setUp(self):
        import tempfile
        self.main = reverse('main')
        self.post = Post.objects.create(name = 'test_name',
                                        content = 'test_text',
                                        photo = tempfile.NamedTemporaryFile(suffix=".jpeg").name)
        
    def test_main_page(self):
        response = self.client.get(self.main)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, '<div class="base">', 1)
      
        

class BrandsPageTest(TestCase):
    def setUp(self):
        import tempfile
        self.brands = reverse('brands')
        self.brand = Brand.objects.create(name = 'test_name', photo = tempfile.NamedTemporaryFile(suffix=".jpeg").name)
        
    def test_brands_page(self):
        response = self.client.get(self.brands)
        self.assertEqual(Brand.objects.count(), 1)
        self.assertContains(response, '<div class="brand">', 1)
    
        

class CarsPageTest(TestCase):
    def setUp(self):
        import tempfile
        self.cars = reverse('cars')
        self.brand = Brand.objects.create(name = 'test_brand', photo = tempfile.NamedTemporaryFile(suffix=".jpeg").name,)
        self.body = Body.objects.create(name='test_body')
        self.tr = Transmission.objects.create(name='test_tr')
        self.dt = DriveType.objects.create(name='test_dt')
        self.car = Car.objects.create(brand = self.brand,
                                        model = 'test_model',
                                        photo1 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo2 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo3 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo4 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        body = self.body,
                                        sits = '1',
                                        created = '2000',
                                        transmission = self.tr,
                                        drive_type = self.dt,
                                        engine_name = 'test_en',
                                        engine_volume = '2.0',
                                        pover = '250 HP',
                                        moment = '300 NM',
                                        about = 'test_about',
                                        little_more_title = 'test_little_more_title',
                                        little_more = 'test_little_more')
        
    def test_cars_page(self):
        response = self.client.get(self.cars)
        self.assertEqual(Car.objects.count(), 1)
        self.assertContains(response, '<div class="car">', 1)
       


class CarsInBrandTest(TestCase):
    def setUp(self):
        import tempfile
        self.brand = Brand.objects.create(name = 'test_brand', photo = tempfile.NamedTemporaryFile(suffix=".jpeg").name,)
        self.body = Body.objects.create(name='test_body')
        self.tr = Transmission.objects.create(name='test_tr')
        self.dt = DriveType.objects.create(name='test_dt')
        self.car = Car.objects.create(brand = self.brand,
                                        model = 'test_model',
                                        photo1 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo2 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo3 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo4 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        body = self.body,
                                        sits = '1',
                                        created = '2000',
                                        transmission = self.tr,
                                        drive_type = self.dt,
                                        engine_name = 'test_en',
                                        engine_volume = '2.0',
                                        pover = '250 HP',
                                        moment = '300 NM',
                                        about = 'test_about',
                                        little_more_title = 'test_little_more_title',
                                        little_more = 'test_little_more')
        self.cars = reverse('brand_details', kwargs={'pk': self.brand.id})
        
    def test_cars_in_brand_page(self):
        response = self.client.get(self.cars)
        self.assertEqual(Car.objects.count(), 1)
        self.assertContains(response, '<div class="car">', 1)



class AuthorDetailsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='nik', password='Qazw1234')
        self.author = Author.objects.get(user=self.user)
        self.client.force_login(self.user)
        self.author = reverse('author_details', kwargs={'pk': self.author.id})
        
    def test_author_page(self):
        response = self.client.get(self.author)
        self.assertEqual(Author.objects.count(), 1)
        self.assertContains(response, '<div class="author">', 1)



class AuthorEditTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='nik', password='Qazw1234')
        self.redirect = '/cars/'
        self.author = Author.objects.get(user=self.user)
        self.client.force_login(self.user)
        self.auth = reverse('author_edit', kwargs={'pk': self.author.id})
        
    def test_author_edit_page(self):
        response = self.client.post(self.auth, {
            'name' : 'test_name',
            'last_name' : 'test_last_name',
            'email' : 'test_email',})
        self.assertEqual(self.redirect, response.headers['Location'])
        self.assertEqual(302, response.status_code)
        self.assertEqual(Author.objects.count(), 1)
        
        
        
class CarCreateTest(TestCase):
    def setUp(self):
        import tempfile
        Car.objects.all().delete()
        self.cars = reverse('create_car')
        self.redirect = '/cars/'
        self.user = User.objects.create(username='nik', password='Qazw1234', is_staff=True)
        self.brand = Brand.objects.create(name = 'test_brand', photo = tempfile.NamedTemporaryFile(suffix=".jpeg").name,)
        self.body = Body.objects.create(name='test_body')
        self.tr = Transmission.objects.create(name='test_tr')
        self.dt = DriveType.objects.create(name='test_dt')
        self.client.force_login(self.user)
    
    def test_create_car(self):
        import tempfile
        self.assertEqual(Car.objects.count(), 0)
        response = self.client.post(self.cars, {
            'brand' : str(self.brand.id),
            'model' : 'test_model',
            'photo1' : tempfile.NamedTemporaryFile(suffix=".jpeg").name,
            'photo2' : tempfile.NamedTemporaryFile(suffix=".jpeg").name,
            'photo3' : tempfile.NamedTemporaryFile(suffix=".jpeg").name,
            'photo4' : tempfile.NamedTemporaryFile(suffix=".jpeg").name,
            'body' : str(self.body.id),
            'sits' : '1',
            'created' :'2000',
            'transmission' : str(self.tr.id),
            'drive_type' : str(self.dt.id),
            'engine_name' : 'test_en',
            'engine_volume' : '2.0',
            'pover' : '250 HP',
            'moment' : '300 NM',
            'about' : 'test_about',
            'little_more_title' : 'test_little_more_title',
            'little_more' : 'test_little_more'})
        self.assertTrue(self.user.is_staff)
        self.assertEqual(self.redirect, response.headers['Location'])
        self.assertEqual(302, response.status_code)
        self.assertEqual(Car.objects.count(), 1)



class CarDetailsTest(TestCase):
    def setUp(self):
        import tempfile
        self.brand = Brand.objects.create(name = 'test_brand', photo = tempfile.NamedTemporaryFile(suffix=".jpeg").name,)
        self.body = Body.objects.create(name='test_body')
        self.tr = Transmission.objects.create(name='test_tr')
        self.dt = DriveType.objects.create(name='test_dt')
        self.car = Car.objects.create(brand = self.brand,
                                        model = 'test_model',
                                        photo1 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo2 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo3 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo4 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        body = self.body,
                                        sits = '1',
                                        created = '2000',
                                        transmission = self.tr,
                                        drive_type = self.dt,
                                        engine_name = 'test_en',
                                        engine_volume = '2.0',
                                        pover = '250 HP',
                                        moment = '300 NM',
                                        about = 'test_about',
                                        little_more_title = 'test_little_more_title',
                                        little_more = 'test_little_more')
        self.cars = reverse('car_details', kwargs={'pk': self.car.id})

    def test_car_details_page(self):
        response = self.client.get(self.cars)
        self.assertContains(response, '<div class="car">', 1)
        
        
        
class CarEditTest(TestCase):
    def setUp(self):
        import tempfile
        self.redirect = '/cars/'
        self.user = User.objects.create(username='nik', password='Qazw1234', is_staff=True)
        self.brand = Brand.objects.create(name = 'test_brand', photo = tempfile.NamedTemporaryFile(suffix=".jpeg").name,)
        self.body = Body.objects.create(name='test_body')
        self.tr = Transmission.objects.create(name='test_tr')
        self.dt = DriveType.objects.create(name='test_dt')
        self.car = Car.objects.create(brand = self.brand,
                                        model = 'test_model',
                                        photo1 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo2 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo3 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo4 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        body = self.body,
                                        sits = '1',
                                        created = '2000',
                                        transmission = self.tr,
                                        drive_type = self.dt,
                                        engine_name = 'test_en',
                                        engine_volume = '2.0',
                                        pover = '250 HP',
                                        moment = '300 NM',
                                        about = 'test_about',
                                        little_more_title = 'test_little_more_title',
                                        little_more = 'test_little_more')
        self.client.force_login(self.user)
        self.cars = reverse('edit_car', kwargs={'pk': self.car.id})
    
    def test_edit_car(self):
        import tempfile
        self.assertEqual(Car.objects.count(), 1)
        response = self.client.post(self.cars, {
            'brand' : str(self.brand.id),
            'model' : 'test_model',
            'photo1' : tempfile.NamedTemporaryFile(suffix=".jpeg").name,
            'photo2' : tempfile.NamedTemporaryFile(suffix=".jpeg").name,
            'photo3' : tempfile.NamedTemporaryFile(suffix=".jpeg").name,
            'photo4' : tempfile.NamedTemporaryFile(suffix=".jpeg").name,
            'body' : str(self.body.id),
            'sits' : '1',
            'created' :'2000',
            'transmission' : str(self.tr.id),
            'drive_type' : str(self.dt.id),
            'engine_name' : 'test_en',
            'engine_volume' : '2.0',
            'pover' : '200 HP',
            'moment' : '300 NM',
            'about' : 'test_about',
            'little_more_title' : 'test_little_more_title',
            'little_more' : 'test_little_more'})
        self.assertTrue(self.user.is_staff)
        self.assertEqual(self.redirect, response.headers['Location'])
        self.assertEqual(302, response.status_code)
        self.assertEqual(Car.objects.count(), 1)



class CarDeleteTest(TestCase):
    def setUp(self):
        import tempfile
        Car.objects.all().delete()
        self.redirect = '/cars/'
        self.user = User.objects.create(username='nik', password='Qazw1234', is_staff=True)
        self.brand = Brand.objects.create(name = 'test_brand', photo = tempfile.NamedTemporaryFile(suffix=".jpeg").name,)
        self.body = Body.objects.create(name='test_body')
        self.tr = Transmission.objects.create(name='test_tr')
        self.dt = DriveType.objects.create(name='test_dt')
        self.car = Car.objects.create(brand = self.brand,
                                        model = 'test_model',
                                        photo1 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo2 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo3 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo4 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        body = self.body,
                                        sits = '1',
                                        created = '2000',
                                        transmission = self.tr,
                                        drive_type = self.dt,
                                        engine_name = 'test_en',
                                        engine_volume = '2.0',
                                        pover = '250 HP',
                                        moment = '300 NM',
                                        about = 'test_about',
                                        little_more_title = 'test_little_more_title',
                                        little_more = 'test_little_more')
        self.client.force_login(self.user)
        self.cars = reverse('car_delete', kwargs={'pk': self.car.id})
    
    def test_delete_car(self):
        self.assertEqual(Car.objects.count(), 1)
        response = self.client.post(self.cars)
        self.assertTrue(self.user.is_staff)
        self.assertEqual(self.redirect, response.headers['Location'])
        self.assertEqual(302, response.status_code)
        self.assertEqual(Car.objects.count(), 0)



class CommentDeleteTest(TestCase):
    def setUp(self):
        import tempfile
        self.user = User.objects.create(username='nik', password='Qazw1234')
        self.author = Author.objects.get(user=self.user)
        self.brand = Brand.objects.create(name = 'test_brand', photo = tempfile.NamedTemporaryFile(suffix=".jpeg").name,)
        self.body = Body.objects.create(name='test_body')
        self.tr = Transmission.objects.create(name='test_tr')
        self.dt = DriveType.objects.create(name='test_dt')
        self.car = Car.objects.create(brand = self.brand,
                                        model = 'test_model',
                                        photo1 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo2 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo3 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        photo4 = tempfile.NamedTemporaryFile(suffix=".jpeg").name,
                                        body = self.body,
                                        sits = '1',
                                        created = '2000',
                                        transmission = self.tr,
                                        drive_type = self.dt,
                                        engine_name = 'test_en',
                                        engine_volume = '2.0',
                                        pover = '250 HP',
                                        moment = '300 NM',
                                        about = 'test_about',
                                        little_more_title = 'test_little_more_title',
                                        little_more = 'test_little_more')
        self.com = Comment.objects.create(title='test', text='test_text', author=self.author, car=self.car, created='2022-06-10')
        self.client.force_login(self.user)
        self.comment = reverse('comment_delete', kwargs={'pk': self.com.id})
        self.redirect = '/cars/'
    
    def test_delete_comment_page(self):
        self.assertEqual(Comment.objects.count(), 1)
        response = self.client.post(self.comment)
        self.assertEqual(self.redirect, response.headers['Location'])
        self.assertEqual(302, response.status_code)
        self.assertEqual(Comment.objects.count(), 0)