"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

from Movie import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),

    url(r'^movielist/(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^movielist/$', views.list_all_movies, name='movielist'),
    url(r'^directors/(?P<director_id>[0-9]+)/$', views.director_detail, name='directordetail'),
    url(r'^directors/$', views.list_all_directors, name='directors'),
    url(r'^genres/(?P<genre_id>[0-9]+)/$', views.genre_detail, name='genredetail'),
    url(r'^genres/$', views.list_all_genres, name='genres'),
    url(r'^add_movie/$', views.add_movie, name='addmovie'),
    url(r'^add_director/$', views.add_director, name='adddirector'),
    url(r'^add_genre/$', views.add_genre, name='addgengre'),
]
