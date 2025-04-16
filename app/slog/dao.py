from app.dao.base import BaseDAO
from app.slog.models import Slog


class SlogDao(BaseDAO):
    model = Slog
