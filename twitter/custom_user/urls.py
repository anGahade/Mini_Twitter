from django.urls import path
from .views import (RegisterView, login_view, logout_view,
                    CustomSettingsView, CustomUserProfileView, subscribe, unsubscribe)

app_name = "custom_user"
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit-profile/', CustomSettingsView.as_view(), name='account_settings'),
    path('user/<str:username>/', CustomUserProfileView.as_view(), name='user_profile'),
    path('edit-profile/', CustomSettingsView.as_view(), name='edit_profile'),
    path('user/<str:username>/subscribe/', subscribe, name='subscribe'),
    path('user/<str:username>/unsubscribe/', unsubscribe, name='unsubscribe'),

]