# Troubleshooting Guide

## ImagePullBackOff
Cause: Incorrect image tag
Resolution: Helm rollback to last stable release

## Pod not scaling
Cause: Resource limits too high
Resolution: Adjust HPA thresholds and requests
