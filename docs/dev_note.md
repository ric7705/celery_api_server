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
celery worker -A app.celery --autoscale=10,2 --loglevel=info
```

IO bound:

```
celery worker -A app.celery -P gevent --loglevel=info --concurrency 20
``` 

## daemon with supervisor

```
[program:celery_api_server]
command=/root/.pyenv/versions/celery_api_server/bin/celery worker -A app.celery --loglevel=info --autoscale=10,2
numprocs=1
directory=/root/celery_api_server
startsecs=10
stopwaitsecs=0
autostart=false
autorestart=true
killasgroup=true
stdout_logfile=/root/supervisor/logs/celery_api_server.log
stderr_logfile=/root/supervisor/logs/celery_api_server.err
```