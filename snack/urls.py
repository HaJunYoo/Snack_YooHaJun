from django.urls import path
from snack import views


urlpatterns = [
    path('', views.list_members, name = 'list_snacks'),
    path('new/', views.create_member, name='add_snack'),
    path('update/<int:id>/', views.update_member, name='update_snack'),
    # update the id -> integer value
    path('delete/<int:id>/', views.delete_member, name='delete_snack'),

]
