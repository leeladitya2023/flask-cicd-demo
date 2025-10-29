pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_NAME = "leeladitya2024/flask-cicd-demo"
    }

    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/leeladitya2023/flask-cicd-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                    echo Building Docker image...
                    docker build -t leeladitya2024/flask-cicd-demo:latest -f app/Dockerfile .
                """
            }
        }

        stage('Test Container') {
            steps {
                bat """
                    echo Running test container...
                    docker run -d -p 5000:5000 --name flask_test %IMAGE_NAME%:latest
                    timeout /t 5
                    curl http://localhost:5000
                    docker stop flask_test
                    docker rm flask_test
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat """
                    echo Logging in to Docker Hub...
                    echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin
                    echo Pushing image to Docker Hub...
                    docker push %IMAGE_NAME%:latest
                """
            }
        }

        stage('Deploy') {
            steps {
                bat """
                    echo Deploying latest container...
                    docker stop flask_cicd_demo
                    docker rm flask_cicd_demo
                    docker run -d -p 5000:5000 --name flask_cicd_demo %IMAGE_NAME%:latest
                    echo Deployment complete.
                """
            }
        }
    }
}

