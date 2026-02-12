#!/bin/bash
# Скрипт для автоформатирования кода

echo "🚀 Форматируем код с помощью Black..."
poetry run black src tests

echo "📦 Сортируем и чистим импорты с помощью isort..."
poetry run isort src tests

echo "✅ Готово! Проверим линтер снова..."
poetry run flake8 src tests
