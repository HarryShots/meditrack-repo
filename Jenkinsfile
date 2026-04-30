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
        # Install Python dependencies
        #sudo yum install python3 -y
        pip3 install --upgrade pip
        pip3 install -r requirements.txt

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
