## FastApi Backend: Chatbot
- This is a fastApi backend that will be used fro chatbot to communicate with the frontend.

### HOW TO RUN
- To run the backend, you just need to clone the repo and run the `run_backend.sh` script. This will build the docker image and run the container.

```bash
cd backend/setup
./run_backend.sh
```

### FILE STRUCTURE

```
.
├── backend
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── setup
│       ├── docker-compose.yml
│       └── run_backend.sh
└── README.md
```

### ENDPOINTS
- The backend has the following endpoints:
    - `/`: This is the root endpoint. It returns a welcome message.
