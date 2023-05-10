from django.urls import path
from .views import api_home_page, api_detail_page, api_update_page, api_delete_page, api_create_page


urlpatterns = [
    path("", api_home_page, name= "api_home_page"),
    path("create/", api_create_page, name="page"),
    path("<int:id>/detail/", api_detail_page, name="detail-page"),
    path("<int:id>/update/", api_update_page, name="update-page"),
    path("<int:id>/delete/", api_delete_page, name="delete-page")
]