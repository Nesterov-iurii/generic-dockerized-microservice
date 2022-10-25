FROM python:3.9-slim

WORKDIR /app

EXPOSE 5000

# Install the dependencies: openssh-client, git
RUN apt-get update && \
    apt-get install -y openssh-client && \
    apt-get install -y --no-install-recommends git

# Create the directory .ssh and add mygitlab to known_hosts
RUN mkdir -p -m 0600 ~/.ssh && \
    ssh-keyscan mygitlab >> ~/.ssh/known_hosts

COPY requirements.txt .
RUN --mount=type=ssh,id=gitlab_ssh_key pip install -r requirements.txt
COPY . .

CMD ["uvicorn", "service.app:app", "--host=0.0.0.0", "--port=5000"]
