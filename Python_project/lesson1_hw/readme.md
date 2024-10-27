### Домашнее задание к 1 занятию:
1. Запустить приложение из первого занятия (RRS_Python_2024_Fall/Python_project/lesson1_hw/app) локально
```commandline
cd app # перейти в директорию приложения
uvicorn main:app # запустить приложение
```
2. Создать свой репозиторий и написать в нем несколько API тестов по swagger http://127.0.0.1:8000/docs#/
с использованием модулей client и response_logging from api_tests/utils/api_client

### Полезное 

1. Type hints: <https://mypy.readthedocs.io/en/stable/builtin_types.html>
2. Документация allure: <https://allurereport.org/docs/> 

Другие примеры костяков для автоматизации api: 
1. <https://habr.com/ru/articles/709380/> 
2. <https://habr.com/ru/articles/765512/>
3. <https://github.com/qa-guru/knowledge-base/wiki/17.-REST-API.-%D0%A7%D0%B0%D1%81%D1%82%D1%8C-II.-%D0%9F%D1%80%D0%BE%D0%B4%D0%BE%D0%BB%D0%B6%D0%B0%D0%B5%D0%BC-%D0%B8%D0%B7%D1%83%D1%87%D0%B0%D1%82%D1%8C>
4. <https://github.com/manikosto/live-coding-api-webinar>

Тест дизайн при тестировании api: 
1. <https://habr.com/ru/articles/704090/>