# Вантажні послуги

Django-сайт для демонтажу, переїздів, вантажних перевезень і вивозу будівельного сміття.

## Локальний запуск

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Деплой на Render

1. Завантажте код на GitHub, не додаючи `.env` і `venv`.
2. У Render створіть **Web Service** з цього GitHub-репозиторію й у полі **Root Directory** вкажіть `transport`.
3. Build Command:

   ```text
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   ```

4. Start Command:

   ```text
   gunicorn config.wsgi:application
   ```

5. Створіть PostgreSQL базу в Render та додайте її `Internal Database URL` як `DATABASE_URL`.
6. Додайте змінні з `.env.example`, замінивши адреси на адресу Render-сервісу. Для `DJANGO_SECRET_KEY` використайте довгий випадковий рядок.

Після деплою відкрийте `/admin/`, створіть адміністратора командою `python manage.py createsuperuser` через Shell у Render або тимчасово локально для вашої бази даних.
