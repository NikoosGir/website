from django.shortcuts import render, redirect
from django.urls import reverse_lazy  
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from jdm.forms import UserRegistrationForm
from jdm.models import Brand, Car, Post, Comment, Author
from jdm.forms import CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render


def error_404(request, exception): # Ошибка
    return render(request, '404.html')


def register_view(request): # Регистрация
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('main')
	form = UserRegistrationForm()
	return render (request = request, template_name='user_form.html', context={'register_form':form})


class JdmLoginView(LoginView): # Логин
    template_name = 'login.html'
    extra_context = {'title': 'JDM - Login'} 


class JdmLogoutView(LogoutView): # Выход
    template_name = 'logout.html'
    extra_context = {'title': 'JDM - Logout'} 


def filters(request): # Фильтрация
    if request.method == 'GET':
        brand_id = request.GET.get('brand_id')
        body_id = request.GET.get('body_id')
        drive_type_id = request.GET.get('drive_type_id')
        transmission_id = request.GET.get('transmission_id')
        created_from = request.GET.get('created_from')
        created_to = request.GET.get('created_to')
        if brand_id is not None: # bt dt tr cf ct
            cars = Car.objects.filter(brand_id=brand_id)
            if body_id is not None: # dt tr cf ct
                cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id))
                if drive_type_id is not None: # tr cf ct
                    cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(drive_type_id=drive_type_id))
                    if transmission_id is not None: # cf ct 
                        cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id))
                        if created_from is not None: # ct
                            cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id)& Q(created__range=(created_from, 2015)))
                            if created_to is not None:
                                cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id) & Q(created__range=(created_from, created_to)))                       
                        elif created_to is not None: # cf
                            cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id)& Q(created__range=(1980, created_to)))                    
                    elif created_from is not None: # tr ct
                        cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(created__range=(created_from, 2015)))
                        if created_to is not None: # tr
                            cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(created__range=(created_from, created_to)))
                    elif created_to is not None: # tr cf
                        cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(created__range=(1980, created_to)))   
                elif transmission_id is not None: # dt cf ct
                    cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(transmission_id=transmission_id))
                    if created_from is not None: # dt ct
                        cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(transmission_id=transmission_id)& Q(created__range=(created_from, 2015)))
                        if created_to is not None: # dt
                            cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(transmission_id=transmission_id) & Q(created__range=(created_from, created_to)))
                    elif created_to is not None: # dt cf
                        cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id)& Q(created__range=(1980, created_to)))
                elif created_from is not None: # dt tr ct
                    cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(created__range=(created_from, 2015))) 
                    if created_to is not None: # dt tr
                        cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(created__range=(created_from, created_to))) 
                elif created_to is not None: # dt tr cf
                    cars = Car.objects.filter(Q(brand_id=brand_id) & Q(body_id=body_id) & Q(created__range=(1980, created_to)))  
            elif drive_type_id is not None: # bt tr cf ct       
                cars = Car.objects.filter(Q(brand_id=brand_id) & Q(drive_type_id=drive_type_id))
                if transmission_id is not None: # bt cf ct
                    cars = Car.objects.filter(Q(brand_id=brand_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id))
                    if created_from is not None: # bt ct
                        cars = Car.objects.filter(Q(brand_id=brand_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id)& Q(created__range=(created_from, 2015)))
                        if created_to is not None: #bt
                            cars = Car.objects.filter(Q(brand_id=brand_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id) & Q(created__range=(created_from, created_to)))                       
                    elif created_to is not None: # bt cf
                        cars = Car.objects.filter(Q(brand_id=brand_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id) & Q(created__range=(1980, created_to)))                       
                elif created_from is not None: # bt tr ct
                    cars = Car.objects.filter(Q(brand_id=brand_id) & Q(drive_type_id=drive_type_id) & Q(created__range=(created_from, 2015)))
                    if created_to is not None: #bt tr
                        cars = Car.objects.filter(Q(brand_id=brand_id) & Q(drive_type_id=drive_type_id) & Q(created__range=(created_from, created_to)))                       
                elif created_to is not None: # bt tr cf
                    cars = Car.objects.filter(Q(brand_id=brand_id) & Q(drive_type_id=drive_type_id) & Q(created__range=(1980, created_to)))                       
            elif transmission_id is not None: # bt dt cf ct
                cars = Car.objects.filter(Q(brand_id=brand_id) & Q(transmission_id=transmission_id))
                if created_from is not None: # bt dt ct
                    cars = Car.objects.filter(Q(brand_id=brand_id) & Q(transmission_id=transmission_id)& Q(created__range=(created_from, 2015)))
                    if created_to is not None: #bt dt
                        cars = Car.objects.filter(Q(brand_id=brand_id) & Q(transmission_id=transmission_id) & Q(created__range=(created_from, created_to)))                       
                elif created_to is not None: # bt dt cf
                    cars = Car.objects.filter(Q(brand_id=brand_id) & Q(transmission_id=transmission_id) & Q(created__range=(1980, created_to)))                       
            elif created_from is not None: # bt dt tr ct
                cars = Car.objects.filter(Q(brand_id=brand_id) & Q(created__range=(created_from, 2015)))
                if created_to is not None: #bt dt tr
                    cars = Car.objects.filter(Q(brand_id=brand_id) & Q(created__range=(created_from, created_to)))  
            elif created_to is not None: #bt dt tr cf
                cars = Car.objects.filter(Q(brand_id=brand_id) & Q(created__range=(1980, created_to)))  
        elif body_id is not None: # br dt tr cf ct 
            cars = Car.objects.filter(body_id=body_id)
            if drive_type_id is not None: #br tr cf ct
                cars = Car.objects.filter(Q(body_id=body_id) & Q(drive_type_id=drive_type_id))
                if transmission_id is not None: #br cf ct 
                    cars = Car.objects.filter(Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id))
                    if created_from is not None: #br ct
                        cars = Car.objects.filter(Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id)& Q(created__range=(created_from, 2015)))
                        if created_to is not None: # br
                            cars = Car.objects.filter(Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id) & Q(created__range=(created_from, created_to)))                       
                    elif created_to is not None: # br cf
                            cars = Car.objects.filter(Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id) & Q(created__range=(1980, created_to)))                       
                elif created_from is not None: #br tr ct
                    cars = Car.objects.filter(Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(created__range=(created_from, 2015)))
                    if created_to is not None: # br tr
                        cars = Car.objects.filter(Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(created__range=(created_from, created_to)))                       
                elif created_to is not None: # br tr cf
                    cars = Car.objects.filter(Q(body_id=body_id) & Q(drive_type_id=drive_type_id) & Q(created__range=(1980, created_to)))                       
            elif transmission_id is not None: #br dr cf ct 
                cars = Car.objects.filter(Q(body_id=body_id) & Q(transmission_id=transmission_id))
                if created_from is not None: #br dr ct
                    cars = Car.objects.filter(Q(body_id=body_id) & Q(transmission_id=transmission_id)& Q(created__range=(created_from, 2015)))
                    if created_to is not None: # br dr 
                        cars = Car.objects.filter(Q(body_id=body_id) & Q(transmission_id=transmission_id) & Q(created__range=(created_from, created_to)))                       
                elif created_to is not None: # br dr cf
                        cars = Car.objects.filter(Q(body_id=body_id) & Q(transmission_id=transmission_id) & Q(created__range=(1980, created_to)))                       
            elif created_from is not None: #br dr tr ct
                cars = Car.objects.filter(Q(body_id=body_id) & Q(created__range=(created_from, 2015)))
                if created_to is not None: # br dr tr
                    cars = Car.objects.filter(Q(body_id=body_id) & Q(created__range=(created_from, created_to)))                       
            elif created_to is not None: # br dr tr cf
                cars = Car.objects.filter(Q(body_id=body_id) & Q(created__range=(1980, created_to)))         
        elif drive_type_id is not None: #br bt tr cf ct
            cars = Car.objects.filter(drive_type_id=drive_type_id)
            if transmission_id is not None: #br bt cf ct 
                cars = Car.objects.filter(Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id))
                if created_from is not None: #br bt ct
                    cars = Car.objects.filter(Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id)& Q(created__range=(created_from, 2015)))
                    if created_to is not None: # br bt
                        cars = Car.objects.filter(Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id) & Q(created__range=(created_from, created_to)))                       
                elif created_to is not None: # br bt cf
                    cars = Car.objects.filter(Q(drive_type_id=drive_type_id) & Q(transmission_id=transmission_id) & Q(created__range=(1980, created_to)))                       
            elif created_from is not None: #br bt tr ct
                cars = Car.objects.filter(Q(drive_type_id=drive_type_id) & Q(created__range=(created_from, 2015)))
                if created_to is not None: # br bt tr
                    cars = Car.objects.filter(Q(drive_type_id=drive_type_id) & Q(created__range=(created_from, created_to)))                       
            elif created_to is not None: #br bt tr cf
                cars = Car.objects.filter(Q(drive_type_id=drive_type_id) & Q(created__range=(1980, created_to)))  
        elif transmission_id is not None: #br bt dr cf ct 
            cars = Car.objects.filter(transmission_id=transmission_id)
            if created_from is not None: #br bt dr ct
                cars = Car.objects.filter(Q(transmission_id=transmission_id)& Q(created__range=(created_from, 2015)))
                if created_to is not None: # br bt dr
                    cars = Car.objects.filter(Q(transmission_id=transmission_id) & Q(created__range=(created_from, created_to)))                       
            elif created_to is not None: # br bt dr cf
                cars = Car.objects.filter(Q(transmission_id=transmission_id) & Q(created__range=(1980, created_to)))    
        elif created_from is not None: #br bt dr tr ct
            cars = Car.objects.filter(created__range=(created_from, 2015))
            if created_to is not None: # br bt dr tr
                cars = Car.objects.filter(created__range=(created_from, created_to))
        elif created_to is not None: # br bt dr tr cf
                cars = Car.objects.filter(created__range=(1980, created_to))     
        else:
            cars = Car.objects.all()          
        count = cars.count()
        print(count)
        return render(request, 'filter.html', context = {'cars' : cars, 'count' : count, 'title' : 'JDM - Filter '})
    
    
