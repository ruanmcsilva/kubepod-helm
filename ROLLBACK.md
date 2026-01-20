## Rollback Strategy

A failed upgrade was simulated by deploying a non-existent image tag.
The application entered an ImagePullBackOff state.

Helm rollback was used to restore the last known good release,
demonstrating safe recovery and production readiness.
