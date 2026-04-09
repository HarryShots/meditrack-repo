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
    python3.8 -m venv venv
    source venv/bin/activate

    pip install --upgrade pip
    pip install -r requirements.txt
    pip install pytest

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
