pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS = credentials("dockerhub")
    }

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
                sh 'docker run --name score_cont -d -p 5000:5000 main_score:2.0'
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
                script {
                    withCredentials(bindings: [usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                        sh 'docker build -t adiros/score_pipe .'
                        sh 'docker push adiros/score_pipe'
                        sh 'docker rm score_cont'
                    }
                }
            }
        }
    }


                
     
