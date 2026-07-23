 🚀 End-to-End DevOps CI/CD PlatformProduction-Inspired CI/CD Pipeline with GitHub Actions, Docker, Kubernetes, Prometheus & GrafanaA production-inspired DevOps portfolio project demonstrating how a multi-component Python application is automatically tested, containerized, deployed to Kubernetes, monitored with Prometheus and Grafana, and auto-scaled using the Horizontal Pod Autoscaler (HPA).Rather than focusing solely on the calculator application itself, this repository showcases the complete software delivery lifecycle—from source code management to automated deployment and observability—using modern DevOps practices.📑 Table of ContentsProject OverviewWhy This Project?Project HighlightsSystem ArchitectureTechnology StackRepository StructureGetting StartedPrerequisitesLocal Setup & DeploymentCI/CD Pipeline DetailsKubernetes & AutoscalingMonitoring & ObservabilityScreenshotsSkills DemonstratedFuture ImprovementsAuthor📖 Project OverviewThis project simulates a real-world DevOps workflow by automating the build, test, deployment, and monitoring of a web-based calculator application.The application consists of a Python Flask backend API and a static HTML/CSS/JS frontend running on NGINX. Every code change triggers a Continuous Integration (CI) pipeline that validates code style and functionality before building Docker images. A Continuous Deployment (CD) workflow then updates the Kubernetes cluster, where traffic is routed via an Ingress controller and monitored via Prometheus metrics.💡 Why This Project?Modern software engineering teams rely on automation to deliver software quickly, consistently, and reliably.This project was built to demonstrate hands-on experience with industry-standard DevOps tools and workflows:Automated Quality Checks: Ensuring code quality and passing unit tests before any container build.Microservice Containerization: Decoupling frontend and backend components into distinct lightweight containers.Orchestration & Resiliency: Managing deployments, internal routing, and traffic ingress using Kubernetes.Dynamic Resource Scaling: Auto-scaling application pods based on real-time CPU load.Observability: Collecting runtime cluster metrics to enable proactive monitoring.✨ Project Highlights🚀 End-to-End CI/CD via GitHub Actions with separate CI and CD workflow pipelines.🐳 Decoupled Architecture with isolated Docker containers for frontend (NGINX) and backend (Flask).☸ Kubernetes Native deployment featuring Services, Deployments, and Ingress routing.📈 Automated Autoscaling configured via Kubernetes Horizontal Pod Autoscaler (HPA).📊 Full Observability integrated with Prometheus metrics collection and Grafana dashboards.✅ Quality Testing automated using PyTest for unit tests and Flake8 for linting.🏗 System ArchitecturePlaintext                        Developer
                            │
                            ▼
                  GitHub Repository
                            │
                 Push / Pull Request
                            │
                            ▼
                GitHub Actions (CI)
            ┌──────────────────────────┐
            │ Install Dependencies     │
            │ Run PyTest               │
            │ Run Flake8 Linting       │
            │ Build Docker Images      │
            └──────────────────────────┘
                            │
                            ▼
                     Docker Hub Registry
                            │
                            ▼
                GitHub Actions (CD)
                            │
                            ▼
                  Kubernetes Cluster
         ┌─────────────────────────────────┐
         │ Frontend Deployment (NGINX)     │
         │ Backend Deployment (Flask)      │
         │ ClusterIP Services              │
         │ NGINX Ingress Controller        │
         │ Horizontal Pod Autoscaler (HPA) │
         └─────────────────────────────────┘
                            │
                            ▼
                    Prometheus Metrics
                            │
                            ▼
                    Grafana Dashboards
