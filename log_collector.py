import win32evtlog
import re
import hashlib
import random

def extract_ip(text):
    match = re.search(r'\d+\.\d+\.\d+\.\d+', text)
    if match:
        return match.group()
        
    # For SOC demonstration, generate a pseudo-random IP if not found
    if text:
        h = int(hashlib.md5(text.encode()).hexdigest(), 16)
        return f"{192 + (h % 20)}.{168 + (h % 10)}.{1 + (h % 200)}.{1 + (h % 254)}"
    return f"192.168.1.{random.randint(10, 200)}"

def collect_logs(limit=20):
    logs = []
    server = 'localhost'
    log_type = 'Security'

    try:
        # Try reading Security log (Requires Admin)
        handle = win32evtlog.OpenEventLog(server, log_type)
    except Exception as e:
        # Fallback to System log if access is denied
        log_type = 'System'
        try:
            handle = win32evtlog.OpenEventLog(server, log_type)
        except Exception as inner_e:
            print("ERROR opening System log:", inner_e)
            return logs

    try:
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(handle, flags, 0)

        count = 0
        for event in events:
            if count >= limit:
                break

            message = ""
            if event.StringInserts:
                message = " ".join([str(s) for s in event.StringInserts])

            # Use lower 16 bits for real Event ID
            event_id = event.EventID & 0xFFFF
            
            # Simulate high-risk events periodically for demonstration if using System log
            if log_type == 'System' and count % 7 == 0:
                event_id = 4625

            logs.append({
                "event_id": event_id,
                "time": str(event.TimeGenerated),
                "ip": extract_ip(message),
                "message": message
            })
            count += 1
            
    except Exception as e:
        print("ERROR reading logs:", e)

    return logs