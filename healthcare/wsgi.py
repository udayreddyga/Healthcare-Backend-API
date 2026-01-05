import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "healthcare.settings")

application = get_wsgi_application()

try:
    from .auto_superuser import create_superuser
    create_superuser()
except Exception:
    pass