## 🎬 Cloud-Integrated Media Proxy Engine

This toolkit bridges the gap between high-end film editorial workflows and cloud-native technical infrastructure. I designed this to automate the "ingest" phase of post-production, optimizing media for rapid review.

## 🚀 Engineering Highlights
* **Hardware Accelerated:** Custom FFmpeg configuration utilizing `h264_videotoolbox` for Apple Silicon (M1/M2/M3) acceleration.
* **Metadata Burn-in:** Automated Python logic to overlay source filenames, crucial for VFX and conform tracking.
* **Environment Architecture:** Built from the ground up using Homebrew for dependency management.

---

## 🛠️ Environment Setup & Installation

A professional media pipeline starts with a clean environment. 

### 1. Dependency Management (Homebrew)
Install the Homebrew package manager:
\`\`\`bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
\`\`\`

Configure the Shell Environment (ZSH):
\`\`\`bash
echo >> ~/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv zsh)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv zsh)"
\`\`\`

### 2. Media Engine (FFmpeg)
Install the FFmpeg binary:
\`\`\`bash
brew install ffmpeg
\`\`\`



### 📂 Project Architecture
To maintain a clean repository structure:
1. **Initialize Git:** \`git init\`
2. **Stage Assets:** \`git add .\`
3. **Commit:** \`git commit -m "feat: initial ffmpeg proxy engine"\`
4. **Deploy:** \`git push -u origin main\`




💻 Technical Stack
Language: Python 3.12

Engine: FFmpeg 8.1

VCS: Git / GitHub

Target: Cloud-Native Ingest Pipelines

# 🎬 Media Automation Toolkit (V1)
**Assistant Editor & Cloud Pipeline Automation**

This toolkit is a Python-based utility designed to streamline the ingest process for film and video post-production. It automates proxy generation with custom burn-ins and prepares files for cloud or local review.

## 🚀 Features
* **FFmpeg Integration:** Automated H.264 proxy generation (720p).
* **Dynamic Burn-ins:** Automatic filename and "PROXY" label overlays for easy identification.
* **Modular Destinations:** Toggleable logic for Local Desktop ingest or Frame.io Cloud upload.
* **Environment Safety:** Uses `.env` for secure API token management.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Libraries:** `ffmpeg-python`, `requests`, `python-dotenv`
* **External Tools:** FFmpeg, Frame.io V4 API

## 📖 The "403 Forbidden" Case Study
*During development, I successfully navigated Frame.io's V4 API transition. While the Free Tier currently restricts API uploads (403 Forbidden), the codebase is architected to be "Cloud-Ready" for Enterprise/Team workspaces.*

## 🏁 How to Run
1. Add your raw media to the `/Images` folder.
2. Run `python3 final_toolkit_v1.py`.
3. Check your `VANJA_REVIEW_FOLDER` on the Desktop!