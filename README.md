# Document Processing API

A robust API built with modern technologies to process and extract text from document files. This application demonstrates advanced backend development skills, database integration, and cloud deployment capabilities.

## 🚀 What This App Does

Imagine you have a collection of PDF or Word documents, and you need to quickly extract all the text content from them programmatically. This API makes that process seamless:

- **Upload Documents**: Send PDF or DOCX files via a simple HTTP request
- **Automatic Text Extraction**: The API intelligently processes the files and pulls out all readable text
- **Database Storage**: Extracted content is securely stored in a PostgreSQL database for future retrieval
- **Fast Response**: Get back the processed document ID instantly for tracking

Perfect for applications like document management systems, content analysis tools, or automated data processing pipelines.

## ✨ Key Features

- **Multi-Format Support**: Handles both PDF and Microsoft Word documents
- **Asynchronous Processing**: Built with async/await for high performance
- **Database Persistence**: Uses Prisma ORM with PostgreSQL for reliable data storage
- **RESTful API**: Clean, well-documented endpoints following REST principles
- **Error Handling**: Comprehensive validation and error responses
- **Modular Architecture**: Clean, maintainable code structure
- **Production Ready**: Includes testing, CI/CD, and deployment configurations

## 🛠️ Technologies & Skills Demonstrated

### Backend Framework
- **FastAPI**: High-performance async web framework for Python
- **Uvicorn**: ASGI server for production deployment

### Database & ORM
- **PostgreSQL**: Robust relational database
- **Prisma**: Next-generation ORM with type safety and auto-generated clients

### Document Processing
- **PyMuPDF (Fitz)**: Advanced PDF text extraction
- **python-docx**: Microsoft Word document processing

### Development Tools
- **Pytest**: Comprehensive testing framework with async support
- **GitHub Actions**: Automated CI/CD pipelines
- **Vercel**: Serverless deployment platform

### Development Practices
- **Modular Architecture**: Clean separation of concerns
- **Type Safety**: Full type hints throughout the codebase\
- **Async Programming**: Modern Python async/await patterns
- **Environment Configuration**: Secure credential management

## 📋 Prerequisites

- Python 3.9+
- PostgreSQL database
- Node.js (for Prisma CLI)

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd document-processing-api
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**
   ```bash
   # Configure your DATABASE_URL in .env
   prisma generate
   prisma db push
   ```

4. **Run the application**
   ```bash
   uvicorn src.main:app --reload
   ```

5. **Test the API**
   ```bash
   curl -X POST "http://localhost:8000/process-document/" \
        -F "file=@your-document.pdf"
   ```

## 📖 API Documentation

### POST /process-document/

Upload a document file for processing.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (PDF or DOCX)

**Response:**
```json
{
  "id": "ckq1f8j9w0000abcdefghijk"
}
```

**Example Usage:**
```python
import requests

files = {'file': open('document.pdf', 'rb')}
response = requests.post('http://localhost:8000/process-document/', files=files)
print(response.json())
```

## 🏗️ Architecture Overview

```
src/
├── main.py              # FastAPI application & endpoints
├── database/
│   └── client.py        # Prisma database client
└── processing/
    ├── document_handler.py  # Main processing logic
    ├── pdf_processor.py     # PDF text extraction
    └── word_processor.py    # Word document processing
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
pytest
```

Tests cover:
- Document processing functions
- File type validation
- Error handling scenarios

## 🚀 Deployment

### Vercel (Recommended)

1. Connect your GitHub repository to Vercel
2. Configure environment variables:
   - `DATABASE_URL`: Your PostgreSQL connection string
3. Deploy automatically on every push

### Manual Deployment

```bash
# Build and deploy
vercel --prod
```

## 🔧 Configuration

Create a `.env` file:

```env
DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
```

## 🤝 Contributing

This project showcases:
- Clean, professional code structure
- Comprehensive documentation
- Modern Python development practices
- Full-stack deployment knowledge

Feel free to explore the codebase to see examples of:
- Async database operations
- File upload handling
- Error management
- API design patterns

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built with ❤️ and coffee using cutting-edge Python technologies**

*Showcasing expertise in backend development, database design, cloud deployment, and modern development workflows.*
