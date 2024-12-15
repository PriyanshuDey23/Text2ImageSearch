# Fashion Cloth Search App

## Overview

The **Fashion Cloth Search App** is an intuitive tool that leverages advanced multimodal search capabilities to provide users with a seamless experience for searching fashion items using natural language queries. Built with the Haystack framework and Streamlit, this app uses state-of-the-art models for retrieving relevant fashion images based on text queries.

---

## Features

- **Multimodal Search**: Combines text-to-image retrieval powered by `sentence-transformers` and Haystack's `MultiModalRetriever`.
- **Dynamic Results Display**: Visual representation of search results with confidence scores.
- **User-Friendly Interface**: Built with Streamlit for a responsive and modern design.
- **Scalable Backend**: Uses an in-memory document store for efficient storage and retrieval of embeddings.

---

## How It Works

1. **Document Store**:
   - The app initializes an in-memory document store to store precomputed image embeddings.
2. **Image Embeddings**:
   - Images are converted to embeddings using the CLIP model (`sentence-transformers/clip-ViT-B-32`).
3. **Multimodal Search**:
   - Text queries are matched to image embeddings using the `MultiModalRetriever` from Haystack.
4. **Streamlit UI**:
   - The user enters a query through a text input box, and the app retrieves and displays the top results as images with confidence scores.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/PriyanshuDey23/Text2ImageSearch.git
   cd fashion-cloth-search-app
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Prepare the image data:

   - Place all your image files in the `Data/` directory (create the directory if it doesn’t exist).

---

## Usage

### Running the App

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at [http://localhost:8501](http://localhost:8501).

3. Enter a text query (e.g., "red dress") and click the **Search** button to retrieve relevant images.

### Example Queries

- "Black leather jacket"
- "Floral summer dress"
- "Running shoes"

---

## Code Structure

### Main Components

1. **`multimodal_search.py`**:

   - Contains the `MultimodalSearch` class responsible for initializing the document store, embedding models, and handling multimodal search logic.

2. **`app.py`**:

   - Implements the Streamlit-based user interface and integrates the `MultimodalSearch` class for seamless functionality.

### Key Functions

#### `multimodal_search.py`

- **`MultimodalSearch`**** Class**:
  - `__init__`: Initializes the document store, loads image embeddings, and sets up the multimodal retriever.
  - `search`: Executes a query and retrieves the top matching documents.

#### `app.py`

- **UI Functions**:
  - `display_header`: Displays the app's header.
  - `get_user_query`: Captures the user's query input.
  - `display_results`: Dynamically displays search results with images and confidence scores.
- **Backend Integration**:
  - `perform_search`: Handles the integration with `MultimodalSearch` for querying the document store.

---

## Technologies Used

- **Haystack**: Multimodal search framework.
- **Streamlit**: Frontend for a clean and interactive UI.
- **Sentence-Transformers**: Pre-trained models for generating embeddings (CLIP).
- **Python**: Core programming language.

---

## Future Enhancements

- Add support for large-scale datasets using vector databases like FAISS or Milvus.
- Implement image-based querying for more versatility.
- Add filters (e.g., category, color) for more granular searches.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push the branch.
4. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---