def search(request): # Поиск
    if request.method == 'GET':
        model = request.GET.get('q')
        brand_id = request.GET.get('brand_id')
        if model is not None:
            cars = Car.objects.filter(model__icontains=model)
            if brand_id is not None:
                cars = Car.objects.filter(Q(model__icontains=model) & Q(brand_id=brand_id))
        elif brand_id is not None:
            cars = Car.objects.filter(brand_id=brand_id)
        count = cars.count()
        print(count)
        return render(request, 'search.html', context = {'cars' : cars, 'count' : count, 'title' : 'JDM - Search '})

        
class MainView(ListView): # Главная 
    model = Post
    context_object_name = 'posts'
    template_name = 'main.html'
    extra_context = {'title': 'JDM - Main'} 
    

class BrandsView(ListView): # Марки авто
    model = Brand
    context_object_name = 'brands'
    template_name = 'brands.html'
    extra_context = {'title': 'JDM - Brands'} 
   
       
class CarsView(ListView): # Модели авто
    model = Car
    context_object_name = 'cars'
    paginate_by = 6
    template_name = 'cars.html'
    extra_context = {'title': 'JDM - Cars'} 
        
    
class BrandCarView(ListView): # Модели авто в марке
    model = Car
    context_object_name = 'cars'
    template_name = 'brand_details.html'
    paginate_by = 3
    extra_context = {'title': 'JDM - Cars in brand'}

    def get_queryset(self):
        print('kwargs', self.kwargs)
        return Car.objects.filter(brand__id=self.kwargs['pk'])
    

