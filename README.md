# AWS Certified Generative AI Developer Professional (AIP-C01)
## Study Guide — GitHub Pages Site

A fully static HTML study guide converted from the AIP-C01 course slides.

---

## 📁 File Structure

```
aws-genai-aip-c01/
├── index.html                          ← Home/overview page
├── sitemap.html                        ← Visual sitemap
├── sitemap.xml                         ← XML sitemap for Google Search Console
├── robots.txt                          ← SEO robots file
├── style.css                           ← All styles
├── .nojekyll                           ← Disables Jekyll processing
├── generative-ai-fundamentals-and-bedrock.html
├── managing-data-for-generative-ai.html
├── agentic-ai.html
├── operations-efficiency-and-optimization.html
├── managing-models-with-sagemaker-ai.html
├── more-tools-for-building-ai-applications.html
├── governance-and-qa.html
├── security-identity-and-compliance.html
├── other-services-analytics.html
├── other-services-compute-containers.html
├── other-services-database.html
├── other-services-developer-tools.html
├── other-services-machine-learning.html
├── other-services-storage-networking.html
└── exam-preparation.html
```

---

## 🚀 Deploying to GitHub Pages

### Step 1: Create a GitHub Repository
1. Go to [github.com](https://github.com) and click **New repository**
2. Name it: `aws-genai-aip-c01`
3. Set to **Public**
4. Click **Create repository**

### Step 2: Upload the Files
**Option A – GitHub Web UI (easiest):**
1. In your new repo, click **Add file → Upload files**
2. Drag all files from this folder into the upload area
3. Click **Commit changes**

**Option B – Git CLI:**
```bash
cd aws-genai-aip-c01
git init
git add .
git commit -m "Initial commit: AIP-C01 study guide"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/aws-genai-aip-c01.git
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repo → **Settings** → **Pages**
2. Under **Source**, select **Deploy from a branch**
3. Choose **main** branch, **/ (root)** folder
4. Click **Save**
5. Your site will be live at: `https://YOUR-USERNAME.github.io/aws-genai-aip-c01/`

### Step 4: Update URLs in sitemap.xml and robots.txt
Replace `YOUR-USERNAME` with your actual GitHub username in:
- `sitemap.xml` (all `<loc>` entries)
- `robots.txt` (the Sitemap line)

### Step 5: Submit to Google Search Console (optional)
1. Go to [search.google.com/search-console](https://search.google.com/search-console)
2. Add property with your GitHub Pages URL
3. Submit `sitemap.xml` under **Sitemaps**

---

## 📊 Site Contents

| Section | Slides |
|---|---|
| Generative AI Fundamentals and Bedrock | 59 |
| Managing Data for Generative AI | 34 |
| Agentic AI | 110 |
| Operations Efficiency and Optimization | 62 |
| Managing Models with SageMaker AI | 65 |
| More Tools for Building AI Applications | 51 |
| Governance and QA | 54 |
| Security, Identity, and Compliance | 51 |
| Other Services (Analytics, Compute, DB, etc.) | ~140 |
| Exam Preparation | 21 |

**Total: 665 slides across 15 sections**

---

*Generated from AWSCertifiedGenerativeAIDeveloper.pdf*
