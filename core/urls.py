from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.chat_index, name="index"),
    path("new/", views.new_conversation, name="new"),
    path("c/<int:pk>/", views.chat_room, name="room"),
    path("api/send/", views.api_send_message, name="api_send"),
    path("logout/", views.force_logout, name="logout"),
    path("accounts/signup/", views.signup, name="signup"),  # ← 추가
    path("upload-file/", views.api_upload_file, name="upload_file"),

]

