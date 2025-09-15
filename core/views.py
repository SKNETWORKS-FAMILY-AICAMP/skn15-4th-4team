from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Conversation, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.http import require_http_methods
from django.db import connection


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()      # 비밀번호는 자동 해시 저장
            login(request, user)    # 가입 직후 자동 로그인 (원하면 제거)
            return redirect("chat:index")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

# --- (임시) OpenAI 호출 대체 함수 ---
def ai_reply(user_text: str, history: list[dict]) -> str:
    return f"Anki 카드 형식 초안:\n- Q: {user_text}\n- A: (여기에 답을 생성해서 채워주세요)"

@login_required
def chat_index(request):
    convs = Conversation.objects.filter(user=request.user)
    return render(request, "chat/index.html", {"conversations": convs})

@login_required
def new_conversation(request):
    conv = Conversation.objects.create(user=request.user, title="새 대화")
    return redirect("chat:room", pk=conv.pk)

@login_required
def chat_room(request, pk: int):
    conv = get_object_or_404(Conversation, pk=pk, user=request.user)
    return render(request, "chat/room.html", {"conv": conv, "messages": conv.messages.all()})

@login_required
@require_POST
def api_send_message(request):
    conv_id = request.POST.get("conversation_id")
    text = request.POST.get("text", "").strip()
    if not conv_id or not text:
        return JsonResponse({"ok": False, "error": "필수값 누락"}, status=400)

    conv = get_object_or_404(Conversation, pk=conv_id, user=request.user)

    # 1) 사용자 메시지 저장
    Message.objects.create(conversation=conv, role="user", content=text)

    # 2) 히스토리 구성
    history = [{"role": m.role, "content": m.content} for m in conv.messages.order_by("created_at")[:50]]

    # 3) AI 응답
    assistant_text = ai_reply(text, history)

    # 4) 어시스턴트 메시지 저장
    Message.objects.create(conversation=conv, role="assistant", content=assistant_text)

    # 5) 제목 자동 업데이트
    if not conv.title or conv.title == "새 대화":
        conv.title = text[:30]
        conv.save(update_fields=["title", "updated_at"])

    return JsonResponse({
        "ok": True,
        "assistant": assistant_text,
        # (선택) 이미지 검색 결과를 내려주고 싶으면 여기에 추가
        # "images": ["https://...", "https://...", "https://..."]
    })

# --- 로그아웃(POST 전용) ---
@require_POST
def force_logout(request):
    logout(request)
    return redirect("login")
