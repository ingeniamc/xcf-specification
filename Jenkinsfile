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
                sh "$python -m poetry install"
            }
        }
        stage('Validate XCF files') {
            steps {
                sh "$python -m poetry run pytest tests/ -v"
            }
        }
    }
}
