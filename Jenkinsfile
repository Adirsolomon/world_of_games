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
                sh 'docker build -t score_server .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:8777 -v $(pwd)/scores.txt:/app/scores.txt score_server'
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
            sh 'docker push score_server'
        }
    }
}