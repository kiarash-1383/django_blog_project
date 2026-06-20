from django.urls import  path
from project1 import views

app_name = 'project1'
# پیشنهاد برای یکدست شدن
urlpatterns = [
    path('index/', views.index, name='index'),
    path('post/', views.PostListView.as_view(), name='post'),
    path('inner_post/<int:id>/', views.inner_post, name='inner_post'), # اضافه کردن اسلش
    path('ticket/', views.ticket, name='ticket'),                     # اضافه کردن اسلش
    path('post/<int:post_id>/comment/', views.comment_view, name='comment_view'), # اضافه کردن اسلش
]
