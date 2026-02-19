"# dataset-generator-proto-" 

Setup Instructions:

1. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate

2. Install required dependencies

pip install -r requirements.txt
playwright install

3. Set up SearXNG (search backend)

-> Clone the SearXNG Docker repository:

git clone https://github.com/searxng/searxng-docker.git
cd searxng-docker


-> Start the Docker containers (Docker must be running):

docker compose up -d


-> Verify that SearXNG is running by opening the following URL in your browser:

http://localhost:8080/

4. Run the project: 

python run.py
