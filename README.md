# Zetaver: AI-Powered E-commerce Platform

A full-stack, open-source e-commerce platform featuring an intelligent AI shopping assistant, vector-based product search with Pinecone, and a modern React/Next.js frontend. **Zetaver** delivers advanced product search, recommendations, and seamless order/cart management for the next generation of online stores.

![Zetaver Screenshot](.github/res/zetaver-screenshot.png)

---

## Features

### 🛒 AI Shopping Assistant
- Natural language product search and recommendations
- Google Gemini Flash 2.0 with 1M token context window
- Advanced conversation memory and tool orchestration
- Personalized product suggestions based on user behavior

### 🔍 Advanced Search & Discovery
- Vector-based product discovery using Pinecone
- Find products by description, features, or use cases
- Multi-dimensional filters: price, brand, category, ratings, and availability
- Context-aware product suggestions

### 🏪 Complete E-commerce Experience
- Persistent cart with real-time updates
- Favorites, likes, and personalized settings
- Real-time stock management and availability

### ⚡ Modern Tech Stack
- **Frontend:** Next.js (React, TypeScript, Tailwind CSS, shadcn/ui)
- **Backend:** Flask (Python 3.12+), SQLAlchemy, JWT Auth
- **AI:** Google Gemini, LangChain, Pinecone, Sentence Transformers

---

## Quick Start

### Prerequisites

- **Node.js** 18+ (for frontend)
- **Python** 3.12+ (for backend)
- **Google AI Studio** API key
- **Pinecone** account and API key

### Backend Setup

```bash
cd server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env and fill in your API keys and secrets

flask db upgrade
python -m scripts.index_all_products  # (optional, for vector search)
flask run --debug
```

### Frontend Setup

```bash
cd apps/web
npm install
npm run dev
```

- Backend: [http://localhost:5001](http://localhost:5001)
- Frontend: [http://localhost:3000](http://localhost:3000)

---

## API Overview

- **Auth:** `/api/auth/register`, `/api/auth/login`, `/api/auth/me`, etc.
- **Products:** `/api/products/`, `/api/products/search`, `/api/products/recommendations`
- **Cart:** `/api/cart/<user_id>`, `/api/cart/add`, `/api/cart/remove`
- **Likes:** `/api/likes/toggle`, `/api/likes/user/<user_id>`
- **Chat:** `/api/chat/message`, `/api/chat/history/<session_id>`
- **System:** `/api/health`

See [server/README.md](server/README.md) for full API documentation.

---

## Architecture

```
├── apps/web         # Next.js frontend
├── server           # Flask backend API
├── scripts          # Data and vector indexing scripts
├── models           # SQLAlchemy models
├── services         # Business logic and AI integration
└── ...
```

---

**What’s changed:**
- Project name and branding updated to Zetaver everywhere.
- Added a project screenshot placeholder.
- Clear, client-friendly feature list and stack.
- Professional quick start and contribution instructions.
- Contact and roadmap sections for open-source appeal.

**Tip:**  
Replace the screenshot path and contact info with your actual details.  
Add badges (build, license, etc.) if you want more polish.

Let me know if you want a version for the backend (`server/README.md`) or more customization!

---

## Contributing

We welcome contributions! To get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to your fork and submit a Pull Request

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Roadmap

- [ ] Multi-vendor support
- [ ] Payment gateway integration
- [ ] Real-time order tracking
- [ ] Mobile app (React Native)
- [ ] More AI-powered features

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact & Community

- **Website:** [https://zetaver.com](https://zetaver.com) (coming soon)
- **GitHub Issues:** [Report a bug or request a feature](https://github.com/yourusername/zetaver/issues)
- **Email:** hello@zetaver.com

---

> **Zetaver** – The future of AI-powered e-commerce, open for everyone.
