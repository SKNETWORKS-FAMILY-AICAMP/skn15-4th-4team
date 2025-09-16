from typing import Any, Dict, List
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .services import pair_user_assistant, QAItem, get_message_model


class QABoardView(ListView):
    template_name = "note/index.html"
    context_object_name = "qa_list"
    paginate_by = 20
    scope = "all"  # 기본: 전체 (필터는 쿼리스트링/URL로)

    def get_queryset(self) -> List[QAItem]:
        Message = get_message_model()
        if Message is None:
            return []

        # URL param 우선 → 쿼리스트링 보조
        conv_id_kw = self.kwargs.get("conv_id")
        conv_qs = self.request.GET.get("conv", "").strip()
        conv_id = str(conv_id_kw) if conv_id_kw is not None else conv_qs

        q = self.request.GET.get("q", "").strip()
        date_from = self.request.GET.get("from", "").strip()
        date_to = self.request.GET.get("to", "").strip()

        qs = (
            Message.objects.select_related("conversation")
            .filter(role__in=["user", "assistant"])
            .order_by("conversation_id", "created_at", "id")
        )

        # 전체/대화별 필터
        if conv_id and str(conv_id).isdigit():
            qs = qs.filter(conversation_id=int(conv_id))

        # 키워드
        if q:
            qs = qs.filter(Q(content__icontains=q))

        # 날짜
        if date_from:
            qs = qs.filter(created_at__date__gte=date_from)
        if date_to:
            qs = qs.filter(created_at__date__lte=date_to)

        items = pair_user_assistant(qs)
        items.sort(key=lambda x: (x.created_at, x.user_msg_id), reverse=True)
        return items

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        conv_id_kw = self.kwargs.get("conv_id")
        ctx["conv"] = str(conv_id_kw) if conv_id_kw is not None else self.request.GET.get("conv", "")
        ctx["q"] = self.request.GET.get("q", "")
        ctx["date_from"] = self.request.GET.get("from", "")
        ctx["date_to"] = self.request.GET.get("to", "")
        ctx["scope"] = self.scope
        return ctx


class MyQABoardView(LoginRequiredMixin, QABoardView):
    """
    로그인 사용자의 모든 대화(Conversation.user == request.user)를 대상으로
    user→assistant 페어를 생성해 보여줍니다.
    """
    scope = "mine"
    login_url = "login"  # settings.LOGIN_URL 과 일치해야 함

    def get_queryset(self) -> List[QAItem]:
        Message = get_message_model()
        if Message is None:
            return []

        q = self.request.GET.get("q", "").strip()
        date_from = self.request.GET.get("from", "").strip()
        date_to = self.request.GET.get("to", "").strip()

        # 🔒 내 대화만 스코프 (Conversation에 user FK가 있다고 가정)
        qs = (
            Message.objects.select_related("conversation")
            .filter(conversation__user=self.request.user, role__in=["user", "assistant"])
            .order_by("conversation_id", "created_at", "id")
        )

        # 키워드/날짜 필터 동일 적용
        if q:
            qs = qs.filter(Q(content__icontains=q))
        if date_from:
            qs = qs.filter(created_at__date__gte=date_from)
        if date_to:
            qs = qs.filter(created_at__date__lte=date_to)

        items = pair_user_assistant(qs)
        items.sort(key=lambda x: (x.created_at, x.user_msg_id), reverse=True)
        return items
