pipeline {
    agent none

    stages {

        stage('Docker set up') {
            agent {
                docker {
                    image 'mcr.microsoft.com/playwright/python:v1.60.0-noble'
                    args '-u root --ipc=host'
                }
            }

        }
        stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --upgrade pip'
            }
        }

        stage('Execute Playwright Test') {
            steps {
                sh 'python -m pytest Learn_Playwright_BDD_Framework/StepDefinitionFiles --html=report.html || true'
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'playwright-report',
                reportFiles: 'index.html',
                reportName: 'Playwright Test Report'
            ])


        }


    }


}