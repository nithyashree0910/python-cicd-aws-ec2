pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t devops-deployment-api:1.0.0 .'
            }
        }

        stage('Deploy Locally') {
            steps {
                bat '''
                    docker rm -f devops-api 2>NUL
                    docker run -d --name devops-api -p 8000:8000 devops-deployment-api:1.0.0
                '''
            }
        }

        stage('Health Check') {
            steps {
                bat '''
                    powershell -Command "$response = Invoke-RestMethod http://127.0.0.1:8000/health; if ($response.status -ne 'healthy') { exit 1 }"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline successful!'
        }

        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}