# API Documentation

This API provides endpoints to manage and control processes, as well as retrieve their status and results.

## Requirements

- Python 3.8+
- FastAPI (https://fastapi.tiangolo.com/)
- Docker (https://www.docker.com/)

## Installation and Usage

1. Clone this repository to your local machine.

2. Install the dependencies by running the following command in the project directory:
   
   pip install -r requirements.txt
   

3. Run the API locally with the following command:
   
   uvicorn api.main:app --reload
   
   This will start the API on http://localhost:8000.

4. To generate the API documentation, navigate to http://localhost:8000/api/docs in a web browser.

5. To start, stop, and check the status and results of processes, use the following endpoints:
   - POST /api/pn/start - Start a process
   - POST /api/pn/stop - Stop a process
   - GET /api/pn - Check the status of a process
   - GET /api/pn/result - Retrieve the result of a process

## Docker

To run the API in a Docker container:

1. Build the Docker image:
   
   docker build -t myapi .
   

2. Run the Docker container:
   
   docker run -d --name myapi-container -p 80:80 myapi
   
   This will start the API on http://localhost in a Docker container. 

## Testing

To run the tests, run the following command in the project directory:
pytest


## License

This API is released under the MIT License (https://opensource.org/licenses/MIT).s