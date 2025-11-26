def python = "python3.12"

pipeline {
    agent {
        docker {
            label 'worker'
            image 'ingeniacontainers.azurecr.io/docker-python:1.4'
        }
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh "$python -m pip install xmlschema==3.2.1"
            }
        }
        stage('Validate XCF files') {
            steps {
                sh "$python validate_example_files.py"
            }
        }
    }
}
