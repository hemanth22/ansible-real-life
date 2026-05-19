# OpenSCAP Security Compliance Dashboard Suite

Professional enterprise-grade dashboards demonstrating Ansible's capability to create comprehensive security compliance reporting and tracking systems.

## Overview

This dashboard suite showcases a complete OpenSCAP security compliance management workflow, from initial scanning through remediation and exception tracking. Built for the **iamgini.compliance** Ansible collection, these dashboards demonstrate real-world security automation capabilities.

## Dashboard Components

### 1. Main Dashboard (`compliance-main-dashboard.html`)

**Primary compliance overview with enterprise KPIs**

- **Key Features:**
  - Real-time compliance status across entire infrastructure
  - KPI cards: Total Servers, Compliant/Non-Compliant counts, Average Score, Active Findings
  - Visual charts: Compliance distribution, Severity breakdown, 30-day trends, Top failing rules
  - Server inventory table with compliance scores and scan status
  - Quick navigation to detailed views

- **Use Case:** Executive and security team overview of organizational compliance posture

### 2. Server Details Dashboard (`compliance-server-details.html`)

**Detailed compliance analysis for individual servers**

- **Key Features:**
  - Complete server profile (OS, IP, role, scan metadata)
  - Individual compliance score with pass/fail breakdown
  - Detailed rule-by-rule evaluation results
  - Severity classification (Critical, High, Medium, Low)
  - Direct links to remediation playbooks
  - Exception status visibility
  - Downloadable reports (HTML, ARF/XML)

- **Use Case:** System administrators investigating specific server compliance issues

### 3. Remediation Tracker (`compliance-remediation-tracker.html`)

**Workflow automation and remediation lifecycle management**

- **Key Features:**
  - 6-phase workflow visualization (Scan → Parse → Generate → Approve → Remediate → Rescan)
  - Visual workflow status with completed/active/pending phases
  - Approval gate management
  - Remediation playbook status tracking
  - Activity timeline and audit trail
  - Links to Ansible Automation Platform job executions
  - Success/failure tracking with error logs

- **Use Case:** DevSecOps teams managing compliance remediation pipelines

### 4. Exception Management Dashboard (`compliance-exceptions.html`)

**Compliance exception tracking and governance**

- **Key Features:**
  - Active exception inventory with business justifications
  - Group-level vs host-specific exception differentiation
  - Compensating controls documentation
  - Approval workflow tracking (approver, date, ticket reference)
  - Review cycle management with expiration alerts
  - Exception scope visualization (which servers are affected)
  - Audit-ready documentation

- **Use Case:** Security governance teams managing risk acceptance and compensating controls

## Design Principles

### Professional Enterprise Aesthetics
- Clean, modern UI using Inter font family
- Professional color palette (blues, greens, yellows, reds for status)
- Consistent spacing and typography
- Subtle shadows and hover effects
- Responsive grid layouts

### No Emoji Policy (Icon Exception)
- Unicode symbols used as professional icons (✓, ✗, ⚠, etc.)
- No decorative emojis in body text
- Maintains corporate professionalism

### Data Visualization
- Chart.js integration for interactive charts
- Doughnut charts for distribution
- Bar charts for severity and rule analysis
- Line charts for trend analysis
- Progress bars for workflow tracking

### Accessibility & Usability
- High contrast ratios for readability
- Semantic HTML structure
- Keyboard-navigable interfaces
- Mobile-responsive design
- Clear visual hierarchy

## Technical Architecture

### Frontend Stack
- **HTML5** - Semantic markup
- **CSS3** - Modern flexbox/grid layouts, custom properties
- **JavaScript** - Chart.js for data visualization
- **Google Fonts** - Inter font family

### Data Integration Points (Future Jinja2 Templates)
These static demos are designed for conversion to Jinja2 templates with:

```jinja2
<!-- Example variables for templating -->
{{ total_servers }}
{{ compliant_servers }}
{{ average_compliance_score }}
{{ server.hostname }}
{{ server.compliance_score }}
{{ rule.severity }}
{{ exception.business_justification }}
{{ remediation.status }}
```

### Ansible Integration Touchpoints

1. **Data Collection:**
   - OpenSCAP scan results (ARF/XML)
   - Parsed compliance data
   - Server inventory facts
   - Exception registry JSON

2. **Workflow Triggers:**
   - Links to AAP job templates
   - Remediation playbook execution
   - Rescan triggers
   - Approval workflows

3. **Reporting:**
   - HTML report generation
   - ARF/XML export
   - Audit trail logging

## Workflow Integration with Ansible Automation Platform

### Phase 1: SCAN
```yaml
- Job Template: "compliance-scan"
  Playbook: playbooks/scan.yml
  Purpose: Run OpenSCAP scans on target servers
  Output: ARF XML results pushed to report server
```

### Phase 2: PARSE & GENERATE
```yaml
- Job Template: "compliance-parse"
  Playbook: playbooks/parse_failures.yml
  Purpose: Extract failed rules from ARF results

- Job Template: "compliance-generate"
  Playbook: playbooks/generate_remediation.yml
  Purpose: Generate Ansible remediation playbooks
```

### Phase 3: APPROVAL (Manual Gate)
- Human review of generated remediation playbooks
- Risk assessment and change approval
- Dashboard provides approval interface

