pipeline {
    // 1. Allocate a standard workspace node executor first
    agent any

    stages {
        stage('Execute Playwright Automation Suite') {
            // 2. Instruct Jenkins to run all steps inside this stage inside your container
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
                stage('Install Packages') {
                    steps {
                        // Standard Linux shell commands are now natively supported here
                        sh 'python -m pip install --upgrade pip'
                        sh 'pip install pytest pytest-bdd'
                    }
                }
                stage('Run Tests') {
                    steps {
                        sh 'python -m pytest Learn_Playwright_BDD_Framework/StepDefinitionFiles'
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
