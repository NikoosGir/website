from re import S
from django.urls import path
from jdm.views import register_view, JdmLoginView, JdmLogoutView, filters, search, MainView, BrandsView, CarsView, BrandCarView, DetailAuthorView, AuthorUpdateView, CarCreateView, UpdateCarView, DeleteCarView, DetailCarView, UpdateCommentView, DeleteCommentView


urlpatterns = [
    path("reg/", register_view, name='registration'),
    path("login/", JdmLoginView.as_view(), name='login'),
    path('logout/', JdmLogoutView.as_view(), name='logout'),
    path('filter/', filters, name='filter'),
    path('search/', search, name='search'),
    path('', MainView.as_view(), name='main'),
    path("author/<int:pk>/", DetailAuthorView.as_view(), name='author_details'),
    path("author/edit/<int:pk>/", AuthorUpdateView.as_view(), name='author_edit'),
    path('brands/', BrandsView.as_view(), name='brands'),
    path('brand/<int:pk>/', BrandCarView.as_view(), name='brand_details'),
    path('cars/', CarsView.as_view(), name='cars'),
    path("car/create/", CarCreateView.as_view(), name='create_car'),
    path('car/<int:pk>/', DetailCarView.as_view(), name='car_details'),
    path("car/edit/<int:pk>/", UpdateCarView.as_view(), name='edit_car'),
    path("car/delete/<int:pk>/", DeleteCarView.as_view(), name='car_delete'),
    path("comment/edit/<int:pk>/", UpdateCommentView.as_view(), name='comment_edit'),
    path("comment/delete/<int:pk>/", DeleteCommentView.as_view(), name='comment_delete'),
]