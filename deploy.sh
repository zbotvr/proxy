#!/bin/bash

echo "Deploying to GitHub..."

git add .
git commit -m "Auto deploy update"
git push origin main

echo "Deployment complete."