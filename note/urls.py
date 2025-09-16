from django.urls import path

# 절대 임포트 시도 → 실패 시 상대 임포트
try:
    from note import views  # type: ignore
except Exception:
    from . import views  # type: ignore

app_name = "note"

urlpatterns = [
    path("", views.QABoardView.as_view(), name="index"),          # 기존 전체/검색
    path("my/", views.MyQABoardView.as_view(), name="mine"),      # ✅ 내 Q&A 전용
    path("<int:conv_id>/", views.QABoardView.as_view(), name="by-conv"),  # 선택: /note/70/ 같은 형태
]