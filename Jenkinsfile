pipeline {
  agent any

  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    IMAGE_NAME = 'harryshots/meditrack-v2'
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
            # Use the specific version we installed instead of generic pip3
            python3.12 -m venv venv
            . venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
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
