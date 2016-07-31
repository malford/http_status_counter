# Http Status Code Counter

This is a simple script to count up http status codes from a Nginx access.log file.

By default it will use the `access.log` file located in `/var/log/nginx/`. You could also provide a your own nginx `access.log` file as an argument.

Depending on environment this may need to be ran with root access.

```
Usage:
  count_http_status_codes.py [/path/to/nginx/access.log]
```
