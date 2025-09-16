from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from note.views import QABoardView  # ← 추가


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),                     # ← 우리 앱
    path("accounts/", include("django.contrib.auth.urls")),  # 로그인/비번 재설정 등
    path("", RedirectView.as_view(pattern_name="chat:index", permanent=False)),
    path("note/", include("note.urls")),            # 전체 목록/검색
    path("c/<int:conv_id>/note/", QABoardView.as_view(), name="note-by-conv"),  # 대화별
]
