

from django.urls import path
from .views import(CreateRecords, ViewRecords, DeleteRecords)


urlpatterns = [
    path("createRecords/", CreateRecords.as_view(), name='create_records'),
    path("viewRecords/", ViewRecords.as_view(), name='view_records'),
    path("deleteRecords/<int:pk>/", DeleteRecords.as_view(), name='delete_records')


]
