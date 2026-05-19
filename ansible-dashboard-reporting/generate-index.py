#!/usr/bin/env python3
"""
Generate index.html from dashboard files in examples/ folder
Reads metadata from www-vars.yaml
"""

import os
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Configuration
EXAMPLES_DIR = "examples"
WWW_VARS_FILE = "www-vars.yaml"
OUTPUT_FILE = "index.html"

def load_metadata():
    """Load dashboard metadata from www-vars.yaml"""
    if not os.path.exists(WWW_VARS_FILE):
        print(f"❌ Error: {WWW_VARS_FILE} not found!")
        return None

    with open(WWW_VARS_FILE, 'r') as f:
        return yaml.safe_load(f)

def get_dashboard_files():
    """Get all HTML files from examples/ directory"""
    examples_path = Path(EXAMPLES_DIR)
    if not examples_path.exists():
        print(f"⚠️  Warning: {EXAMPLES_DIR}/ directory not found. Creating it...")
        examples_path.mkdir(exist_ok=True)
        return []

    return sorted([f.name for f in examples_path.glob("*.html")])

def group_dashboards_by_category(metadata, files):
    """Group dashboards by category"""
    grouped = defaultdict(list)
    dashboards = metadata.get('dashboards', {})

    for filename in files:
        if filename in dashboards:
            info = dashboards[filename]
            category = info.get('category', 'Uncategorized')
            grouped[category].append({
                'filename': filename,
                'title': info.get('title', filename),
                'description': info.get('description', 'No description available')
            })
        else:
            # File exists but not in metadata
            grouped['Uncategorized'].append({
                'filename': filename,
                'title': filename.replace('.html', '').replace('-', ' ').title(),
                'description': 'No description available'
            })

    return dict(grouped)

def generate_html(metadata, grouped_dashboards):
    """Generate the index.html content"""
    site = metadata.get('site', {})
    title = site.get('title', 'Dashboard Gallery')
    subtitle = site.get('subtitle', '')
    author = site.get('author', '')
    github_repo = site.get('github_repo', '#')
    year = site.get('year', datetime.now().year)

    total_dashboards = sum(len(dashboards) for dashboards in grouped_dashboards.values())

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Red Hat Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #2d3748;
            line-height: 1.6;
            min-height: 100vh;
        }}

        .hero {{
            background: rgba(0, 0, 0, 0.3);
            color: white;
            padding: 60px 20px;
            text-align: center;
            backdrop-filter: blur(10px);
        }}

        .hero h1 {{
            font-size: 3em;
            font-weight: 800;
            margin-bottom: 10px;
            letter-spacing: -1px;
        }}

        .hero p {{
            font-size: 1.2em;
            opacity: 0.95;
            max-width: 700px;
            margin: 0 auto 20px;
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 30px;
            flex-wrap: wrap;
        }}

        .stat-item {{
            text-align: center;
        }}

        .stat-number {{
            font-size: 2.5em;
            font-weight: 700;
            display: block;
        }}

        .stat-label {{
            font-size: 0.9em;
            opacity: 0.9;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
        }}

        .category-section {{
            background: white;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .category-title {{
            font-size: 1.8em;
            font-weight: 700;
            color: #1e3a8a;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #3b82f6;
        }}

        .dashboard-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
            margin-top: 20px;
        }}

        .dashboard-card {{
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            padding: 25px;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }}

        .dashboard-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.3s ease;
        }}

        .dashboard-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            border-color: #3b82f6;
        }}

        .dashboard-card:hover::before {{
            transform: scaleX(1);
        }}

        .dashboard-title {{
            font-size: 1.3em;
            font-weight: 600;
            color: #1e3a8a;
            margin-bottom: 10px;
        }}

        .dashboard-description {{
            font-size: 0.95em;
            color: #64748b;
            line-height: 1.5;
            margin-bottom: 15px;
        }}

        .dashboard-link {{
            display: inline-block;
            color: #3b82f6;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9em;
            transition: all 0.2s;
        }}

        .dashboard-link:hover {{
            color: #1e3a8a;
            text-decoration: underline;
        }}

        .dashboard-link::after {{
            content: ' →';
            transition: transform 0.2s;
            display: inline-block;
        }}

        .dashboard-card:hover .dashboard-link::after {{
            transform: translateX(5px);
        }}

        footer {{
            background: rgba(0, 0, 0, 0.8);
            color: white;
            text-align: center;
            padding: 30px 20px;
            margin-top: 50px;
        }}

        footer p {{
            margin: 8px 0;
            opacity: 0.9;
        }}

        footer a {{
            color: #60a5fa;
            text-decoration: none;
        }}

        footer a:hover {{
            text-decoration: underline;
        }}

        .github-link {{
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background: #3b82f6;
            color: white;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.2s;
        }}

        .github-link:hover {{
            background: #1e3a8a;
            transform: scale(1.05);
        }}

        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2em;
            }}

            .dashboard-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="hero">
        <h1>🚀 {title}</h1>
        <p>{subtitle}</p>
        <div class="stats">
            <div class="stat-item">
                <span class="stat-number">{total_dashboards}</span>
                <span class="stat-label">Dashboards</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">{len(grouped_dashboards)}</span>
                <span class="stat-label">Categories</span>
            </div>
        </div>
    </div>

    <div class="container">
'''

    # Generate category sections
    for category, dashboards in sorted(grouped_dashboards.items()):
        html += f'''
        <div class="category-section">
            <h2 class="category-title">{category}</h2>
            <div class="dashboard-grid">
'''
        for dashboard in dashboards:
            html += f'''
                <div class="dashboard-card" onclick="window.location.href='{EXAMPLES_DIR}/{dashboard["filename"]}'">
                    <h3 class="dashboard-title">{dashboard["title"]}</h3>
                    <p class="dashboard-description">{dashboard["description"]}</p>
                    <a href="{EXAMPLES_DIR}/{dashboard["filename"]}" class="dashboard-link">View Dashboard</a>
                </div>
'''
        html += '''
            </div>
        </div>
'''

    # Footer
    html += f'''
    </div>

    <footer>
        <p><strong>Generated by Ansible Dashboard Gallery</strong></p>
        <p>Created by {author}</p>
        <p>Powered by Red Hat Ansible Automation Platform</p>
        <a href="{github_repo}" class="github-link" target="_blank">View on GitHub</a>
        <p style="margin-top: 20px; font-size: 0.85em; opacity: 0.7;">
            © {year} | Last generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}
        </p>
    </footer>
</body>
</html>
'''
    return html

def main():
    print("🔨 Generating index.html...")

    # Load metadata
    metadata = load_metadata()
    if not metadata:
        return

    # Get dashboard files
    files = get_dashboard_files()
    if not files:
        print(f"⚠️  No HTML files found in {EXAMPLES_DIR}/")
        print("💡 Move your dashboard HTML files to the examples/ folder first")
        return

    print(f"✅ Found {len(files)} dashboard(s)")

    # Group by category
    grouped = group_dashboards_by_category(metadata, files)

    # Generate HTML
    html_content = generate_html(metadata, grouped)

    # Write to file
    with open(OUTPUT_FILE, 'w') as f:
        f.write(html_content)

    print(f"✅ Successfully generated {OUTPUT_FILE}")
    print(f"📊 Total: {sum(len(d) for d in grouped.values())} dashboards in {len(grouped)} categories")
    print("\n📂 Categories:")
    for category, dashboards in grouped.items():
        print(f"   - {category}: {len(dashboards)} dashboard(s)")

if __name__ == "__main__":
    main()
