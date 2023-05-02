from django.urls import path

from .views import CustomUserCreateView, CustomUserUpdateView, CustomUserDetailView, CustomLogoutView, CustomLoginView


app_name = 'users'


urlpatterns = [
    path('user_info/<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
    path('register/', CustomUserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', CustomUserUpdateView.as_view(), name='user_update'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]