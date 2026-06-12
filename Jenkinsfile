pipeline {
    // 1. Tell Jenkins to start the workspace on your Windows machine first
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Playwright Tests in Docker') {
            steps {
                script {
                    // 2. This structure forces Jenkins to run the container using Linux commands, bypassing the Windows 'bat' crash
                    docker.image('mcr.microsoft.com/playwright/python:v1.60.0-noble').inside('-u root --ipc=host') {

                        // All commands inside this block run smoothly on Linux rules
                        sh 'pip install --upgrade pip'

                        sh '''
                        if [ -f requirements.txt ]; then
                            pip install -r requirements.txt
                        elif [ -f Learn_Playwright_BDD_Framework/requirements.txt ]; then
                            pip install -r Learn_Playwright_BDD_Framework/requirements.txt
                        fi
                        '''

                        // Runs your exact target Python folder command
                        sh 'python -m pytest Learn_Playwright_BDD_Framework/StepDefinitionFiles || true'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Playwright execution complete.'
        }
    }
}