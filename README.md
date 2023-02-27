# shortener
Docker lecture repository at [Avito's Analytics Academy](https://avito-analytics-academy.ru/) Data Science course.

## Step 1. Build
```bash
docker build -t shortener:0.0.1 .
docker images
```
## Step 2. Run
```bash
# run redis
docker run --name shortener-redis -d -p 6379:6379 -v $(pwd)/data:/data redis redis-server --save 60 1
# run shortener
docker run --rm -d -p 5500:5500 --name=shortener shortener:0.0.1
docker ps
```
## Step 3. Test
```bash
curl -X POST http://127.0.0.1:5500/urls/ -d 'https://avito-analytics-academy.ru/'
```
