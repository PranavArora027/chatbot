
# CUSTOM CHATBOT

A custom chatbot application that integrates with openai and allows users to login/signup through firebase and is deployed on an EC2 server further allowing to upload files to the server that is processed to save in a S3 bucket.

## Environment Variables

To run this project, you will need to create add the following environment variables to your .env file in the below format.

```bash
API_KEY = 
S3_BUCKET_NAME = 
apiKey = 
authDomain = 
projectId = 
storageBucket = 
messagingSenderId = 
appId = 
measurementId = 

```


## Installation on local machine

Clone the project in your local machine.

```bash
  git clone "github_project_link"
```
Install docker on your computer.
```bash
  pip install docker
```
Build the docker image.
```bash
  docker build -t 'chatbot' .
```
Run a container with the image.
```bash
  docker run --detach -p 8501:8501 'chatbot'
```
GOTO:
```bash
  localhost:8501
```


## Uploading to EC2 server.

1. Create an EC2 server using amazon linux as AMI and allow connection from anywhere on port 8501.

2. Create IAM Role with full access to S3.

3. Attach this IAM role to the EC2 server.

4. Create S3 bucket and write bucket policy such that only the above IAM role can access that bucket.

5. Connect to EC2 server.

6. Get root access.

```bash
  sudo su
```

7. Update the packages.

```bash
  yum update
```

8. Install git.

```bash
  yum install git
```

9. Clone the project on the EC2 server.

```bash
  git clone "github_project_link"
```

10. Install pip

```bash
  yum install python3-pip
```

11. Install docker.

```bash
  pip install docker
```
12. create add the environment variables to your .env file in the above mentioned format.

13. Build the docker image.
```bash
  docker build -t 'chatbot' .
```
14. Run a container with the image.
```bash
  docker run --detach -p 8501:8501 'chatbot'
```
15. GOTO:
```bash
  @ec2_publicip:8501
```