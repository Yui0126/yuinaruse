from django.urls import path


from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.detail, name="detail"),
    path("<int:post_id>/comment/", views.comment, name="comment"),
    path("about/", views.about, name="about"),
]