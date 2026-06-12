pipeline {
    agent {
        docker{
            image 'mcr.microsoft.com/playwright:v1.60.0-noble'
            args '-U root -v $Home/.npm:/.npm'
        }

    }

    environment {
        npm_config_cache = '/.npm'
        CI = "true"
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Execute Playwright Test') {
            steps {
                sh 'npx playwright test'
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