def python = "python3.12"

pipeline {
    agent {
        docker {
            label 'worker'
            image 'ingeniacontainers.azurecr.io/docker-python:1.6'
        }
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh "$python -m poetry install --with tests"
            }
        }
        stage('Run tests') {
            steps {
                sh "$python -m poetry run pytest --junitxml=pytest_reports/junit.xml"
            }
            post {
                always {
                    junit "pytest_reports/junit.xml"
                }
            }
        }
    }
}
