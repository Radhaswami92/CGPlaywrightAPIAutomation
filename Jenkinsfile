pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.59.0-noble' } }
   stages {
       stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }
      stage('e2e-tests') {
         steps {
            sh 'pip install -r requirements.txt'
            sh 'python -m pytest Learn_Playwright_BDD_Framework/StepDefinitionFiles --html=report.html || true'
         }
      }
   }
}