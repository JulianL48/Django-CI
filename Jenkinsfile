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
                git branch: 'Facturacion', url: 'https://github.com/JulianL48/Django-CI.git'
            }
        }
        stage('Set up Python') {
            steps {
                // Configura Python 3.8
                bat 'py -m venv venv'
                bat '.\\venv\\Scripts\\activate && python -m pip install --upgrade pip'
            }
        }
        stage('Install dependencies') {
            steps {
                // Instala las dependencias
                dir('MarketProject') {
                    bat '.\\..\\venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Run makemigrations') {
            steps {
                // Ejecuta makemigrations
                dir('MarketProject') {
                    bat '.\\..\\venv\\Scripts\\activate && python manage.py makemigrations'
                }
            }
        }
        stage('Run migrations') {
            steps {
                // Ejecuta migrate
                dir('MarketProject') {
                    bat '.\\..\\venv\\Scripts\\activate && python manage.py migrate'
                }
            }
        }
        stage('Set up Python path') {
            steps {
                // Configura el PYTHONPATH
                script {
                    env.PYTHONPATH = "${WORKSPACE}\\MarketProject"
                }
            }
        }
        stage('Run tests') {
            steps {
                // Ejecuta pytest con cobertura
                dir('MarketProject') {
                    withEnv(["DJANGO_SETTINGS_MODULE=MarketProject.settings"]) {
                        bat '.\\..\\venv\\Scripts\\activate && pytest --cov=. --cov-report=xml'
                    }
                }
            }
        }
        stage('SonarCloud Scan') {
            steps {
                // Ejecuta el análisis de SonarCloud
                dir('MarketProject') {
                    bat '''.\\..\\venv\\Scripts\\activate &&
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
            bat 'rmdir /s /q venv'
        }
    }
}