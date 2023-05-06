from django.urls import path

from .views import TransferView, CreateUserView, APIRootView

urlpatterns = [
    path('', APIRootView.as_view(), name='roots'),
    path("transfer/", TransferView.as_view(), name='transfer'),
    path("create/", CreateUserView.as_view(), name='create'),
]

