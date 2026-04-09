pipeline {
  agent any

  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    IMAGE_NAME = 'harryshots/meditrack'
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

stage('Test') {
  steps {
    sh '''
    python3 -m venv venv
    source venv/bin/activate

    # Upgrade pip FIRST
    pip install --upgrade pip

    # Install dependencies
    pip install -r requirements.txt

    # Install pytest
    pip install pytest

    # Run tests
    pytest
    '''
  }
}

    stage('Build Image') {
      steps {
        sh '''
        docker build -t $IMAGE_NAME:latest .
        '''
      }
    }

    stage('Push to Docker Hub') {
      steps {
        sh '''
        echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
        docker push $IMAGE_NAME:latest
        '''
      }
    }
  }

  post {
    always {
      sh 'docker logout'
    }
  }
}
