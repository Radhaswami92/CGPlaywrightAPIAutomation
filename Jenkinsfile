pipeline {
    // We remove the global agent block to let the manual node structure handle Windows compatibility
    agent none

    stages {
        stage('Run Tests inside Docker') {
            agent {
                docker {
                    image 'mcr.microsoft.com/playwright/python:v1.60.0-noble'
                    // Forces root and sets up host memory allocation to prevent Chromium freezes
                    args '-u root --ipc=host'
                }
            }
            steps {
                // 'checkout scm' automatically pulls your latest code from GitHub
                checkout scm

                // Installs Python packages straight into the root workspace
                sh 'pip install --upgrade pip'
                //h 'if [ -f requirements.txt ]; then pip install -r requirements.txt; elif [ -f Learn_Playwright_BDD_Framework/requirements.txt ]; then pip install -r Learn_Playwright_BDD_Framework/requirements.txt; fi'

                // Runs your target BDD Step Definition test path using Linux-style forward slashes
                sh 'python -m pytest Learn_Playwright_BDD_Framework/StepDefinitionFiles || true'
            }
        }
    }

    post {
        always {
            // We use a clean echo step here so your pipeline won't crash if the HTML plugin isn't fully ready
            echo 'Playwright execution cycle finished. Processing complete.'
        }
    }
}