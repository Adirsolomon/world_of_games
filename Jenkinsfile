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
                sh 'docker compose up --build'
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
            sh 'docker stop score_cont'
        }
        success {
            sh 'docker push main_score-main_score'
        }
    }
}
