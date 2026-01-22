# KubeProd Platform

Production-ready Kubernetes platform using Helm and GitOps.

## Architecture
- Kubernetes (kind)
- Helm charts for application packaging
- Argo CD for GitOps continuous delivery
- Horizontal Pod Autoscaler
- NetworkPolicy (zero-trust)
- RBAC with least privilege
- Secrets management
- Resource limits and requests

## Repositories
- kubepod-app: Application source code and Docker image
- kubepod-helm: Helm charts and environment configuration
- kubepod-gitops: GitOps manifests (Argo CD Applications)

## Deployment Flow
1. Code or config is committed to GitHub
2. Argo CD detects changes
3. Helm applies desired state
4. Kubernetes enforces security and scaling

## Production Practices
- Automated rollbacks using Helm
- Non-root containers
- Git as single source of truth
- Environment separation (dev/prod)

## Troubleshooting
Documented real failure scenarios:
- ImagePullBackOff
- Rollback strategy
