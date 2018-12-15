from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("uploadFile/", views.upload, name='upload'),
    path("select_dir/", views.select_dir, name="selectdir"),

    path("downloadFile/", views.download, name='download'),

    # path("static_for_test_html_js/", views.front_test, name="front_test"),
]
