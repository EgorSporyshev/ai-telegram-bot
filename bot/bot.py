# ===============================
#  Конфиг Telegram AI бота
#  (пример: скопируйте в config.yml и заполните токены)
# ===============================

# Версия схемы конфига (для совместимости).
schema_version: 3

# -------------------------------
# Telegram
# -------------------------------
telegram:
  # Токен бота от @BotFather.
  token: ""

  # Разрешённые пользователи (по username без @).
  # Если список пуст, бот будет доступен всем.
  usernames: []
  # примеры:
  # usernames: ["alice", "bob"]

  # Админы — могут менять настройки через /config.
  # Если список пуст, никто не может менять настройки.
  admins: []
  # примеры:
  # admins: ["alice"]

  # Разрешённые групповые чаты (по ID).
  # Если пусто — разрешены только пользователи из telegram.usernames.
  chat_ids: []
  # примеры:
  # chat_ids: [-1001405001234, -1007778889990]

# -------------------------------
# Параметры ИИ (OpenAI-совместимые провайдеры)
# -------------------------------
openai:
  # Эндпоинт API (любой OpenAI-совместимый провайдер):
  #   - OpenAI:     https://api.openai.com/v1
  #   - OpenRouter: https://openrouter.ai/api/v1
  #   - Nebius:     https://api.studio.nebius.ai/v1
  url: "https://api.openai.com/v1"

  # API-ключ провайдера.
  api_key: ""

  # Имя чат-модели (пример: gpt-4o-mini).
  # Смотрите актуальные модели у вашего провайдера.
  model: "gpt-4o-mini"

  # Имя модели генерации изображений (если используется).
  image_model: "dall-e-3"

  # Размер контекста (только для кастомных моделей; можно не трогать).
  window: 128000

  # Базовый системный промпт (тон/роль бота).
  prompt: "You are an AI assistant."

  # Параметры генерации (см. доку провайдера).
  params:
    temperature: 0.7
    max_tokens: 4096

# -------------------------------
# Диалог/лимиты
# -------------------------------
conversation:
  # Глубина «памяти» — сколько предыдущих сообщений учитывать.
  depth: 3

  # Лимит сообщений для НЕзанесённых в telegram.usernames пользователей.
  # Помогает не сжечь бюджет в больших группах.
  # count = 0 означает без ограничений.
  message_limit:
    count: 0
    period: hour   # minute | hour | day

# -------------------------------
# Генерация изображений
# -------------------------------
imagine:
  # Режим доступа к генерации изображений:
  #   - none              — выключено для всех
  #   - users_only        — только пользователи из telegram.usernames
  #   - users_and_groups  — пользователи из telegram.usernames и участники из telegram.chat_ids
  enabled: none

# -------------------------------
# Хранение состояния (контекста)
# -------------------------------
persistence_path: "./data/persistence.pkl"

# -------------------------------
# Шорткаты (кастомные команды с готовыми промптами)
# Вызов: начните сообщение с !имя_шортката
# -------------------------------
shortcuts:
  bugfix: >
    Examine the following code. Rewrite it if necessary to fix bugs and various problems.
    Explain the changes you've made.

  proofread: >
    Proofread the following text. Correct grammar and punctuation errors. Rephrase if necessary.
    Make sure the resulting text is clear, concise, and easy to read. Explain the changes you've made.

  summarize: >
    Explain the following text in simple terms. Use no more than two paragraphs.

  translate: >
    Translate the following text into English.

  # Пример русского шортката (добавленный для наглядности):
  # perevedi: >
  #   Переведи следующий текст на русский язык. Сохраняй смысл, стиль и термины.