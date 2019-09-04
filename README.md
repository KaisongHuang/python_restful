# python_restful

I'm trying to build a restful API using flask.

### Setup environment
1. flask
2. nginx
```
cd /etc/nginx/sites-enabled/
sudo vim flaskapp
```
add config below:
```
server{
        listen 80;
        server_name 3.17.147.251;

        location / {
                proxy_pass http://127.0.0.1:8000;
        }
}
```
3. gunicorn
```
gunicorn helloworld:app
```
4. change security rules on EC2 console, add `HTTP` & `HTTPS` in `inbound` rules
