# Website publication and maintenance

This repository is published at **https://bowen-ai.github.io/ai-accelerator-codesign/** using GitHub Pages and the workflow at [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml).

## Deployment architecture

The `main` branch contains the course source:

- `index.html` — course overview and interactive analytical demonstration.
- `curriculum.html` — weekly syllabus and learning outcomes.
- `readings.html` — original university resources and tools.
- `capstone.html` — final architecture assessment.
- `assets/site.css` — shared styles.
- `labs/` — locally executed Python teaching labs and automated tests.
- `docs/` — supporting technical notes.

The publishing workflow checks out `main`, assembles the HTML, stylesheet and supporting documents into a static artifact, and uses the official GitHub Pages upload/deployment actions. No npm, Jekyll, backend server or third-party deployment service is required.

## GitHub Pages configuration

GitHub Pages is configured to use **GitHub Actions** as the deployment source. Repository administrators can review this setting at [Settings → Pages](https://github.com/Bowen-AI/ai-accelerator-codesign/settings/pages).

Every change to the site files on `main` triggers a new deployment. Runs can be reviewed under the repository's [Actions tab](https://github.com/Bowen-AI/ai-accelerator-codesign/actions/workflows/deploy-pages.yml).

## Maintenance and integrity

The website publishes independently authored teaching material and links to official university sources. Do not mirror copyrighted university lecture materials unless their licenses explicitly permit it. Keep employer-confidential designs, benchmarks and data out of this public repository.

The interactive roofline model is analytical; it must not be described as a production accelerator emulator or a source of measured chip power, area or latency. Core Python exercises are executed locally, not on GitHub Pages.
