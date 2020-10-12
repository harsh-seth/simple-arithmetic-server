# Simple Arithmetic Server

### What
A small Python Flask server to compute the resultants of simple arithmetic operations. 

Designed to be a template to help give an introduction to the following topics: Python, Flask (servers in general), HTML + CSS, Git 


### How to Setup
1) Fork this repository

2) Clone it into your development environment with the following command
```
git clone https://github.com/<username>/simple-arithmetic-server
```

3) Navigate into the project folder and add the upstream remote
```
cd ./simple-arithmetic-server/
git remote add upstream https://github.com/harsh-seth/simple-arithmetic-server.git
```

4) Navigate to the `server` folder in the repository via CLI
```
cd ./src/server
```

5) Ensure that you have `pip3` installed on your machine with the command
```
pip3 --version
```
6) Install the server dependencies with the command
```
pip3 install -r requirements.txt
```

7) Start up the server with the command
```
py app.py
```

8) Navigate to `localhost:8080` to visit the page
