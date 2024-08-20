pipeline {
    agent any

    environment {
        SECRET_KEY = credentials('SECRET_KEY')
        SONAR_TOKEN = credentials('SONAR_TOKEN')
    }

    stages {
        stage('Checkout') {
            steps {
                // Clona el repositorio
                git 'https://tu-repositorio-git.git'
            }
        }
        stage('Set up Python') {
            steps {
                // Configura Python 3.8
                sh 'python3.8 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
            }
        }
        stage('Install dependencies') {
            steps {
                // Instala las dependencias
                dir('MarketProject') {
                    sh '. ../venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Run makemigrations') {
            steps {
                // Ejecuta makemigrations
                dir('MarketProject') {
                    sh '. ../venv/bin/activate && python manage.py makemigrations'
                }
            }
        }
        stage('Run migrations') {
            steps {
                // Ejecuta migrate
                dir('MarketProject') {
                    sh '. ../venv/bin/activate && python manage.py migrate'
                }
            }
        }
        stage('Set up Python path') {
            steps {
                // Configura el PYTHONPATH
                script {
                    env.PYTHONPATH = "${WORKSPACE}/MarketProject"
                }
            }
        }
        stage('Run tests') {
            steps {
                // Ejecuta pytest con cobertura
                dir('MarketProject') {
                    withEnv(["DJANGO_SETTINGS_MODULE=MarketProject.settings"]) {
                        sh '. ../venv/bin/activate && pytest --cov=. --cov-report=xml'
                    }
                }
            }
        }
        stage('SonarCloud Scan') {
            steps {
                // Ejecuta el análisis de SonarCloud
                dir('MarketProject') {
                    sh '''. ../venv/bin/activate &&
                        sonar-scanner \
                        -Dsonar.projectKey=JulianL48_Django-CI \
                        -Dsonar.organization=julianl48 \
                        -Dsonar.sources=./MarketProject \
                        -Dsonar.host.url=https://sonarcloud.io \
                        -Dsonar.python.coverage.reportPaths=coverage.xml \
                        -Dsonar.branch.name=Facturacion \
                        -Dsonar.exclusions=**/wsgi.py,**/asgi.py,**/manage.py'''
                }
            }
        }
        stage('Upload coverage report') {
            steps {
                // Publica el reporte de cobertura
                archiveArtifacts artifacts: 'MarketProject/coverage.xml', fingerprint: true
            }
        }
    }

    post {
        always {
            // Limpia el entorno
            sh 'rm -rf venv'
        }
    }
}