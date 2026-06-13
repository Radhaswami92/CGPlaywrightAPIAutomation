pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // Pulls code directly from your master branch
                git url: 'https://github.com/Radhaswami92/CGPlaywrightAPIAutomation.git', branch: 'master'
            }
        }
        stage('Run Tests inside Playwright Container') {
            steps {
                // Changed from 'sh' to 'bat' to work natively on your Windows Jenkins runner
                bat '''
                    docker run --rm ^
                    -v "%WORKSPACE%":/workspace ^
                    -w /workspace ^
                    mcr.microsoft.com/playwright/python:v1.60.0-noble ^
                    bash -c "python -m pip install --upgrade pip && python -m pytest Learn_Playwright_BDD_Framework/StepDefinitionFiles"
                '''
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
