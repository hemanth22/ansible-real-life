# Dashboard Hosting Guide

## 📁 Repository Structure

```
ansible-dashboard-reporting/
├── examples/                    # All dashboard HTML files go here
│   ├── demo-dashboard.html
│   ├── compliance-main-dashboard.html
│   └── ...
├── www-vars.yaml               # Dashboard metadata (titles, descriptions, categories)
├── generate-index.py           # Python script to generate index.html
├── generate-index.sh           # Bash alternative (simpler, no metadata)
├── index.html                  # Generated landing page
└── DASHBOARD-HOSTING.md        # This file
```

---

## 🚀 Quick Start

### Option 1: Using Python (Recommended)

**Advantages:**
- Uses metadata from `www-vars.yaml`
- Organized by categories
- Rich descriptions and styling
- Easy to maintain

**Steps:**
1. Add new dashboard HTML file to `examples/` folder
2. Edit `www-vars.yaml` to add metadata:
   ```yaml
   dashboards:
     your-new-dashboard.html:
       title: "Your Dashboard Title"
       description: "What this dashboard shows"
       category: "Operations"  # or "Security & Compliance", etc.
   ```
3. Run the generator:
   ```bash
   python3 generate-index.py
   ```
4. Open `index.html` in browser to preview

### Option 2: Using Bash (Simple)

**Advantages:**
- No dependencies (no Python/YAML needed)
- Auto-discovers all HTML files
- Quick and simple

**Steps:**
1. Add new dashboard HTML file to `examples/` folder
2. Run the generator:
   ```bash
   ./generate-index.sh
   ```
3. Open `index.html` in browser to preview

---

## 🌐 Hosting on Cloudflare Pages

### Prerequisites
- GitHub/GitLab repository with this code
- Cloudflare account (free tier works great)

### Deployment Steps

1. **Login to Cloudflare Dashboard**
   - Go to https://dash.cloudflare.com
   - Navigate to "Pages" in the sidebar

2. **Connect Your Repository**
   - Click "Create a project"
   - Click "Connect to Git"
   - Select your GitHub/GitLab account
   - Choose this repository

3. **Configure Build Settings**
   ```
   Build command:     python3 generate-index.py
   Build output dir:  /
   Root directory:    /
   ```
   
   Or if using bash:
   ```
   Build command:     ./generate-index.sh
   Build output dir:  /
   Root directory:    /
   ```

4. **Deploy**
   - Click "Save and Deploy"
   - Cloudflare will build and deploy automatically
   - You'll get a URL like: `https://your-project.pages.dev`

5. **Auto-Deploy on Git Push**
   - Every push to main branch triggers automatic rebuild
   - Changes appear in ~30 seconds

---

## 🎨 Customization

### Editing Site Metadata (Python version only)

Edit `www-vars.yaml`:

```yaml
site:
  title: "Your Company Dashboard Gallery"
  subtitle: "Custom subtitle here"
  author: "Your Name"
  github_repo: "https://github.com/yourusername/your-repo"
  year: 2024
```

### Adding a New Category

Just add it in `www-vars.yaml`:

```yaml
dashboards:
  my-new-dashboard.html:
    title: "Network Monitoring"
    description: "Real-time network metrics"
    category: "Networking"  # New category - will auto-create section
```

### Styling Changes

Both scripts generate inline CSS in `index.html`. To customize:
1. Run the generator once
2. Edit the generated `index.html` (or modify the script templates)
3. For permanent changes, edit the HTML template in the generator script

---

## 🔄 Workflow for Adding New Dashboards

1. **Create your dashboard HTML file**
   - Use inline CSS and JavaScript
   - Use CDN links for external resources (Chart.js, fonts, etc.)

2. **Save to examples/ folder**
   ```bash
   mv your-new-dashboard.html examples/
   ```

3. **Add metadata** (if using Python version)
   ```bash
   nano www-vars.yaml
   ```

4. **Regenerate index**
   ```bash
   python3 generate-index.py
   # or
   ./generate-index.sh
   ```

5. **Commit and push** (if using Cloudflare Pages)
   ```bash
   git add .
   git commit -m "Add new dashboard"
   git push
   ```

6. **Auto-deploy happens** - your changes are live in ~30 seconds!

---

## 📋 Dashboard Development Guidelines

For best compatibility with static hosting:

✅ **Do:**
- Use inline CSS and JavaScript
- Use CDN links for libraries (Chart.js, fonts, etc.)
- Make dashboards self-contained
- Use relative paths for links between dashboards
- Test locally before pushing

❌ **Don't:**
- Avoid server-side code (PHP, Python Flask, etc.)
- Don't reference local files outside the repo
- Don't use database connections
- Avoid API keys in source code

---

## 🛠️ Troubleshooting

**Script says "No HTML files found"**
- Make sure files are in `examples/` folder (not root)
- Check file permissions

**Dashboard shows broken layout**
- Ensure all CDN resources are accessible
- Check browser console for errors
- Verify relative paths are correct

**Changes not showing on Cloudflare**
- Check build logs in Cloudflare dashboard
- Ensure build command succeeded
- Clear browser cache
- Wait ~1 minute for CDN propagation

---

## 📚 Examples

### Current Dashboards

1. **OS Patching Workflow** - Real-time task tracking
2. **Compliance Overview** - Security posture dashboard
3. **Server Details** - Per-server compliance breakdown
4. **Remediation Tracker** - Track fix progress
5. **Exception Management** - Handle compliance exceptions

All dashboards are production-ready and can be used as templates!

---

## 🔗 Useful Links

- **Cloudflare Pages Docs**: https://developers.cloudflare.com/pages
- **Chart.js Documentation**: https://www.chartjs.org/docs
- **Python YAML Module**: https://pyyaml.org/wiki/PyYAMLDocumentation

---

## 📝 License & Credits

Created by Gineesh Madapparambath  
Powered by Red Hat Ansible Automation Platform  
© 2024
