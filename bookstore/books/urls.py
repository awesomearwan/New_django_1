from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'books'

# DRF router for API endpoints
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='books')

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),  # Updated name
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('profile/', views.MyProfileView.as_view(), name='my_profile'),
    path('addprofile/', views.profileView.as_view(), name='addprofile'),
    path('api/', include(router.urls)),
]