🛠 Technology StackCategoryTechnologies / ToolsProgramming / WebPython 3.x, Flask, HTML5, CSS3, JavaScriptContainerizationDocker, NGINXOrchestrationKubernetes, Minikube / KindCI/CD PipelinesGitHub ActionsConfiguration & NetworkingKubernetes Manifests, NGINX IngressMonitoring & MetricsPrometheus, Grafana, Metrics ServerTesting & QualityPyTest, Flake8📂 Repository StructurePlaintext.
├── .github/
│   └── workflows/
│       ├── ci.yml              # CI pipeline (Build, Lint, Test, Docker Push)
│       └── cd.yml              # CD pipeline (Deploy to Kubernetes)
├── frontend/
│   ├── Dockerfile              # Dockerfile for NGINX Frontend
│   ├── index.html              # Web Calculator Interface
│   ├── nginx.conf              # NGINX custom configuration
│   ├── script.js               # Frontend Logic
│   └── style.css               # Styling
├── k8s/
│   ├── deployment.yaml         # Backend Deployment
│   ├── service.yaml            # Backend Service
│   ├── frontend-deployment.yaml# Frontend Deployment
│   ├── frontend-service.yaml   # Frontend Service
│   ├── ingress.yaml            # NGINX Ingress Manifest
│   └── hpa.yaml                # Horizontal Pod Autoscaler Manifest
├── calculator.py               # Flask REST API entry point
├── logic.py                    # Core Calculator Business Logic
├── test_logic.py               # PyTest Suite
├── Dockerfile                  # Dockerfile for Flask Backend
├── requirements.txt            # Python Dependencies
└── ReadMe.md                   # Project Documentation
🚀 Getting StartedPrerequisitesEnsure you have the following installed locally:Python 3.10+ & pipDocker DesktopkubectlMinikube (or Kind)Helm (optional, for Prometheus/Grafana stack)Local Setup & DeploymentClone the RepositoryBashgit clone https://github.com/abdulwahedmutayyib/end-to-end-CI-CD-Calculator-project-.git
cd end-to-end-CI-CD-Calculator-project-
Local Python Setup & TestingBash# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests and linter
pytest
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
Build & Run Containers via DockerBash# Build backend
docker build -t calculator-backend:latest .

# Build frontend
docker build -t calculator-frontend:latest ./frontend
Deploy to Kubernetes (Minikube)Bash# Start local cluster
minikube start

# Enable Ingress and Metrics Server
minikube addons enable ingress
minikube addons enable metrics-server

# Apply manifests
kubectl apply -f k8s/

# Verify cluster state
kubectl get pods
kubectl get svc
kubectl get ingress
🔄 CI/CD Pipeline DetailsThe project utilizes two decoupled workflows configured in .github/workflows/:StageTriggerProcess / ToolsCI (Build & Validate)Push/PR to mainRuns PyTest and Flake8 linting. On success, builds Docker images and pushes tagged versions to Docker Hub.CD (Deploy)Successful CI RunConnects to the Kubernetes cluster and applies updated manifests (kubectl apply) using rolling update strategies.📊 Horizontal Pod AutoscalerThe backend deployment is integrated with Kubernetes HPA to automatically scale based on target CPU utilization:SettingConfiguration ValueTarget MetricTarget CPU Utilization: 50%Min Replicas2 PodsMax Replicas5 PodsBash# Check HPA status
kubectl get hpa
📈 Monitoring & ObservabilityObservability is handled via Prometheus for metrics collection and Grafana for dashboard visualization:Cluster Metrics: Monitors Node CPU, Memory consumption, and Pod deployment health via Kubernetes Metrics Server.Prometheus Targets: Scrapes application metrics and resource usage across cluster namespaces.Grafana Visualization: Displays live dashboard graphs tracking pod scaling events, latency, and memory footprints.📸 ScreenshotsAdd images below by placing files inside a docs/images/ directory.Calculator Application InterfaceGitHub Actions Passing PipelineKubernetes Pods & Services StatusGrafana Metrics Dashboard🎯 Skills DemonstratedEnd-to-End CI/CD Pipeline ArchitectureDocker Container Optimization & Multi-stage BuildsKubernetes Deployment Strategies & Ingress ConfigurationHorizontal Pod Autoscaling (HPA) & Load ManagementObservability with Prometheus & GrafanaUnit Testing & Automated Code Linting🚀 Future Improvements[ ] Helm Chart packaging for simplified Kubernetes release management.[ ] Infrastructure provisioned via Terraform on AWS EKS.[ ] Security scanning integration using Trivy for Docker images and SonarQube for static analysis.[ ] Transition CD delivery model to GitOps using Argo CD.👨‍💻 AuthorAbdul Wahed MutayyibDevOps EngineerGitHub: github.com/abdulwahedmutayyibLinkedIn: linkedin.com/in/abdulwahedmutayyib⭐ If you found this project helpful, feel free to give it a star on GitHub!

