from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('register/',views.register,name="register"),
    path('profile/(?P<username>[a-zA-Z0-9]+)$',views.profile, name="profile"),
    path('profile/edit_profile/', views.edit_profile, name="edit_profile"),
    path('profile/bookmarks/', views.index_bookmarks, name="index_bookmarks"),
    path('new_bookmark/', views.create_bookmark, name='new_bookmark'),
    path('logout/',views.logout_view, name="logout"),
    url('^', include('django.contrib.auth.urls')),
    path('login_twitter', views.login_twitter, name='login_twitter'),
    path('callback_url/', views.callback_url, name='callback'),
    path('post_tweet/', views.post_tweet, name='post_tweet'),
]

