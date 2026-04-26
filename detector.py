def classify_log(log):
    event_id = log.get("event_id")
    
    # High Risk Events
    if event_id == 4625:
        return {
            "severity": "High",
            "threat": "Failed Login Attempt (Brute Force)",
            "action": "Investigate / Block IP"
        }
    elif event_id in [4728, 4732, 4756]:
        return {
            "severity": "High",
            "threat": "Privilege Escalation (Group Modification)",
            "action": "Investigate Admin Actions"
        }
        
    # Medium Risk Events
    elif event_id in [4720, 4722, 4724]:
        return {
            "severity": "Medium",
            "threat": f"Account Modification (Event {event_id})",
            "action": "Review User Activity"
        }
    elif event_id == 4648:
        return {
            "severity": "Medium",
            "threat": "Explicit Credential Logon",
            "action": "Monitor"
        }

    # Low Risk Events
    elif event_id == 4624:
        return {
            "severity": "Low",
            "threat": "Successful Login",
            "action": "Normal Activity"
        }
    elif event_id == 4634:
        return {
            "severity": "Low",
            "threat": "Successful Logoff",
            "action": "Normal Activity"
        }

    # Default
    else:
        return {
            "severity": "Medium",
            "threat": f"Unclassified Event ID {event_id}",
            "action": "Monitor"
        }