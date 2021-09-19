# AAIB-Challenge-Solution
A solution to the AAIB coding challenge


## Getting Started


```
# clone repo
git clone git@github.com:ibrahimawadhamid/AAIB-Challenge-Solution.git
cd AAIB-Challenge-Solution

# setup backend
virtualenv venv
source venv/bin/activate
pip install -r ./backend/requirements.txt

# start backend
uvicorn backend.main:app

# setup frontend
cd frontend
npm i
cp .env.example .env

# start frontend
npm start
```