from django.contrib import admin
from django.urls import path
from scramapp.views import home_view, deletePlan, publicScram, login_user, logout_user, register_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('delete_plan/<str:field_id>', deletePlan, name='delete_plan'),
    path('public/', publicScram, name = 'publicscram'),
    path('login_user/', login_user, name = 'login'),
    path('logout_user/', logout_user, name = 'logout'),
    path('register_user/', register_user, name='register_user'),
]
