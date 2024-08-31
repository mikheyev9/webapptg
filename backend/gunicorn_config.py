import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
bind = "0.0.0.0:8000"
loglevel = "info"
accesslog = "-"
timeout = 30
graceful_timeout = 30
max_requests = 1000
# accesslog = "logs/access.log"
# errorlog = "logs/error.log"