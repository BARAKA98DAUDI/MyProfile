web: gunicorn profile_project.wsgi --workers=3 --timeout 120
release: python manage.py migrate && python manage.py collectstatic --noinput