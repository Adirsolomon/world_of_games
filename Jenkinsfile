pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t main_score:2.0 .'
            }
        }

         stage('Run') {
            steps {
                sh 'docker run -d -p 5000:5000 main_score:2.0'
            }
        }

        stage('Test') {
            steps {
                sh 'python e2e.py'
            }
        }
    }

    post {
        always {
            sh 'docker stop $(docker ps -q)'
        }
        success {
            sh 'docker push main_score:2.0'
        }
    }
}
