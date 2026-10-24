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
            sh '''
            python3 -m venv venv
            ./venv/bin/python -m pip install --upgrade pip
            ./venv/bin/python -m pip install -r requirements.txt
            '''
            }
        }


    stage('Run Tests') {
steps {
sh './venv/bin/python -m pytest -v'
}
}


    stage('Build Docker Image') {
        steps {
            sh 'docker build -t devops-deployment-api:1.0.0 .'
        }
    }

    stage('Deploy Locally') {
    steps {
        sh '''
            docker rm -f devops-api || true
            docker run -d --name devops-api --network cicd-network -p 8000:8000 devops-deployment-api:1.0.0
        '''
    }
}

  stage('Health Check') {
    steps {
        sh '''
            for i in $(seq 1 10); do
                if curl -fsS http://devops-api:8000/health; then
                    exit 0
                fi
                sleep 2
            done
            exit 1
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
