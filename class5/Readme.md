
# **Flask Blog Web Application – AWS EC2 Deployment**
## **Scope**

This project demonstrates deploying a containerized Flask-based blog web application on AWS ECS, backed by a PostgreSQL database on Amazon RDS, and securely exposed to the public internet using an Application Load Balancer (ALB) with HTTPS via AWS Certificate Manager (ACM).

The primary goals of this setup are:

● Containerized deployment using Docker<br>
● Scalable and managed container orchestration with ECS<br>
● Persistent data storage using RDS (PostgreSQL)<br>
● Secure public access using HTTPS<br>
● Domain-based access using a custom DNS name<br>

##**Architecture Overview**<br>

**Flask Web Application**<br>
● Built using Flask.<br>
● Listens on port 5000 inside the container.<br>
● Responsible for creating and serving blog posts.<br>

**Docker Container**

● The Flask app is packaged into a Docker image.<br>
● The container exposes port 5000.<br>

**IAM**

● An IAM User represents a non-human identity used by applications or developers.<br>
● We disable console access because:<br>
    ● The user is meant for programmatic access only<br>
    ● It reduces security risk<br>
● AdministratorAccess is attached only for learning purposes.<br>
    ● In production, use least-privilege policies.<br>

**Amazon ECS**

● ECS runs the Docker container as a service.<br>
● ECS handles container lifecycle and availability.<br>
● The service is registered as a target for the Application Load Balancer.<br>

**Amazon RDS (PostgreSQL)**

● Used as the backend database to store blog posts.<br>
● ECS tasks connect to RDS using security group rules.<br>
● Database credentials are configured via environment variables or secrets.<br>

**Application Load Balancer (ALB)**

● Serves as the public entry point.<br>
● Terminates HTTPS using an ACM certificate.<br>
● Forwards incoming HTTPS requests to ECS tasks over HTTP port 5000.<br>

**AWS Certificate Manager (ACM)**

● SSL/TLS certificate issued for *.rrd-devops.xyz.<br>
● Certificate is attached directly to the ALB (non-exportable).<br>

**Domain & DNS**

● Domain: rrd-devops.xyz<br>
● Subdomain used: nov25.rrd-devops.xyz<br>
● DNS record points nov25.rrd-devops.xyz to the ALB.<br>

## **Deployment Steps**
1. Build the Flask Application

        Develop the Flask blog application.
        Configure the app to listen on port 5000.
        Ensure database connection parameters (host, user, password, DB name) are configurable via environment variables.

2. Containerize the Application

        Create a Dockerfile for the Flask app.
        Expose port 5000 inside the container.
        Build the Docker image locally.
        Test the image using docker run -p 5000:5000.

3. Push Image to Amazon ECR

        Create a private repository in Amazon ECR.
        Authenticate Docker to ECR.
        Tag and push the Docker image to the ECR repository.

4. Create PostgreSQL Database (RDS)

        Launch an Amazon RDS PostgreSQL instance.
        Place RDS inside the same VPC as ECS.
        Configure security groups to allow inbound traffic on 5432 only from EC2
        Note the RDS endpoint for application configuration.

5. Configure EC2 service

        Create an EC2 instance
        Install Docker and Docker compose
        Create an IAM role for EC2 instance
        Attach the role to EC2 instance and set the security groups
        Deploy the docker image in EC2 instance
        Database can be connected as they are in the same VPC via 5432
        Run the container in EC2 and check from local url

6. Create Application Load Balancer (ALB)

        Create an Application Load Balancer in public subnets.
        Configure:
            Listener on HTTPS (443).
            Target Group pointing to ECS tasks on HTTP port 5000.
        Set up health checks for the Flask application.

7. Configure ACM Certificate

        Request a wildcard certificate for *.rrd-devops.xyz using AWS Certificate Manager.
        Validate the certificate via DNS.
        Attach the ACM certificate to the ALB HTTPS listener.

8.  Configure Route 53 DNS

        Create a hosted zone for rrd-devops.xyz in Route 53.
        Add an A record (Alias):
            nov25.rrd-devops.xyz → Application Load Balancer.
        DNS now routes public traffic to the ALB.
        Add the ns servers in the Namecheap (domain provider)

9.  Verify Deployment

        Access the application via: [https://nov25.rrd-devops.xyz] (https://nov25.rrd-devops.xyz)
        The site will be live until **11.01.2026** and will be taken down to save free credits. 
        Confirm:
            HTTPS is working.
            Blog posts are stored and retrieved from RDS.
            ECS tasks are healthy behind the ALB.