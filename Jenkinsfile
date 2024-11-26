pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Kinnaruo/sast-demo-app.git', branch: 'master'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Create a virtual environment and activate it
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install bandit
                '''
            }
        }
        stage('SAST Analysis') {
            steps {
                // Use the virtual environment to run Bandit
                sh '''
                    . venv/bin/activate
                    bandit -f xml -o bandit-output.xml -r . || true
                '''
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
            
