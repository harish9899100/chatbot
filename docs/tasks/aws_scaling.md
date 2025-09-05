# AWS Auto Scaling Setup

## 🔧 Prerequisites

Before starting, ensure the following are complete:

### ✅ AWS CLI Installed

Install the AWS CLI on your local machine or deployment server:

```bash
# On macOS
brew install awscli

# On Ubuntu/Debian
sudo apt install awscli

# Or via pip (cross-platform)
pip install awscli
```

### ✅ AWS Credentials Configured

Run the following to configure your AWS credentials:

```bash
aws configure
```

You'll be prompted to enter:

* AWS Access Key ID
* AWS Secret Access Key
* Default region name (e.g., `us-east-1`)
* Default output format (e.g., `json`)

🔐 These will be saved in `~/.aws/credentials` and `~/.aws/config`.

### ✅ Environment Variables Set

Ensure the following environment variables are set **before running** the `aws_scaling.rake` task:

```bash
export AWS_LAUNCH_TEMPLATE_NAME="your-template-name"
export AWS_ASG_NAME="your-auto-scaling-group"
export AWS_ALB_TARGET_GROUP_ARN="your-target-group-arn"
export AWS_SUBNET_ID="your-subnet-id"
export AWS_SECURITY_GROUP_ID="your-security-group-id"
export AWS_KEY_NAME="your-key-name"
export AWS_INSTANCE_TAG_KEY="your-tag-key"         # e.g., Role
export AWS_INSTANCE_TAG_VALUE="your-tag-value"     # e.g., app-server
```

---

# AWS Auto Scaling Setup

This guide outlines the steps to set up Auto Scaling for a **Rails** application on AWS, covering all necessary networking, security, and compute resources.

---

## 0. Create a VPC and Networking Resources (AWS Console)

If you don’t already have a VPC, create one using the AWS Management Console:

### 0.1 Create a VPC

* Go to the **VPC Dashboard**.
* Click **Your VPCs** → **Create VPC**.
* Enter a name and a CIDR block (e.g., `10.0.0.0/16`).
* Click **Create VPC**.

### 0.2 Create Subnets

* In the **VPC Dashboard**, click **Subnets** → **Create Subnet**.
* Select your VPC, specify a name, choose an Availability Zone, and assign a CIDR block (e.g., `10.0.1.0/24`).
* Create **at least two subnets** in different Availability Zones for high availability.

### 0.3 Create and Attach an Internet Gateway

* In the **VPC Dashboard**, click **Internet Gateways** → **Create Internet Gateway**.
* Name it and click **Create**.
* Select the new Internet Gateway → **Actions** → **Attach to VPC** → select your VPC.

### 0.4 Update Route Tables

* In the **VPC Dashboard**, click **Route Tables** and select the main route table.
* Under **Routes**, click **Edit routes** → **Add route**:

  * Destination: `0.0.0.0/0`
  * Target: your Internet Gateway
* Under **Subnet Associations**, associate this route table with your **public subnets**.

### 0.5 (Optional) Create Private Subnets

* In the **VPC Dashboard**, click **Subnets** → **Create Subnet**.
* Use a different CIDR block (e.g., `10.0.10.0/24`).
* **Do not associate** private subnets with the route table that routes through the Internet Gateway.

### 0.6 (Optional) Configure a NAT Gateway

* In the **VPC Dashboard**, click **NAT Gateways** → **Create NAT Gateway**.
* Select a **public subnet** and allocate a new Elastic IP.
* Update the route table for **private subnets** to send `0.0.0.0/0` traffic to the NAT Gateway.

---

## 1. Create a Security Group

A security group acts as a virtual firewall for your EC2 instances.

* Go to **EC2 Dashboard** → **Security Groups** → **Create Security Group**.
* Add inbound rules for:

  * **SSH (port 22)**: Your IP only
  * **HTTP (port 80)**: Anywhere (0.0.0.0/0)
  * **HTTPS (port 443)**: Anywhere (0.0.0.0/0)
  * Any custom ports your app needs (e.g., 3000)
* Outbound rules are typically open by default.
* If you have an existing suitable security group, reuse it.

---

## 2. Create a Key Pair

A key pair is required to SSH into your EC2 instances.

* Go to **EC2 Dashboard** → **Key Pairs** → **Create Key Pair**.
* Download and securely store the `.pem` file.
* If you already have a key pair, you can reuse it.

---

## 3. Create a Load Balancer

A Load Balancer distributes incoming traffic across instances.

* Go to **EC2 Dashboard** → **Load Balancers** → **Create Load Balancer**.
* Choose **Application Load Balancer** (recommended).
* Add listeners: **HTTP (port 80)** and **HTTPS (port 443)**.
* For HTTPS, ensure you have an ACM certificate and SSL policy.
* Assign the security group created above.
* Add **at least two subnets** in different Availability Zones for HA.

---

## 4. Create a Target Group

A target group defines where the Load Balancer sends traffic.

* Go to **EC2 Dashboard** → **Target Groups** → **Create Target Group**.
* Choose **Instances** as the target type.
* Set the protocol/port (e.g., HTTP:80).
* Register instances manually or leave empty — the Auto Scaling Group will attach instances automatically.
* Reuse an existing target group if appropriate.

---

## 5. Create a Launch Template

A launch template defines EC2 configuration.

* Go to **EC2 Dashboard** → **Launch Templates** → **Create Launch Template**.
* Specify:

  * AMI ID (use a Rails-ready AMI or your custom image)
  * Instance type (e.g., t3.micro)
  * Key pair
  * Security group
  * User data script (optional: install packages, pull code, start Rails, etc.)
  * Network settings (subnet, public IP)
* Keep your template versioned if you update it later.

---

## 6. Create an Auto Scaling Group

The ASG manages the desired number of instances.

* Go to **EC2 Dashboard** → **Auto Scaling Groups** → **Create Auto Scaling Group**.
* Attach the launch template.
* Set desired, minimum, and maximum instance counts.
* Attach the Load Balancer and Target Group.
* Configure scaling policies (e.g., scale out if CPU > 70%).
* Use **ELB health checks** for better accuracy.

---

## Additional Best Practices

* Use **IAM roles** for EC2 instances to access other AWS services securely.
* Store app secrets in **SSM Parameter Store** or **Secrets Manager** — avoid hardcoding.
* Use **CloudWatch** for logs, metrics, and alarms.
* Use **RDS/Aurora** for managed databases.
* Use **S3** for static asset storage.

---

## 📚 References

* [EC2 Docs](https://docs.aws.amazon.com/ec2/)
* [Auto Scaling Docs](https://docs.aws.amazon.com/autoscaling/)
* [Load Balancer Docs](https://docs.aws.amazon.com/elasticloadbalancing/)

---

## 🚀 Deploy / Scale Up

When your setup is ready and environment variables are configured, deploy or scale with Capistrano:

```bash
cap staging aws:scale_up
```

Replace `staging` with your environment name.

---

## ✅ Final Tips

* Make sure your AMI is **up to date** with all app dependencies.
* Always test scaling in a **staging environment** first.
* Verify your Load Balancer listeners include **both HTTP and HTTPS** — with a valid **ACM certificate** attached to the HTTPS listener.
