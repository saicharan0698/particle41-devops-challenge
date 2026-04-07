# Particle41 DevOps Team Challenge - SimpleTimeService

This repository contains my submission for the Particle41 DevOps challenge. It includes a containerized Go-based microservice and the Terraform code required to provision a production-ready EKS environment on AWS.

## 📁 Project Structure

```text
.
├── app/
│   ├── main.py            # SimpleTimeService source code
│   ├── Dockerfile         # Optimized multi-stage build (Non-root)
│   └── microservice.yml   # K8s Deployment & NodePort Service
└── terraform/
    ├── main.tf            # VPC & EKS Cluster definition
    ├── variables.tf       # Input variables
    ├── outputs.tf         # Useful resource IDs
    └── terraform.tfvars   # Default configuration values

## 🛠 Prerequisites
Before you begin, ensure you have the following installed:
1. AWS CLI (configured with access keys)
2. Terraform (v1.0+)
3. kubectl
4. Docker (optional, for local testing)

## Task 1: SimpleTimeService (App & K8s)
The SimpleTimeService is a minimalist web server that returns the current timestamp and the visitor's IP address in JSON format.

Container Security
Non-Root Execution: The application runs as a non-root user (UID 1001) inside the container to adhere to security best practices.

Lightweight: Built using a minimal base image to reduce the attack surface.

Deployment
To deploy the service to your Kubernetes cluster:


kubectl apply -f app/microservice.yml
🌍 Accessing the Service (NodePort)
The service is exposed via NodePort. Since the EKS nodes are in private subnets, you can access the service using one of these two methods:

Method 1: Port Forwarding (Easiest for Review)
This is the recommended way to verify the service without modifying AWS Security Groups:


kubectl port-forward svc/simple-time-service 8080:80
Access the API at: http://localhost:8080

Method 2: Internal Node Access
If you are within the VPC or have a VPN/Bastion setup:

Find the assigned NodePort: kubectl get svc simple-time-service

Get the Private IP of a node: kubectl get nodes -o wide

Access via: http://<NODE_PRIVATE_IP>:<NODE_PORT>



## 🏗 Task 2: Infrastructure (Terraform & AWS)
The Terraform configuration provisions:

A VPC with 2 Public and 2 Private subnets.

An EKS Cluster with a managed node group.

2x m6a.large Nodes deployed strictly within Private Subnets for security.

Deployment Instructions
Navigate to the terraform directory:


cd terraform
Initialize and apply:


terraform init
terraform apply
Update your local kubeconfig to connect to the new cluster:

aws eks update-kubeconfig --region <REGION> --name <CLUSTER_NAME>


🧹 Cleanup
To avoid ongoing AWS costs, destroy the resources once the review is complete:

terraform destroy
