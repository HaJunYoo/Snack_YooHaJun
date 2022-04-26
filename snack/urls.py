from django.urls import path
from snack import views
#snack

urlpatterns = [
    path('', views.list_snacks, name = 'list_snacks'),
    path('new/', views.create_snack, name='add_snack'),
    path('update/<int:id>/', views.update_snack, name='update_snack'),
    # # update the id -> integer value
    path('delete/<int:id>/', views.delete_snack, name='delete_snack'),

]
