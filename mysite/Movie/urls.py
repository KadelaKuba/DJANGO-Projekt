from django.conf.urls import url
from django.contrib import admin

from . import views

# urlpatterns = [
#     url(r'^$', views.index, name="index"),
#     # /Movie/1
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
#
# ]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', views.index, name='index'),
#
#
#     url(r'^booklist/(?P<book_id>[0-9]+)/$', views.detail, name = 'detail'),
#     url(r'^authors/(?P<author_id>[0-9]+)/$', views.author_detail, name = 'authordetail'),
#     url(r'^booklist/$', views.list_all_books, name = 'booklist'),
#     url(r'^authors/$', views.list_all_authors, name = 'authors'),
#     url(r'^add_book/$', views.add_book, name = 'addbook'),
#     url(r'^add_author/$', views.add_author, name = 'addauthor'),
#     url(r'^add_genre/$', views.add_genre, name = 'addgengre'),
#
#     url(r'^search/$', views.search, name = 'search'),
#     url(r'^search/([a-zA-Z])/$', views.search, name = 'search_value'),
#
#
#     #url(r'^add_book$', 'add_book'),
# ]
