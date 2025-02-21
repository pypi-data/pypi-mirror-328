# Spatial Analysis Environment

This repo abstracts the basics of a spatial analysis environment, so it can be used consistently across microservices.

A slightly weird thing right now:
- We want to use conda for installation, because it helps manage a lot of the dependencies (GDAL)
- But we can't use conda for publishing, because the path to get on conda-forge seems like a pain and we haven't prioritized it. Eventually we'll use pixi, but pixi build is still in development.
- So we're using `uv` to publish, and that introduces some dependency mismatches.  We can see what those are with the `create-mismatch-report` target.  So far they have been minor.

## Environments

The `environments` directory contains the base environment and any other environments that are needed.

The `base` environment is the core dependencies for all later tooling and environments.

The `analysis` environment is used for later tooling that is specific to analysis (like RasterOps and VectorOps).

The `jupyter` environment is used for the Jupyter notebook and includes RasterOps and VectorOps.

The `pmtiles` environment is used for the PMTiles tooling.

## Usage

### Adding a new dependency

When adding a new dependency to the project:

1. Add the package to `environments/base/base.yml`:
```yaml
dependencies:
  - new-package>=1.0.0
```

2. Add the same package to `pyproject.toml`:
```toml
dependencies = [
    "new-package>=1.0.0",
]
```

3. Update the lock files:
```bash
make lock
```

4. Review the mismatch report at `version_info/mismatch_report.txt` to ensure version alignment between conda and uv

5. Test the environment:
```bash
make test-conda
```

Note: Package names might differ slightly between conda and pip (e.g., `memory_profiler` vs `memory-profiler`). Check both repositories if you encounter installation issues.

### Publishing
The package can be published to PyPI using the following workflow:

```bash
# First build the publisher container
make publisher-base

# Create a new lock file if dependencies have changed
make lock

# Publish to PyPI (requires UV_PUBLISH_TOKEN in .env.publish)
make publish
```

Note: Before publishing, ensure you have created a `.env.publish` file with your PyPI token:
```
UV_PUBLISH_TOKEN=your_token_here
```

## Deploying a Jupyter Notebook to Nautilus

### Prerequisites

1. Install `helm` (On MacOSX):
```bash
brew install helm
```
See https://helm.sh/docs/intro/install/ for other systems.

2. Configure AWS credentials:
Create a file named `.env.s3` with your Nautilus Cept S3 credentials:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_ENDPOINT_URL=your_endpoint_url
```

### Deployment

Create a deployment with a pod, ingress, and persistent volume unique to you:
```bash
make jupyter-deploy
```

Release resources when you're done:
```bash
make jupyter-teardown
```
