# Analyze, choose, and justify the appropriate resource option for deploying the app

## Analyze costs, scalability, availability, and workflow

### Virtual Machine (VM)
- **Cost**: Higher cost due to always-on infrastructure. You pay for the VM even when idle.
- **Scalability**: Manual scaling required. Need to configure load balancers and scale sets yourself.
- **Availability**: High availability possible but requires manual configuration of availability sets.
- **Workflow**: More complex. Requires SSH access, manual setup of web server (nginx), Python environment, and dependencies.

### App Service
- **Cost**: Lower cost with free and basic tiers available. Pay only for the plan, not idle compute.
- **Scalability**: Built-in auto-scaling with simple configuration. Scale up or out easily.
- **Availability**: Built-in high availability with SLA of 99.95%.
- **Workflow**: Simple deployment via GitHub Actions. No server management needed.

## Justification for choosing App Service

I chose **Azure App Service** to deploy the Article CMS for the following reasons:

1. The application is a lightweight Flask web app that does not require full control over the underlying infrastructure. App Service handles all server management automatically, allowing focus on the application code itself.

2. App Service integrates directly with GitHub for CI/CD deployment, making it much simpler to deploy code changes. This reduces deployment time and risk of errors compared to manually configuring a VM with nginx and gunicorn.

3. For a CMS application of this scale, App Service's built-in scaling and availability features are more than sufficient, at a lower cost than running a dedicated VM.

## What would change my decision?

If the application requirements changed significantly, I might reconsider using a VM. For example, if the app needed custom software that cannot run on App Service (such as specific OS-level dependencies or custom runtimes), a VM would be necessary. Additionally, if the application needed to run background processes or daemons, or required full control over networking and security configurations, a VM would be a better choice. Finally, if the application scaled to millions of users requiring very specific performance tuning at the OS level, a VM or AKS (Kubernetes) would be more appropriate.
