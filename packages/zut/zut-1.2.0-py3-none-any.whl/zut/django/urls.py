from django.urls import path

try:
    import channels
except ImportError:
    channels = False
    
from zut.django import views

app_name = 'zut'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('lang/', views.LangView.as_view(), name='lang'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

if channels:
    from zut.django import consumers

    websocket_urlpatterns = [
        path('ping/', consumers.PingConsumer.as_asgi()),
    ]
