# Kafka News Classification System

A microservices-based news article classification system built with Python, FastAPI, Apache Kafka, and MongoDB. The system processes newsgroup articles, categorizes them as "interesting" or "not interesting," and stores them in MongoDB for further analysis.

## 🏗️ Architecture

The system consists of three main microservices:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│    Publisher    │    │ Interesting     │    │ Not Interesting │
│   (Port 8000)   │    │ Subscriber      │    │ Subscriber      │
│                 │    │ (Port 8001)     │    │ (Port 8002)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │  Apache Kafka   │
                    │  (Port 9092)    │
                    └─────────────────┘
                                 │
                    ┌─────────────────┐
                    │    MongoDB      │
                    │  (Port 27017)   │
                    └─────────────────┘
```

### Components

- **Publisher**: Loads newsgroup data and publishes articles to Kafka topics based on category classification
- **Interesting Subscriber**: Consumes articles from the "interesting_categories" topic and stores them in MongoDB
- **Not Interesting Subscriber**: Consumes articles from the "not_interesting_categories" topic and stores them in MongoDB
- **Apache Kafka**: Message broker for asynchronous communication between services
- **MongoDB**: Document database for storing categorized articles

## 📋 Prerequisites

- Docker Desktop
- Docker Compose (included with Docker Desktop)
- Python 3.8+ (for local development only)

## 🚀 Quick Start

The easiest way to run the entire system using Docker Compose:

```bash
# Start all services
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Stop and remove volumes (clean slate)
docker-compose down -v
```


## 🔌 API Endpoints

### Publisher Service (Port 8000)
- `GET /` - Welcome message
- `GET /publish` - Publish articles to Kafka topics

### Interesting Subscriber Service (Port 8001)
- `GET /` - Welcome message
- `GET /get_interesting_articles` - Retrieve stored interesting articles

### Not Interesting Subscriber Service (Port 8002)
- `GET /` - Welcome message
- `GET /get_not_interesting_articles` - Retrieve stored not interesting articles

### Service URLs
- Publisher: http://localhost:8000
- Interesting Subscriber: http://localhost:8001
- Not Interesting Subscriber: http://localhost:8002
- MongoDB: mongodb://localhost:27017
- Kafka: localhost:9092

## 💾 Data Storage

Articles are stored in MongoDB with the following structure:

```json
{
  "topic": "interesting_categories",
  "partition": 0,
  "offset": 123,
  "key": null,
  "category": "comp.graphics",
  "article_data": {
    "category": "comp.graphics",
    "text": "Article content...",
    "target": 1
  },
  "time_stamp": "2024-01-01T12:00:00Z"
}
```

Each category is stored as a separate document, making it easy to query and analyze articles by category.

## 🔧 Usage Workflow

1. **Start the system** using Docker Compose:
   ```bash
   docker-compose up -d --build
   ```

2. **Publish articles** by calling:
   ```bash
   curl http://localhost:8000/publish
   ```

3. **Articles are automatically consumed** by the subscriber services and stored in MongoDB

4. **Retrieve stored articles** by calling:
   ```bash
   # Get interesting articles
   curl http://localhost:8001/get_interesting_articles
   
   # Get not interesting articles
   curl http://localhost:8002/get_not_interesting_articles
   ```

5. **Check system status**:
   ```bash
   docker-compose ps
   docker-compose logs
   ```

## 🐳 Docker Configuration

### Docker Compose Services

The system uses Docker Compose to orchestrate all services:

- **MongoDB**: `mongodb` - Document database (Port 27017)
- **Kafka**: `kafka` - Message broker (Port 9092)  
- **Publisher**: `publisher-container` - Article publisher (Port 8000)
- **Interesting Subscriber**: `interesting-subscriber-container` - Consumer service (Port 8001)
- **Not Interesting Subscriber**: `not-interesting-subscriber-container` - Consumer service (Port 8002)

All containers are connected via the `kafka-news-network` Docker network with persistent volumes for data storage.

### Environment Variables

The services use the following environment variables:

```yaml
# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS=kafka:9092

# MongoDB Configuration  
MONGO_DATABASE=news-articles
MONGO_HOST=mongodb
MONGO_PORT=27017
```

## 🧹 Cleanup

### Docker Compose Cleanup
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (complete cleanup)
docker-compose down -v

# Remove unused Docker resources
docker system prune -f
```



## 🛠️ Development

### Project Structure
```
├── publisher/
│   ├── app/
│   │   ├── data/
│   │   ├── data_loader.py
│   │   ├── kafka_producer.py
│   │   ├── main.py
│   │   └── manager.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── interesting_subscriber/
│   ├── app/
│   │   ├── consumer.py
│   │   ├── dal.py
│   │   ├── main.py
│   │   └── manager.py
│   ├── Dockerfile
│   └── requirements.txt
│   
├── not_interesting_subscriber/
│   ├── app/
│   │   ├── consumer.py
│   │   ├── dal.py
│   │   ├── main.py
│   │   └── manager.py
│   ├── Dockerfile
│   └── requirements.txt
│   
├── docker-compose.yml
└── README.md
```

### Key Technologies
- **FastAPI**: Modern, fast web framework for building APIs
- **Apache Kafka**: Distributed streaming platform (Bitnami image)
- **MongoDB**: NoSQL document database
- **Docker & Docker Compose**: Containerization and orchestration
- **Python**: Primary programming language

### Docker Compose Structure
```yaml
# docker-compose.yml includes:
services:
  mongodb:        # Database service
  kafka:          # Message broker
  publisher:      # Article publisher
  interesting-subscriber:     # Consumer for interesting articles
  not-interesting-subscriber: # Consumer for not interesting articles

networks:
  kafka-news-network:  # Internal network

volumes:
  kafka_data:     # Persistent Kafka data
  mongodb_data:   # Persistent MongoDB data
```



### Health Checks

All services include health checks. Check their status:
```bash
docker-compose ps
```

Healthy services will show `Up (healthy)` status.

