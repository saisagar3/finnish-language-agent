import os
import pandas as pd
from transformers import AutoTokenizer

class DataProcessor:
    def __init__(self, model_name="TurkuNLP/bert-base-finnish-uncased", data_dir="data"):
        self.data_dir = data_dir
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def load_raw_data(self, filename):
        """
        Load raw Finnish language data
        Supports CSV, TXT, and other common formats
        """
        filepath = os.path.join(self.data_dir, 'raw', filename)

        # Detect file type and load accordingly
        if filename.endswith('.csv'):
            return pd.read_csv(filepath)
        elif filename.endswith('.txt'):
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.readlines()
        else:
            raise ValueError(f"Unsupported file format: {filename}")
        
    def preprocess_data(self, data):
        """
        Preprocess raw data for tokenization
        - Tokenization
        - Lowercase conversion
        - Basic cleaning
        """

        # Tokenize with special handling for Finnish language
        tokens = self.tokenizer.tokenize(data)
        return tokens
    
    def training_data(self, raw_data):
        """
        Convert raw data into model-ready format
        """
        processed_data = [self.preprocess_data(data) for data in raw_data]
        return processed_data
    
if __name__ == "__main__":
    processor = DataProcessor()
    raw_data = processor.load_raw_data("finnish_corpus.txt")
    processed_data = processor.training_data(raw_data)