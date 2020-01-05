from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('detail/<int:id>', views.detail_page, name='detail_page'),
	path('edit-page/', views.edit_page, name="edit_page"),
	path('update-page/<int:id>', views.update_page, name="update_page"),
	path('delete-page/<int:id>', views.delete_page, name="delete_page"),
]