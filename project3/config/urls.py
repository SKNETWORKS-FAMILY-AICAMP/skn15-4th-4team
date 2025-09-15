from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),  # ← core 앱 라우트
    path("accounts/", include("django.contrib.auth.urls")),  # 로그인/로그아웃/비번재설정
    path("", RedirectView.as_view(pattern_name="chat:index", permanent=False)),
]
