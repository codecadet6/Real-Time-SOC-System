from flask import Flask, jsonify, render_template, request
from log_collector import collect_logs
from detector import classify_log
from responder import block_ip, alert_admin
from collections import Counter

app = Flask(__name__)

BLOCKED_IPS = set()

SYSTEM_SETTINGS = {
    "auto_block": True,
    "log_alerts": True,
    "strict_mode": False
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logs")
def logs():
    raw_logs = collect_logs()

    ip_list = [log["ip"] for log in raw_logs]
    ip_count = Counter(ip_list)

    processed = []

    for log in raw_logs:
        result = classify_log(log)

        ip = log["ip"]
        count = ip_count[ip]

        # Apply Settings
        strike_limit = 3 if SYSTEM_SETTINGS["strict_mode"] else 5

        # Blacklist logic
        if count >= strike_limit or result["severity"] == "High":
            status = "BLACKLISTED"
            # Automated Response
            if ip not in BLOCKED_IPS and ip not in ["N/A", "Unknown", "127.0.0.1", "::1"]:
                if SYSTEM_SETTINGS["log_alerts"]:
                    alert_admin(f"High risk activity detected from {ip}. Initiating Block.")
                if SYSTEM_SETTINGS["auto_block"]:
                    block_ip(ip)
                BLOCKED_IPS.add(ip) # Add to prevent repeated block attempts
        elif count >= 3:
            status = "Suspicious"
        else:
            status = "Normal"

        processed.append({
            "ip": ip,
            "time": log["time"],
            "severity": result["severity"],
            "threat": result["threat"],
            "action": result["action"],
            "status": status
        })

    return jsonify(processed)

@app.route("/api/firewall")
def firewall():
    return jsonify(list(BLOCKED_IPS))

@app.route("/api/settings", methods=["GET", "POST"])
def manage_settings():
    global SYSTEM_SETTINGS
    if request.method == "POST":
        new_settings = request.json
        if new_settings:
            SYSTEM_SETTINGS.update(new_settings)
            return jsonify({"status": "updated", "settings": SYSTEM_SETTINGS})
    return jsonify(SYSTEM_SETTINGS)

@app.route("/api/raw_logs")
def raw_logs():
    return jsonify(collect_logs())

if __name__ == "__main__":
    app.run(debug=True)
