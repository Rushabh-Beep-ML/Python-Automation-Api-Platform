🐍 Python Automation & API Processing Platform










A modular backend application for automating text cleaning, transformation, parsing, and enrichment with external APIs, featuring a responsive UI and test coverage.
Designed with production-style service architecture, configuration management, and extensibility principles.

✨ Highlights

✔ Robust text cleaning pipeline
✔ Smart parsing with key:value detection
✔ External API enrichment service layer
✔ Simple UI for processing and inspecting results
✔ Structured JSON output format
✔ Environment-based configuration system
✔ Pytest-backed test suite

🏗️ Architecture Overview

The application follows a clean, layered architecture:

python-automation-tool/
│
├── app/
│   ├── routes/          # Web + API endpoints
│   ├── services/        # Processing + enrichment logic
│   ├── utils/           # Helper utilities
│   ├── templates/       # UI templates (HTML)
│   └── static/          # JS and CSS assets
│
├── tests/               # Unit tests for services/helpers
├── config.py            # Application configuration loader
├── run.py               # Entry point
├── requirements.txt     # Dependencies
├── .env.example         # Configuration template
└── README.md


This structure allows:

✔ separation of concerns
✔ testability
✔ clear extensibility points

🚀 Getting Started
📌 Prerequisites

Python 3.8+

Pip

Virtual environment (recommended)

🔹 Clone the repository
git clone https://github.com/<your-username>/python-automation-api-platform.git
cd python-automation-api-platform

🔹 Setup a virtual environment
python -m venv venv


Activate:

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

🔹 Install dependencies
pip install -r requirements.txt

🔹 Configure environment
cp .env.example .env


Edit .env values:

SECRET_KEY=your-secret
EXTERNAL_API_BASE_URL=https://jsonplaceholder.typicode.com
API_TIMEOUT=10
DEBUG=True

🔹 Run the application
python run.py


➡ Visit: http://localhost:5000

📡 API Reference
🔸 POST /api/process

Request body:

{
  "raw_input": "Line 1\nLine 2",
  "operations": [
    "clean_whitespace",
    "normalize_case",
    "remove_duplicates",
    "external_api_enrich"
  ]
}


Response:

{
  "success": true,
  "processed_items": [...],
  "summary": {
    "total_items": 2,
    "operations_applied": 4
  }
}

🧪 Running Tests
pytest -v
pytest --cov=app tests/

🧩 Supported Operations
Operation	Description
clean_whitespace	Removes extra spaces & empty lines
normalize_case	Converts text format (lower, upper, title, sentence)
remove_duplicates	Eliminates duplicate lines
external_api_enrich	Enriches each item using configured API
🛠️ Tech Stack

🔹 Flask — lightweight web framework
🔹 Python Requests — API communication
🔹 Jinja2 — templates
🔹 Pytest — testing
🔹 Dotenv — config management

📌 Future Enhancements

⬜ CSV file upload support
⬜ Dashboard + authentication
⬜ Scheduled batch processing
⬜ Database storage of results
⬜ Swagger / OpenAPI documentation
⬜ Cloud deploy with Docker + Render / Railway

👨‍💻 Author

Rushabh Ahire
Backend Developer — Python | APIs | Automation

💼 GitHub:@Rushabh-beep 
          @Rushabh-Beep-ML
🔗 https://www.linkedin.com/in/rushabh-ahire-31131a345?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
