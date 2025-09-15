from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),                     # ← 우리 앱
    path("accounts/", include("django.contrib.auth.urls")),  # 로그인/비번 재설정 등
    path("", RedirectView.as_view(pattern_name="chat:index", permanent=False)),
]
