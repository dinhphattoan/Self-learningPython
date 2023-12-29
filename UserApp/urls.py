from django.urls import path

from UserApp import auth_views

from . import views
urlpatterns = [
     # Authentication views
    path('',views.index,name="default_view"),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('signup/', auth_views.signup_view, name='signup'),
    path('password_reset/', auth_views.password_reset_view, name='password_reset'),
    path('upload_document/',views.upload_document,  name='upload_document')
]
