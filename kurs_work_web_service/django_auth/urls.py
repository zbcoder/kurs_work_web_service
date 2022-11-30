from django.urls import path


urlpatterns = [
    path(r'login/', login, name='login'),
    path(r'registry/', registry, name='registry'),
    path(r'logout/', logout, name='logout')
]