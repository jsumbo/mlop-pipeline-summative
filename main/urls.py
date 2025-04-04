from django.urls import path
from .views import index, predict, process_upload, prediction_result, logout_view

urlpatterns = [
    path("", index, name="index"),
    path("predict/", predict, name="predict"),
    path("upload/", process_upload, name="upload"),
    path("prediction-result/", prediction_result, name="prediction_result"),
    path("logout/", logout_view, name="logout"),
]