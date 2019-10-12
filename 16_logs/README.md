# Анализатор логов

Скрипт для анализа данных access.log файлов 

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5.
В качестве параметра нужно указать директорию в которой нужно файлы логов 
или указать путь к определенному файлу

Пример выполнения скрипта, Python 3.7:

```bash
$ python3 logs_parser.py -f access.log
{
    "access.log": {
        "Total sum of requests": 7,
        "Requests count by type": {
            "\"GET": 4,
            "\"POST": 3
        },
        "Top requests by ip": {
            "109.169.248.247": 2,
            "46.72.177.4": 2,
            "83.167.113.100": 2,
            "95.29.198.15": 1
        },
        "Top client errors requests": {
            "GET /administrator/ HTTP/1.1\" 400": 1
        },
        "Top server errors requests": {}
    }
}
```

