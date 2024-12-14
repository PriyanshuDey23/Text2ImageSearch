from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import MultiModalRetriever
from haystack import Pipeline
from haystack import Document
import os

from haystack.document_stores import InMemoryDocumentStore

class MultimodalSearch:
    def __init__(self):
        # Initialize the DocumentStore to store 512 dim image embeddings
        self.document_store = InMemoryDocumentStore(embedding_dim=512)

        # Directory containing the images
        doc_dir = "Data"

        # Prepare image documents
        images = [
            Document(content=f"./{doc_dir}/{filename}", content_type="image")
            for filename in os.listdir(f"./{doc_dir}")
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))
        ]

        # Write image documents to the store
        self.document_store.write_documents(images)

        # Initialize the multimodal retriever
        self.retriever_text_to_image = MultiModalRetriever(
            document_store=self.document_store,
            query_embedding_model="sentence-transformers/clip-ViT-B-32",
            query_type="text",
            document_embedding_models={"image": "sentence-transformers/clip-ViT-B-32"},
        )

        # Generate and store embeddings
        self.document_store.update_embeddings(retriever=self.retriever_text_to_image)

        # Create a pipeline and add the retriever
        self.pipeline = Pipeline()
        self.pipeline.add_node(component=self.retriever_text_to_image, name="retriever_text_to_image", inputs=["Query"])

    def search(self, query, top_k=3):
        # Run the pipeline to perform the search
        results = self.pipeline.run(query=query, params={"retriever_text_to_image": {"top_k": top_k}})
        return sorted(results["documents"], key=lambda d: d.score, reverse=True)
