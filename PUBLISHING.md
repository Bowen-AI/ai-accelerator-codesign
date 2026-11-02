# Publish the Bowen-AI course website

Repository: https://github.com/Bowen-AI/ai-accelerator-codesign

Expected URL *after GitHub Pages is enabled and deploys successfully*:
https://bowen-ai.github.io/ai-accelerator-codesign/

The course homepage is already in root-level index.html and needs **no build process**.

## One-time GitHub Pages setting
1. Open https://github.com/Bowen-AI/ai-accelerator-codesign/settings/pages
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Select branch **main** and folder **/(root)**.
4. Click **Save**.
5. After GitHub indicates the deployment succeeded, open the expected URL above.

If there is no Pages configuration available, check organization policies and Pages permissions. The connected GitHub integration can push source files but cannot toggle GitHub Pages settings via its available actions.

## Publishing notes
- The .nojekyll file disables Jekyll transformations; browser HTML and JavaScript run without a server backend.
- The simulator requires Python when run locally and is not executed by GitHub Pages.
- Website progress checkboxes are browser-local, not synced to GitHub.
- Repository is public. Do not upload confidential Google designs, benchmarks, internal documentation or specifications.
- Course materials are linked from university sites; the source repository contains independent summaries and original exercises, not mirrored copyrighted lectures.
