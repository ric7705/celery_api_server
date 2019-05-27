# Dev Note

## run UT/coverage

execute unit test:
```
py.test
```

execute coverage:

```
py.test --cov=app
```

export coverage to html, to htmlcov folder
```
py.test --cov=app --cov-report=html
```

## execute the celery server
start celery worker (in task_server directory)

CPU bound:
```
celery worker -A app.celery --concurrency 4 --loglevel=info
```

IO bound:

```
celery worker -A app.celery -P gevent --loglevel=info --concurrency 20
``` 