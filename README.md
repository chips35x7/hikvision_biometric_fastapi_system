Hikvision Biometric Integration (FastAPI)

This project is a proof-of-concept for integrating with *Hikvision (model: DS-K1T804AMF) biometric devices* using *FastAPI* and Python. It includes testing scripts for sending XML-based subscriptions to the ISAPI endpoints and handling device event notifications for intergration
into custom backend systems such as employee attendance tracking, Access Control panels, School or University Check-In, or Visitor Management.

---

📁 Project Structure

```
hikvision_biometric_fastapi_system/
├── app.py                      # Main FastAPI application
├── subscription_test_script.py # Script for sending subscription to device
├── fingerprint_logs.json       # Placeholder for storing incoming logs/events
├── subscription.xml            # XML payload for ISAPI subscription
├── response.xml                # Sample response from the device
├── .env                        # Credentials for ISAPI access (excluded from Git)
├── requirements.txt            # Python dependencies
└── README.md                   # Project description
```

---

⚙️ Setup Instructions

1. *Clone the repository*
   ```bash
   git clone chips35x7
   cd hikvision_biometric_fastapi_system
   ```

2. *Create virtual environment (optional but recommended)*
   ```bash
   python -m venv .venv
.venv\Scripts\activate on Windows PCs
   ```

3. *Install dependencies*
   ```bash
   pip install -r requirements.txt
   ```

4. *Create `.env` file*
   ```
   USERNAME=admin
   PASSWORD=your_device_password
   ```

---

🚀 Running the Test Script

Use the test script to send a subscription to your Hikvision device:

```bash
python subscription_test_script.py
```

Make sure the device IP, network gateway, port, and credentials in the `.env` file match your actual setup.

---

🔒 Notes

- This is a test/prototype project and *not production-ready*.
- Make sure your device supports ISAPI and XML-based subscriptions.
- `.env`, `.venv/`, and `_pycache_/` are excluded from version control.

---

📌 Status

Prototype phase incomplete and still in development. 
Reference version archived: `biometric-php-python-prototype-archived/`

---

📞 Contact

Developed by: Nigel Chiputura  
Location: Marondera, Zimbabwe  
Portfolio: www.nigelchiputura.dev