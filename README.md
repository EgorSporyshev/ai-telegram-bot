
# 🤖 AI Telegram Bot

Учебный проект — Telegram-бот с искусственным интеллектом, работающий на базе современных языковых моделей:
[OpenAI](https://platform.openai.com/), [OpenRouter](https://openrouter.ai/), [Nebius](https://docs.nebius.com/) и [Gemini](https://ai.google.dev/gemini-api/docs/openai).

---

## ✨ Возможности

* 💬 Работает как в **личных чатах**, так и в **группах**
* 👤 Понимает прямые вопросы, упоминания и уточнения
* 🌍 Умеет получать данные из внешних ссылок (статьи, код, текстовые файлы)
* ⚡ Поддерживает **шорткаты** — короткие команды для быстрого действия
  *(proofread, translate, summarize и др.)*
* 📝 Позволяет задавать разные **промпты и модели** для каждого чата
* 🔧 Гибкая настройка прямо во время работы (`/config`)
* ⏳ Ограничения на количество сообщений для защиты бюджета
* 📎 Удобные мелочи: пересылка сообщений, ответы на файлы, длинные ответы в приложении файлом, редактирование вопросов

---

## 🚀 Примеры использования

**Личный чат**

> 🧑 Объясни Apache Kafka трёхлетнему ребёнку
>
> 🤖 Apache Kafka — это как большой почтовый ящик. Игрушки (компьютеры) кладут туда письма, и другие игрушки могут их забирать. Так они быстро делятся сообщениями.

**Группа**

> 🧑 @humblebot Кто играл Рамси Болтона в «Игре престолов»?
>
> 🤖 Рамси Болтона сыграл Иван Реон.

**Шорткат**

> 🧑 !proofread I can has write java programz
>
> 🤖 Исправленный текст: «I can write Java programs.»

---

## ⚙️ Основные команды

* `/help` — список команд
* `/retry` — повторить ответ на последний вопрос
* `/version` — информация о боте и модели
* `/prompt` — задать стиль ответа (например, «будь строгим учителем»)
* `/model` — выбрать модель (например, `gpt-4o-mini`)
* `/config` — изменить настройки «на лету»
* `/clear` — очистить контекст (если включена память)

---

## 🔑 Установка и запуск

### 1. Подготовка

1. Получите API-ключ у выбранного провайдера (например, [OpenAI](https://platform.openai.com/)).
2. Создайте Telegram-бота через [@BotFather](https://t.me/BotFather).
3. Клонируйте репозиторий:

```bash
git clone https://github.com/<ваш-логин>/ai-telegram-bot.git
cd ai-telegram-bot
```

### 2. Настройка

Скопируйте пример конфига и укажите токены:

```bash
cp config.example.yml config.yml
```

В файле `config.yml` пропишите:

* ваш `TELEGRAM_BOT_TOKEN` (от BotFather)
* ключ `OPENAI_API_KEY` (или другого провайдера)
* список разрешённых пользователей (`telegram.usernames`)

### 3. Запуск через Docker

```bash
docker compose up --build --detach
```

Остановить:

```bash
docker compose stop
```

Обновить:

```bash
docker compose down
git pull
docker compose up --build --detach
```

---

## 🧑‍💻 Запуск для разработки

```bash
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
cp config.example.yml config.yml
mkdir ./data
```

В `config.yml` добавьте токены и настройки, затем запустите бота:

```bash
python -m bot.bot
```


