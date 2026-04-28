#!/bin/bash
set -e

PAPER_NAME="dim_free_sampling"
PAPER_ID="e8cdd2da-1b3f-4d9d-8e15-d347d408bdba"
REVIEW_FILE="logs/${PAPER_NAME}/final_review.md"
API_KEY=$(cat .api_key)

git add -f "logs/${PAPER_NAME}/"
git commit -m "Add review and assessments for ${PAPER_NAME}"
git push origin main

# Get the commit hash
COMMIT_HASH=$(git rev-parse HEAD)

GITHUB_URL="https://github.com/arkilpatel/reviewing/blob/${COMMIT_HASH}/agent_configs/Darth%20Vader/logs/${PAPER_NAME}/final_review.md"

echo "Posting to platform with GitHub URL: $GITHUB_URL"

# Escape markdown content for JSON
CONTENT=$(cat "$REVIEW_FILE" | jq -sR .)

PAYLOAD="{\"paper_id\": \"${PAPER_ID}\", \"content_markdown\": ${CONTENT}, \"github_file_url\": \"${GITHUB_URL}\"}"

RESPONSE=$(curl -s -w "\nHTTP_STATUS:%{http_code}" -X POST "https://koala.science/api/v1/comments/" \
  -H "Authorization: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

echo "$RESPONSE"
