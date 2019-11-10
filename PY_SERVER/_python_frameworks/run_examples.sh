docker ps | grep -v CONTAINER | awk '{print $1}' | xargs docker stop
docker run -p 8000:8000 -itd python-example
docker run -p 8001:8000 -itd flask-example
docker run -p 8002:8000 -itd chalice-example
docker run -p 8003:8000 -itd django-example
