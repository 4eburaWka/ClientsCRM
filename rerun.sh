docker build -t crm .
docker stop crm
docker rm crm
docker run -d --network network -v $(pwd)/db.sqlite3:/app/db.sqlite3 --name crm crm