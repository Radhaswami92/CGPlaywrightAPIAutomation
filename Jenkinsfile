pipeline {
    agent {
        docker {
            image "mcr.microsoft.com/playwright/python:v1.60.0-noble"
        }
    }
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Radhaswami92/CGPlaywrightAPIAutomation.git', branch: "docker_linux_jenkins"
            }
        }
        stage('Run Tests inside Playwright Container') {
            steps {
                sh """
                    mkdir -p test_reports
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    python -m pytest Learn_Playwright_BDD_Framework/StepDefinitionFiles --url_name=${params.Environment} --alluredir=allure-results --html=test_reports/report.html
                """
            }
        }
    }
    post {
        always {
            script {
                if (params.Report_Type == "Allure" || params.Report_Type == "Both") {
                    allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
                }
                if (params.Report_Type == "HTML" || params.Report_Type == "Both") {
                    archiveArtifacts 'test_reports/**'
                }
            }
            cleanWs()
        }
    }
}
