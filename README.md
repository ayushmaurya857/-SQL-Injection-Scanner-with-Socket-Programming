SQL Injection Scanner with Socket Programming

A client–server tool (Python) that accepts web page URLs from clients, parses forms on those pages, crafts automated test inputs, and checks for possible SQL injection weaknesses. Built as a learning / defensive-assessment project to demonstrate secure networking, automated scanning techniques, and distributed tool design — only for authorized, legal testing.

⚠️ Important — Read before using
This project is intended for defensive use, learning, and authorized security testing only. Do not scan, probe, or attack systems you do not own or do not have explicit written permission to test. Misuse may be illegal and unethical. Use this tool only on your own applications, lab targets (e.g., OWASP Juice Shop, DVWA), or systems where you have written authorization.

🚩 Key Features (High-level, non-exploitable)

Client–server architecture using Python sockets and threading for concurrent clients.

Server accepts URL submissions from clients, fetches the target page, and extracts <form> elements.

Automated generation of test inputs for form fields and submission of requests (using requests) to observe responses.

HTML parsing and form extraction using BeautifulSoup.

Scalable basic design that demonstrates networking + security testing workflows suitable for defensive learning and automation research.

Implementation intentionally avoids embedding or exposing exploit payload libraries in this README. The repository contains the scanner code; treat it as an educational tool and review any payload-generation logic carefully before use.

🧰 Toolstack

Language: Python 3.8+

Libraries: requests, beautifulsoup4, urllib.parse, socket, threading

Optional (dev/test): OWASP Juice Shop, Damn Vulnerable Web App (DVWA), or custom test apps.

🏗️ Architecture (Overview)

+-----------+        TCP sockets         +-----------+

|  Client   |  ------------------------> |  Server   |

| (submit   |<------------------------ | (fetches  |

|  URLs)    |----------responses -------|  pages,   |

+-----------+ ----------------------|  analyzes)|

                                   +-----------+

- Server spawns a thread per client connection.
- 
- Server uses HTTP requests to fetch pages and BeautifulSoup to parse forms.
- 
- Server returns scan summaries to the client (possible vulnerable fields, HTTP responses, notes).

📁 Project Structure

sql-injection-scanner/

├── server.py                # Server: accepts client connections and handles scanning tasks

├── client.py                # Client: connects to server, sends URLs to scan, receives summaries

├── requirements.txt         # Python dependencies

├── README.md

├── LICENSE

└── docs/

    └── safe-testing-guidelines.md

⚙️ Setup (local, safe lab)

1. Clone the repository:

git clone https://github.com/<your-username>/sql-injection-scanner.git

cd sql-injection-scanner

2. Create a virtual environment and install dependencies:

  python -m venv venv

  source venv/bin/activate     # macOS / Linux

  venv\Scripts\activate        # Windows

  pip install -r requirements.txt

🧪 Testing & Demo

<img width="1365" height="716" alt="Screenshot 2025-09-12 182903" src="https://github.com/user-attachments/assets/f1a72dce-1646-42a5-875e-4e22ce525498" />

🔒 Responsible Use & Guidance

Authorized testing only. Obtain written permission before testing any third-party systems. Maintain a scope document listing hosts and targets you are allowed to test.

Limit impact. Configure the server to run in low-rate mode and avoid destructive payloads. Use a staging/test environment for all experiments.

Logging & audit. Keep logs of scans, timestamps, and consent documents. Share findings responsibly via secure channels (e.g., an issue tracker with limited access).

Safe Targets: The project recommends using well-known intentionally vulnerable targets (OWASP Juice Shop, DVWA) or your own sandboxed application.

3. Recommended: spin up a deliberately vulnerable web app to practice against:

  OWASP Juice Shop (node-based)

  Damn Vulnerable Web App (DVWA)

  Custom intentionally vulnerable test pages

▶️ How to Run (educational/demo)

These commands show the networking flow (server/client). They do not provide exploit payloads.

Start the server (from repo root):

  python server.py

The server listens for client connections and processes scanning requests in separate threads.

Start a client in another terminal and submit a target (use only authorized targets):

  python client.py

Follow the client prompt to enter a URL (e.g., http://localhost:3000/login) — only use test/lab targets.

Server performs safe automated checks (form extraction, benign input testing, response observation) and returns a summary to the client. The summary indicates observations such as form fields found, unusual database-error-like responses, HTTP status codes, and recommended next steps for an authorized security assessment.