### Phase 4: REMEDIATE
```yaml
- Job Template: "compliance-remediate"
  Playbook: playbooks/remediate.yml
  Purpose: Apply fixes to non-compliant servers
  Approval: Required
```

### Phase 5: RESCAN
```yaml
- Job Template: "compliance-rescan"
  Playbook: playbooks/rescan.yml
  Purpose: Validate remediation success
```

## Use Case Demonstrations

### Security Compliance Audit
1. Security auditor opens **Main Dashboard**
2. Reviews overall compliance posture (87.2% average)
3. Identifies 4 non-compliant servers
4. Drills into **Server Details** for specific failures
5. Documents findings for audit report

### Remediation Campaign
1. DevOps engineer opens **Remediation Tracker**
2. Reviews 12 pending remediation playbooks
3. Approves low-risk changes for staging environment
4. Monitors execution progress
5. Validates with rescan

### Exception Management
1. Security manager opens **Exception Management**
2. Reviews 3 expiring exceptions
3. Evaluates compensating controls
4. Extends approval or initiates remediation
5. Documents decision in ticket system

### Compliance Trend Analysis
1. CISO reviews **Main Dashboard** monthly
2. Analyzes 30-day compliance trend (81.5% → 87.2%)
3. Identifies top non-compliant rules
4. Prioritizes remediation efforts
5. Reports progress to executive team

## Future Enhancements (Jinja2 Conversion)

### Dynamic Data Binding
```jinja2
{% for server in compliance_results %}
  <tr>
    <td>{{ server.hostname }}</td>
    <td>{{ server.compliance_score }}%</td>
    <td>
      <span class="status-{{ server.status_class }}">
        {{ server.status_label }}
      </span>
    </td>
  </tr>
{% endfor %}
```

### Real-Time Updates
- Auto-refresh capability
- WebSocket integration for live status
- Progressive updates during scan execution

### Filtering & Search
- Server name search
- Severity filtering
- Date range selection
- Group/environment filtering

### Export Capabilities
- PDF report generation
- CSV data export
- JSON API endpoints
- Email report scheduling

## Dashboard Metrics Explained

### Compliance Score Calculation
```
Compliance Score = (Passed Rules / Total Rules Evaluated) × 100
```

### Status Classification
- **Compliant:** ≥ 95% compliance score
- **Partially Compliant:** 70-94% compliance score
- **Non-Compliant:** < 70% compliance score

### Severity Levels
- **Critical:** Immediate security risk, exploitation likely
- **High:** Significant risk, should remediate urgently
- **Medium:** Moderate risk, plan remediation
- **Low:** Minor risk, remediate when convenient
- **Info:** Informational finding, no action required

## File Structure

```
ansible-dashboard-reporting/
├── compliance-main-dashboard.html          # Main overview dashboard
├── compliance-server-details.html          # Individual server details
├── compliance-remediation-tracker.html     # Remediation workflow
├── compliance-exceptions.html              # Exception management
├── demo-dashboard.html                     # Original OS patching demo
└── COMPLIANCE-DASHBOARDS-README.md         # This file
```

## Viewing the Dashboards

### Local Development
```bash
# Open in browser directly
firefox compliance-main-dashboard.html

# Or serve via Python HTTP server
cd /home/gmadappa/ansible/ansible-real-life/ansible-dashboard-reporting
python3 -m http.server 8080

# Access at http://localhost:8080/compliance-main-dashboard.html
```

### Production Deployment
For production use, these would be:
1. Converted to Jinja2 templates
2. Populated with real OpenSCAP data
3. Served via nginx on report server
4. Protected with authentication
5. Integrated with AAP workflow templates

## Related Ansible Collection

These dashboards are designed for the **iamgini.compliance** collection:
- Repository: `/home/gmadappa/ansible/ansible-collection-compliance`
- Collection: `iamgini.compliance`
- Purpose: Automated security compliance scanning and remediation
- Supported Profiles: CIS, STIG, PCI-DSS, HIPAA, custom profiles

## Demo Data

All data shown in these dashboards is sample/dummy data for demonstration purposes:
- 47 total servers (mixture of prod, staging, dev)
- Compliance scores ranging from 68% to 98%
- Various severity levels and rule failures
- Realistic exception scenarios
- Sample workflow states

## Next Steps for Production

1. **Template Conversion:**
   - Convert HTML to Jinja2 templates
   - Add variable placeholders
   - Implement loops and conditionals

2. **Data Integration:**
   - Parse OpenSCAP ARF XML results
   - Extract compliance metrics
   - Build JSON data structures

3. **Ansible Playbook Creation:**
   - Generate dashboard HTML from templates
   - Push to report server
   - Schedule regular updates

4. **AAP Integration:**
   - Create workflow templates
   - Add approval nodes
   - Link to job executions

5. **Security Hardening:**
   - Add authentication
   - Implement SSL/TLS
   - Audit logging
   - Data encryption

## Conclusion

These dashboards demonstrate Ansible's capability to create sophisticated, enterprise-grade compliance management systems. The professional design, comprehensive workflow tracking, and detailed reporting make this an excellent showcase for automated security compliance management.

The clean, modern interface rivals commercial compliance tools while being fully integrated with the Ansible ecosystem and customizable to any organization's specific requirements.

---

**Created:** 2026-05-19  
**Collection:** iamgini.compliance v1.0.0  
**Purpose:** OpenSCAP Security Compliance Demo  
**Status:** Static Demo (Ready for Jinja2 Conversion)
