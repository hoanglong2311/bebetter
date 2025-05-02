# CI/CD Setup for Netlify Deployment

This repository is configured with GitHub Actions to automatically deploy to Netlify when code is pushed to the main branch or when pull requests are created/updated.

## Setup Instructions

To make the automatic deployments work, you need to configure two secrets in your GitHub repository:

1. **NETLIFY_AUTH_TOKEN**: A personal access token from Netlify
2. **NETLIFY_SITE_ID**: Your Netlify site ID

### How to get these values:

#### Netlify Auth Token
1. Log in to your Netlify account
2. Go to User Settings (click your avatar in the top right)
3. Go to Applications
4. Under "Personal access tokens", click "New access token"
5. Give it a name (e.g., "GitHub Actions")
6. Copy the generated token

#### Netlify Site ID
1. Log in to your Netlify account
2. Go to your site
3. Go to Site Settings
4. The Site ID is listed under "Site information"

### Adding Secrets to GitHub

1. Go to your GitHub repository
2. Click on "Settings"
3. Click on "Secrets and variables" then "Actions"
4. Click "New repository secret"
5. Add the two secrets with the exact names:
   - `NETLIFY_AUTH_TOKEN`
   - `NETLIFY_SITE_ID`

## How It Works

- When you push to the main branch, the site will be built and deployed to production
- When you create or update a pull request, a preview deployment will be created

The GitHub Actions workflow is defined in `.github/workflows/netlify-deploy.yml`
