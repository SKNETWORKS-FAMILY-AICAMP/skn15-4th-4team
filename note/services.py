from dataclasses import dataclass
from typing import Iterable, List, Optional, Any
from django.conf import settings
from django.apps import apps

def get_message_model():
    """
    settings.NOTE_MESSAGE_MODEL (예: "chat.Message")에서 모델을 지연 로드.
    없거나 로드 실패 시 None 반환.
    """
    model_label = getattr(settings, "NOTE_MESSAGE_MODEL", "chat.Message")
    try:
        app_label, model_name = model_label.split(".")
        return apps.get_model(app_label, model_name)
    except Exception:
        return None

@dataclass
class QAItem:
    conversation_id: int
    conversation_title: str
    user_msg_id: int
    user_text: str
    assistant_msg_id: Optional[int]
    assistant_text: Optional[str]
    created_at: "datetime"

def pair_user_assistant(messages: Iterable[Any]) -> List[QAItem]:
    """
    같은 대화(conversation) 내에서
    1) user 메시지 바로 다음 assistant 메시지를 Q&A로 페어링.
    2) assistant가 없으면 A=None 처리.
    """
    items: List[QAItem] = []
    prev_user = None
    for msg in messages:
        if getattr(msg, "role", None) == "user":
            prev_user = msg
        elif (
            getattr(msg, "role", None) == "assistant"
            and prev_user
            and getattr(prev_user, "conversation_id", None) == getattr(msg, "conversation_id", None)
        ):
            items.append(
                QAItem(
                    conversation_id=prev_user.conversation_id,
                    conversation_title=str(getattr(prev_user.conversation, "title", "")) or f"대화 #{prev_user.conversation_id}",
                    user_msg_id=prev_user.id,
                    user_text=getattr(prev_user, "content", ""),
                    assistant_msg_id=msg.id,
                    assistant_text=getattr(msg, "content", ""),
                    created_at=prev_user.created_at,
                )
            )
            prev_user = None
    if prev_user:
        items.append(
            QAItem(
                conversation_id=prev_user.conversation_id,
                conversation_title=str(getattr(prev_user.conversation, "title", "")) or f"대화 #{prev_user.conversation_id}",
                user_msg_id=prev_user.id,
                user_text=getattr(prev_user, "content", ""),
                assistant_msg_id=None,
                assistant_text=None,
                created_at=prev_user.created_at,
            )
        )
    return items
