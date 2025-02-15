# AIProof

AIProof is an AI-powered proofreading tool that detects and highlights spelling mistakes, grammar issues, punctuation errors, and non-idiomatic expressions in structured HTML documents. It is designed as an API service using **FastAPI** for easy integration into products.

### Key Features:
✅ AI-based grammar correction using an LLM **BERT**

✅ Highlights spelling, punctuation, and syntax errors in **HTML**

✅ Easy-to-use **FastAPI** integration

✅ Supports bulk processing for large-scale content verification

### How It Works:
1. Upload an **HTML document** via the API.
2. AIProof scans the text and **highlights errors**.
3. Retrieve the corrected **HTML output**.
4. Seamlessly integrate the results into your applications.

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup
```sh
# Clone the repository
git clone https://github.com/yourusername/aiproof.git
cd aiproof

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Running the API
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at `http://127.0.0.1:8000`.

## API Usage
### Endpoint: `/process_html`
**Method:** `POST`

**Request:**
- Upload an HTML file as `multipart/form-data`

**Example using cURL:**
```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/process_html' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@sample.html'
```

**Response:**
```json
{
  "corrected_html": "<html>...</html>"
}
```

## Deployment
You can deploy AIProof using Docker:
```sh
# Build the Docker image
docker build -t aiproof .

# Run the container
docker run -p 8000:8000 aiproof
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## Author
- [Vishwanath Akuthota](https://www.github.com/vishwanathakuthota)
- [Follow Me](https://www.drpinnacle.com/)
- [Know more](https://techoptima.ai/about/Vishwanath%20Akuthota)