class DetailAuthorView(DetailView, UserPassesTestMixin): # Подробности автора
    model = Author
    template_name = 'author_details.html'
    extra_context = {'title': 'JDM - Author'} 

    def test_func(self):
        author_id = self.kwargs['pk']
        user = self.request.user
        author = Author.objects.get(id=author_id)
        if author.user == user:
            return True
        return False      
    
class AuthorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # Редактирование автора
    model = Author
    fields = ('name', 'last_name', 'email', 'avatar', 'date_of_birthday')
    template_name = 'author_form.html'
    success_url = reverse_lazy('cars')
    extra_context = {'title': 'JDM - Author edit'}
    login_url = reverse_lazy('login')

    def test_func(self):
        author_id = self.kwargs['pk']
        user = self.request.user
        author = Author.objects.get(id=author_id)
        if author.user == user:
            return True
        return False    
    
    
class CarCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView): # Создание модели авто
    model = Car
    fields = ('brand', 'model', 'photo1', 'photo2', 'photo3', 'photo4', 'body', 'sits', 'created', 'transmission', 'drive_type', 'engine_name', 'engine_volume', 'pover', 'moment', 'about', 'little_more_title', 'little_more',)
    template_name = 'car_form.html'
    success_url = reverse_lazy('cars')
    extra_context = {'title': 'JDM - Car create'}
    login_url = reverse_lazy('login')

    def test_func(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return True
        return False


class DetailCarView(DetailView): # Подробности модели авто
    model = Car
    form = CommentForm
    template_name = 'car_details.html'
    extra_context = {'title': 'JDM - Car info', 'form':form} 
    
    def post(self, request, *args, **kwargs): # Создание комментария
        post_id = kwargs['pk']
        form = CommentForm(data=request.POST, files=request.FILES)
        form.instance.car = Car.objects.get(id=post_id)
        form.instance.author_id  = request.user.id
        try:
            form.save()
        except Exception as e:
            print(e)
        return redirect('car_details', post_id)


class UpdateCarView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # Редактирование модели авто
    model = Car
    fields = ('brand', 'model', 'photo1', 'photo2', 'photo3', 'photo4', 'body', 'sits', 'created', 'transmission', 'drive_type', 'engine_name', 'engine_volume', 'pover', 'moment', 'about', 'little_more_title', 'little_more',)
    template_name = 'car_form.html'
    success_url = reverse_lazy('cars')
    extra_context = {'title': 'JDM - Car edit'}
    login_url = reverse_lazy('login')

    def test_func(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return True
        return False
    

class DeleteCarView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # Удаление модели авто
    model = Car
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('cars')
    extra_context = {'title': 'JDM - Car delete'}
    login_url = reverse_lazy('login')

    def test_func(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return True
        return False


class UpdateCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # Редактирование комментария
    model = Comment
    fields = ('title', 'text')
    template_name = 'comment_form.html'
    success_url = reverse_lazy('cars')
    extra_context = {'title': 'JDM - Comment edit'}
    login_url = reverse_lazy('login')

    def test_func(self):
        comment_id = self.kwargs['pk']
        user = self.request.user
        comment = Comment.objects.get(id=comment_id)
        if comment.author.user == user:
            return True
        elif self.request.user.is_staff or self.request.user.is_superuser:
            return True
        return False
    
    
class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # Удаление комментария
    model = Comment
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('cars')
    extra_context = {'title': 'JDM - Comment delete'}
    login_url = reverse_lazy('login')

    def test_func(self):
        comment_id = self.kwargs['pk']
        user = self.request.user
        comment = Comment.objects.get(id=comment_id)
        if comment.author.user == user:
            return True
        elif self.request.user.is_staff or self.request.user.is_superuser:
            return True
        return False