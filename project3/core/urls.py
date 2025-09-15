from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.chat_index, name="index"),                 # 대화 목록 + 새 대화 버튼
    path("new/", views.new_conversation, name="new"),         # 새 대화 만들고 방으로 이동
    path("c/<int:pk>/", views.chat_room, name="room"),        # 특정 대화방
    path("api/send/", views.api_send_message, name="api_send")# 메시지 전송 API (AJAX)
]
