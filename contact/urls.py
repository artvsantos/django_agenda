from contact import views
from django.urls import path

app_name = 'contact'

urlpatterns = [
    # contact (CRUD)
    path('contact/create/', views.contact, name='contact'),
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.contact, name='contact'),
    path('contact/<int:contact_id>/delete/', views.contact, name='contact'),


    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
