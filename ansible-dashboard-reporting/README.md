# Ansible Dashboard Reporting

Real-time visual status tracking for multi-step automation workflows with live HTML dashboards and Slack notifications.

## Overview

This project provides automated reporting and visualization for complex infrastructure workflows (patching, maintenance, deployments). It tracks task progress, generates auto-refreshing web dashboards, and sends real-time Slack notifications.

## Features

- **Live HTML Dashboard** - Auto-refreshing web page with color-coded task status
- **Slack Integration** - Real-time block-formatted notifications to Slack channels
- **Workflow State Management** - Track tasks through Todo → In Progress → Completed/Error/Fixed states
- **AAP Integration** - Links to Ansible Automation Platform job outputs
- **Error Handling** - Automatic error detection and recovery workflows

## Quick Start

```bash
# Set Slack bot token
export SLACK_BOT_TOKEN=<your-bot-token>

# Run basic reporting workflow
ansible-playbook reporting.yaml -e "send_slack=true"

# Run with AAP job integration
ansible-playbook reporting-jobs.yaml -e "status_data_task=01_backup_task"
```

## Components

- **Playbooks**: `reporting.yaml`, `reporting-jobs.yaml`, `reporting-fix.yaml`
- **Roles**: `prepare-report` (dashboard generation), `notify-slack` (Slack notifications)
- **Templates**: `patching-dashboard.html` (responsive dashboard with Chart.js)
- **Data**: `vars/sample-data.yaml` (18-task patching workflow example)

## Configuration

- **Dashboard Location**: `/var/www/html/dashboards/index.html` on `utils.lab.iamgini.com`
- **Slack Channel**: `#ansible` (configurable via `slack_channel` variable)
- **Refresh Rate**: 3 seconds (configurable via `html_refresh_rate`)
- **AAP Controller**: `https://aap.lab.iamgini.com`

## Example Workflow

Sample multi-tier application patching workflow:
1. Backup configuration → VMWare snapshot
2. Health checks → Remove from load balancer
3. Stop services → Patch servers (MQ/App/DB)
4. Start services → Verify health
5. Re-add to load balancer → Final validation

## Resources

- [Slack API Documentation](https://api.slack.com/)
- Slack Block Kit for message formatting