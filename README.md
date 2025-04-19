# WhatsApp Messaging Integration with FastAPI

> This project demonstrates sending WhatsApp messages using FastAPI and the 360dialog sandbox API, created as part of a technical assessment.

---

## 📝 Assessment Objective

The objective was to:
- Build a backend service using **FastAPI** that can send messages to WhatsApp numbers.
- Integrate it with **Meta's WhatsApp Business API** for real-time communication.
- Keep the solution lightweight and focused on prototype-ready functionality.

---

## ⚠️ Problems Faced

### 1. Meta Business API Setup Issues
- Meta’s WhatsApp Business API **requires business verification**, a registered business name, display name matching a verified business, and legal documents.
- **Billing setup was mandatory**, which made it hard to proceed for prototyping or personal testing purposes.

### 2. Limited Test Environment
- Meta allows sending messages only to **pre-approved test numbers**.
- Sandbox usage is extremely limited and not ideal for quick prototyping or multiple number testing.

### 3. Authorization & Permissions
- Attempting to message other numbers returned the error:
  ```
  {
    "detail": "{\"meta\": {\"success\": false, \"http_code\": 403, \"developer_message\": \"No permission for that number\"}}"
  }
  ```

## ✅ Workaround Used

I used the **360dialog Sandbox API**, which allows developers to send WhatsApp messages to their own number without requiring full Meta business account verification.

- How to generate the API_KEY for 360Dialog Sandbox
  [Visit the Official Documentation](https://docs.360dialog.com/partner/api-reference/sandbox)
  Send a message - `START` to their official WhatsApp Business Number - `+49 30 609859535`
  You get a response with the TEST_API_KEY with that you can message your number 
---

## 🧰 Technologies Used

- **FastAPI** – Backend framework
- **Python 3.11**
- **360dialog Sandbox API** – For sending WhatsApp messages
- **Dotenv** – For handling environment variables

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/20481A5450/TMBC_Python-Developer.git
cd TMBC_Python-Developer
```

### 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # on Linux/macOS
env\Scripts\activate     # on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Rename the `example.env` to `.env` file
```ini
# .env file
D360_API_KEY=your_360dialog_test_key
```

### 5. Start the FastAPI Server
```bash
uvicorn app.main:app --reload
```

---

## 📦 Example Endpoint

**Send Message API:**

```http
GET /send-message?phone_number=91XXXXXXXXXX
```

Query Parameter:
- `phone_number`: WhatsApp number in international format (e.g., 919876543210)

---

## 📌 Notes

- The 360dialog sandbox only allows sending messages to your **registered number**.
- For other functonalities should use, a proper **Meta Business Account** and **approved number** are required.

---
