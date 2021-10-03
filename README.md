# AAIB-Challenge-Solution

A solution to the AAIB coding challenge

## Getting Started

### Development

```
# clone repo
git clone git@github.com:ibrahimawadhamid/AAIB-Challenge-Solution.git
cd AAIB-Challenge-Solution

## Terminal 1 - setup backend ##

cd backend
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# start backend service
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

## Terminal 2 - setup frontend ##

cd frontend
npm install
cp .env.example .env

# start frontend
npm start
```

### Docker

```
# clone repo
git clone git@github.com:ibrahimawadhamid/AAIB-Challenge-Solution.git
cd AAIB-Challenge-Solution

# start docker containers
docker-compose up -d

```

Open browser at [http://localhost:3000](http://localhost:3000)
