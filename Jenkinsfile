pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Kinnaruo/sast-demo-app', branch: 'master'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install bandit'
            }
        }
        stage('SAST Analysis') {
            steps {
                // Run Bandit for static analysis, outputting to an XML file
                sh 'bandit -f xml -o bandit-output.xml -r . || true'

                // Record and display the Bandit analysis results in Jenkins
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
