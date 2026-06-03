# 🔐 Real-Time Security Log Analysis and Automated Threat Mitigation System

## 📖 Overview

The **Real-Time Security Log Analysis and Automated Threat Mitigation System** is a Security Operations Center (SOC)-inspired cybersecurity solution that continuously monitors Windows event logs, detects malicious activities, assesses security risks, and automatically initiates response actions.

The system provides a modern **Zero Trust SOC Dashboard** for real-time visibility into security events, enabling security analysts to identify threats, monitor attack patterns, and respond to incidents efficiently.

---

## 🎯 Objectives

- Monitor security logs in real time.
- Detect suspicious and malicious activities.
- Perform threat classification and risk assessment.
- Automate incident response actions.
- Provide centralized security monitoring through an interactive dashboard.
- Improve SOC efficiency and reduce response time.

---

## 🚀 Key Features

### 📊 Real-Time Log Monitoring
- Collects Windows Security and System Event Logs.
- Extracts Event IDs, timestamps, messages, and source IP addresses.
- Supports continuous log polling for live monitoring.

### 🛡️ Threat Detection Engine

The system identifies various security events such as:

- Brute Force Login Attempts
- Failed Authentication Events
- Privilege Escalation Attempts
- Group Membership Modifications
- Account Creation and Modification Activities
- Explicit Credential Logons
- Unusual User Activities

### ⚠️ Security Risk Analysis

Events are categorized into:

| Severity | Description |
|-----------|------------|
| Low | Normal system activities |
| Medium | Potentially suspicious activities |
| High | Critical security threats requiring immediate action |

### 🤖 Automated Incident Response

When high-risk activity is detected:

- Security alerts are generated.
- Malicious IP addresses are automatically blocked.
- Firewall rules are dynamically created.
- Threat sources are added to a blacklist.
- Administrator notifications are logged.

### 📈 Interactive SOC Dashboard

The dashboard provides:

- Real-time threat monitoring
- Security metrics visualization
- Risk distribution charts
- Attack origin visualization
- Firewall management
- System log inspection
- Security policy configuration

---

## 🏗️ System Architecture

```text
Windows Event Logs
        │
        ▼
 Log Collection Module
        │
        ▼
 Threat Detection Engine
        │
        ▼
 Risk Classification
        │
        ▼
 Automated Response Engine
        │
        ▼
 SOC Dashboard & Reporting
```

---

## 🖥️ Dashboard Modules

### 🔹 Live Dashboard
- Total Threat Count
- High-Risk Alerts
- Top Threat Source IP
- Real-Time Event Stream

### 🔹 Threat Intelligence
- Security monitoring status
- Threat feed visualization
- IOC monitoring support

### 🔹 Firewall Rules
- Displays automatically blocked IP addresses
- Tracks active isolation actions

### 🔹 System Logs
- Raw telemetry inspection
- Event log dump viewer

### 🔹 Settings Panel

Configurable security controls:

- Auto Firewall Blocking
- Alert Logging
- Strict Mode Enforcement

---

## 🔍 Threat Detection Rules

| Event ID | Threat Type | Severity |
|-----------|------------|-----------|
| 4625 | Failed Login Attempt (Brute Force) | High |
| 4728 | Privilege Escalation | High |
| 4732 | Group Membership Modification | High |
| 4756 | Group Membership Modification | High |
| 4720 | Account Creation | Medium |
| 4722 | Account Enabled | Medium |
| 4724 | Password Reset | Medium |
| 4648 | Explicit Credential Logon | Medium |
| 4624 | Successful Login | Low |
| 4634 | Successful Logoff | Low |

---

## 🛠️ Technology Stack

### Backend
- Python
- Flask
- Windows Event Log API (`win32evtlog`)
- Logging Module
- Windows Firewall (`netsh`)

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js

### Security Components
- Rule-Based Threat Detection
- Risk Scoring Engine
- Automated Response Module
- Firewall Integration

---

## 📂 Project Structure

```text
├── app.py
├── detector.py
├── log_collector.py
├── responder.py
├── utils.py
├── requirements.txt
│
├── templates
│   └── index.html
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/security-log-analysis.git
cd security-log-analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Access the Dashboard

```text
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### Retrieve Processed Logs

```http
GET /logs
```

### Retrieve Raw Logs

```http
GET /api/raw_logs
```

### Retrieve Blocked IPs

```http
GET /api/firewall
```

### Manage System Settings

```http
GET /api/settings
POST /api/settings
```

---

## 🔐 Security Workflow

1. Collect logs from Windows Event Viewer.
2. Extract Event IDs and IP addresses.
3. Classify events using predefined threat rules.
4. Assign risk severity levels.
5. Generate alerts for high-risk events.
6. Automatically block malicious IP addresses.
7. Display results on the SOC dashboard.
8. Maintain firewall blocklist and incident history.

---

## 🔮 Future Enhancements

- Machine Learning-Based Anomaly Detection
- SIEM Integration (Splunk, ELK)
- Email and SMS Notifications
- Threat Intelligence Feed Integration
- Geo-IP Attack Mapping
- Real-Time Malware Detection
- Advanced Risk Scoring Algorithms
- User Behavior Analytics (UBA)
