"""katysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from katysite import views as mainview
from coaching import views as coach
from numero import views as num


coaching_urlpatterns = [
    path('', coach.index, name='coaching_index'),
    re_path(r"^post/(?P<post_id>\d+)", coach.post, name='coaching_post'),
    path('posts/', coach.posts, name='coaching_all_posts'),
    re_path(r"^post", coach.post, name='coaching_post'),
]

numero_urlpatterns = [
    path('', num.index, name='numero_index'),
    re_path(r"^calc", num.calc, name='calc_matrix')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainview.index, name='main_index'),
    # path('<slug:menu_slug>', mainview.index, name='main_index'),
    path('coach/', include(coaching_urlpatterns)),
    path('numero/', include(numero_urlpatterns)),
]
