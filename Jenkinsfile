pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Radhaswami92/CGPlaywrightAPIAutomation.git', branch: 'master'
            }
        }
        stage('Execute Entirely Inside Playwright Container') {
            steps {
                // This command natively forces the container to open, installs packages, and executes tests entirely within its environment.
                bat '''
                    docker run --rm ^
                    -v "%WORKSPACE%":/workspace ^
                    -w /workspace ^
                    mcr.microsoft.com/playwright/python:v1.60.0-noble ^
                    bash -c "python -m pip install --upgrade pip && pip install pytest pytest-bdd && python -m pytest Learn_Playwright_BDD_Framework/StepDefinitionFiles"
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
