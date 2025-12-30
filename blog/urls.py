from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comment/<int:pk>/edit/',views.edit_comment, name='edit_comment'),

    #api
    path('api/posts/', api_views.post_list_api, name='api_post_list'),
    path('api/posts/<slug:slug>/', api_views.post_detail_api, name='api_post_detail'),
    path('api/categories/', api_views.category_list_api, name='api_category_list'),
    path('api/category/<slug:slug>/posts/', api_views.post_by_category_api, name='api_post_by_category'),

    
    
    
]