pipeline{
    agent any

    stages{
        stage("Checkout"){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Vamsi-Cloudangles/Dimond_new.git']]])
            }
        }
        stage("build"){
            steps{
                git branch: 'main', url: 'https://github.com/Vamsi-Cloudangles/Dimond_new.git'
            }
        }
        stage("load data"){
            steps{
                sh 'python3 Load_Data.py'
            }
        }
        stage("data analysis"){
            steps{
                sh 'python3 Data_Analysis.py'
            }
        }
        stage("data cleaning"){
            steps{
                sh 'python3 Data_Cleaning.py'
            }
        }
        stage("data visualization"){
            steps{
                sh 'python3 Data_Visualization.py'
            }
        }
        stage("feature engineering"){
            steps{
                sh 'python3 Feature_Engineering.py'
            }
        }
        stage("feature selection"){
            steps{
                sh 'python3 Feature_Selection.py'
            }
        }
        stage("data preprocessing"){
            steps{
                sh 'python3 Data_Preprocessing.py'
            }
        }
        stage("model selection"){
            steps{
                sh 'pyhton3 Model_Selection.py'
            }
        }
        
    }
    post{
        always{
            emailext body:"summery", subject: "Pipeline Status", to: 'vamsi.muramreddy@cloudangles.com'
        }
    }
}
