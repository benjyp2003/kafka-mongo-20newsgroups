docker stop interesting-subscriber 2>nul
docker rm interesting-subscriber 2>nul

docker rmi interesting-subscriber-app:latest 2>nul


docker build -t interesting-subscriber:latest .
docker run -d --name interesting-subscriber-container -p 8001:8001 interesting-subscriber-app:latest
