Overview
My project demonstrates the process of building, deploying, and managing a containerized application using Docker, AWS CodeBuild, Amazon Elastic Container Registry (ECR), and Kubernetes. It involves setting up a continuous integration/continuous deployment (CI/CD) pipeline to automate the process and ensuring the application runs smoothly in a Kubernetes cluster with proper logging and monitoring.

Docker and ECR
Store Docker Images in ECR: A Docker image was successfully built and pushed to Amazon ECR.

AWS CodeBuild Pipeline: An AWS CodeBuild pipeline was created and configured to automatically trigger on a push event to the linked GitHub repository. The pipeline builds the Docker image and pushes it to Amazon ECR.

Kubernetes Configuration
Deployment and Service Configuration: Kubernetes YAML configuration files were created to deploy the application. The configurations include:

Deployment: Configures the application's deployment.
Service: Sets up the necessary services.
ConfigMap: Shares plaintext environment variables.
Secrets: Manages sensitive environment variables securely.
Successful Deployment: The application was successfully deployed to the Kubernetes cluster.

Kubernetes Database Service: A PostgreSQL database service was created and deployed within the Kubernetes cluster.

Logging and Monitoring
CloudWatch Container Insights: CloudWatch Container Insights logs were reviewed to ensure the application is operating normally. The logs periodically print the health status of the application, confirming that it runs without errors.
Conclusion
This project demonstrates the full lifecycle of a containerized application, from building and pushing Docker images to ECR, setting up a CI/CD pipeline with AWS CodeBuild, and deploying the application and database services in a Kubernetes cluster. Comprehensive logging and monitoring ensure that the application runs smoothly and is ready for production.