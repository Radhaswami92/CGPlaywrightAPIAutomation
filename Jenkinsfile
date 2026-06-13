pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.60.0-noble'
            args '-u root'
        }
    }
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Radhaswami92/CGPlaywrightAPIAutomation.git', branch: 'master'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                //sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Playwright Tests') {
            steps {
                sh 'python -m pytest Learn_Playwright_BDD_Framework/StepDefinitionFiles'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
