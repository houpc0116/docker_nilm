#!/bin/sh

echo 'Run migration'
python manage.py makemigrations
python manage.py migrate
echo 'Create Super User'
# 使用 manage.py createsuperuser 命令建立 superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell
exec "$@"
