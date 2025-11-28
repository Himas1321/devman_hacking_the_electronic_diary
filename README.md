# devman_hacking_the_electronic_diary
### Запуск скрипта на работающем сайте

- поместить файл `scripts.py` в папку с файлом `manage.py` проекта
- запустить django shell `python manage.py shell`
- запустить скрипт командой `from scripts import fix_marks, remove_chastisements, create_commendation`

### Примеры запуска скрипта

- Исправление всех плохих оценок на пятерки.
```python
fix_marks("имя ученика")
```

- Удаление замечаний учителей.
```python
remove_chastisements("имя ученика")
```

- Создание похвалы.
```python
create_commendation("имя ученика", "название предмета")
```
