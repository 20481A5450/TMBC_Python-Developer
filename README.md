Here’s your complete **README.md** content in code block format, suitable for a professional repository:

# WhatsApp Messaging Integration with FastAPI

> This project demonstrates sending WhatsApp messages using FastAPI and the 360dialog sandbox API, created as part of a technical assessment.

---

## 📝 Assessment Objective

The objective was to:
- Build a backend service using **FastAPI** that can send messages to WhatsApp numbers.
- Integrate it with **Meta's WhatsApp Business API** (or suitable alternative) for real-time communication.
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

We used the **360dialog Sandbox API**, which allows developers to send WhatsApp messages to their own number without requiring full Meta business account verification.

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
git clone https://github.com/your-username/whatsapp-fastapi-integration.git
cd whatsapp-fastapi-integration
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

### 4. Create a `.env` file
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
- For production use, a proper **Meta Business Account** and **approved number** are required.

---

## 🧪 Future Enhancements

- Add webhook support for receiving messages.
- Integrate real-time message status tracking.
- Replace sandbox with production Meta API once verification is complete.

---

## 🤝 Acknowledgements

Thanks to [360dialog](https://www.360dialog.com/) for providing an easier testing environment for WhatsApp API integration.

---

## 📄 License

This project is licensed under the MIT License.
```

Let me know if you want a `requirements.txt` file or folder structure to go along with this!
