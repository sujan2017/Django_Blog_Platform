from django.urls import path
from . api_views import(
    post_list_api,
    post_detail_api,
    category_list_api,
    post_by_category_api,
    post_create_api,
    post_update_api,
    post_delete_api,
    comment_list_api,
    comment_create_api,
    comment_update_api,
    comment_delete_api,
    register_api,
    login_api,
    logout_api

)

urlpatterns = [
    path('posts/', post_list_api, name='api-post-list'),
    path('posts/create/', post_create_api, name='api-post-create'),
    path('posts/<slug:slug>/', post_detail_api, name='api-post-detail'),
    path('posts/<slug:slug>/update/', post_update_api, name='api-post-update'),
    path('posts/<slug:slug>/delete/', post_delete_api, name='api-post-delete'),
    path('categories/', category_list_api, name='api-category-list'),
    path('categories/<slug:slug>/posts/', post_by_category_api, name='api-posts-by-category'),
    path('posts/<slug:post_slug>/comments/', comment_list_api, name='api-comment-list'),
    path('posts/<slug:post_slug>/comments/create/', comment_create_api, name='api-comment-create'),
    path('comments/<int:comment_id>/update/', comment_update_api, name='api-comment-update'),
    path('comments/<int:comment_id>/delete/', comment_delete_api, name='api-comment-delete'),

    path('auth/register/', register_api, name='api-register'),
    path('auth/login/', login_api, name='api-login'),
    path('auth/logout/', logout_api, name='api-logout'),


]
