# Welcome to Raven


## Mkdocs
```
mkdocs build
mkdocs build --clean
```

Note: --clean = (Remove old files from the site_dir before building (the default).)


## Celery
```
celery worker -A raven -l info
```

Note: [Celery Docs](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)