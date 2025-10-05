from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()


class Settings(BaseModel):
    """
    Класс конфигурации приложения.
    Автоматически валидирует значения из .env.
    """
    bot_token: str = Field(..., alias="BOT_TOKEN", min_length=10)
    channel_id: str = Field(..., alias="CHANNEL_ID")
    webhook_host: str = Field(...,
alias="WEBHOOK_HOST")

    class Config:
        populate_by_name = True


def get_settings() -> Settings:
    """
    Загружает конфигурацию из .env и возвращает объект Settings.
    """
    data = {
        "BOT_TOKEN": os.getenv("BOT_TOKEN"),
        "CHANNEL_ID": os.getenv("CHANNEL_ID"),
    }
    return Settings(**data)


if __name__ == "__main__":
    settings = get_settings()
    print("✅ Конфигурация успешно загружена:")
    print(settings.model_dump())