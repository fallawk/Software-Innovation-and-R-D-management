pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'echo "Fail!"; exit 1'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
	    mail to: 'aoxiaotian@foxmail.com',
	         subject: "Pipelin aways sending: ${currentBuild.fullDisplayName}",
		 body: "${env.BUILD_URL} aways send this"
        }
        success {
            echo 'This will run only if successful'
        }
	post {
	    mail to: 'aoxiaotian@foxmail.com',
	         subject: "Failed Pipelin: ${currentBuild.fullDisplayName}",
		 body: "Somethings is wrong with ${env.BUILD_URL}"
	}
        unstable {
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}

