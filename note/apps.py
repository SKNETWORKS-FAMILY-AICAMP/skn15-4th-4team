from django.apps import AppConfig

class NoteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "note"
    verbose_name = "Q&A 노트"
