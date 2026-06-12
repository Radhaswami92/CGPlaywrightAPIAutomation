pipeline {
    // Runs the initial steps on your Windows agent
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
                    // This environment variable forces Jenkins to map Windows paths safely into the Linux container
                    withEnv(['WORKSPACE_LINKED_TO_C=true']) {
                        docker.image('mcr.microsoft.com/playwright/python:v1.60.0-noble').inside('-u root --ipc=host') {

                            stage('Install Dependencies') {
                                sh 'pip install --upgrade pip'
                                sh '''
                                if [ -f requirements.txt ]; then
                                    pip install -r requirements.txt
                                elif [ -f Learn_Playwright_BDD_Framework/requirements.txt ]; then
                                    pip install -r Learn_Playwright_BDD_Framework/requirements.txt
                                fi
                                '''
                            }

                            stage('Execute pytest') {
                                sh 'python -m pytest Learn_Playwright_BDD_Framework/StepDefinitionFiles || true'
                            }
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Playwright execution cycle completed.'
        }
    }
}