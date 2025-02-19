import spacy

class SemanticTextSplitter:
    """
    A class for splitting text into semantic chunks without breaking sentences, utilizing spaCy's NLP capabilities.
    This class ensures that chunks are split at sentence boundaries whenever possible, providing more meaningful text segments.

    Parameters:
    - chunk_size (int): Maximum length of each text chunk in characters.
    - chunk_overlap (int): Number of characters each chunk can overlap with the next chunk. If less than 1, it is taken as a fraction of the chunk_size. 
       Note: When overlapped is used, it will violate the sentence boundary.
    - skip_chunk (int): Number of initial chunks to skip in the final output.
    - skip_char (int): Number of characters to skip at the beginning of the text, aligning to the nearest sentence boundary.
    - model (str): spaCy model identifier to be used for sentence tokenization and boundary detection.

    Usage:
    ```python
    # Example text
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    
    # Create an instance of SemanticTextSplitter
    splitter = SemanticTextSplitter(chunk_size=100, model="en_core_web_sm")
    
    # Split the text and print the results
    chunks = splitter.split_text(text)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {chunk}")
    ```

    This will split the text into chunks of up to 100 characters, each aligning with sentence boundaries as closely as possible.
    """    
    
    def __init__(self, chunk_size:int, chunk_overlap:float = 0, skip_chunk:int = 0, skip_char:int = 0, model:str = "en_core_web_sm"):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.skip_chunk = skip_chunk
        self.skip_char = skip_char
        self.nlp = spacy.load(model)
        
    def _find_sentence_boundary(self, text, skip_char):
        """
        Adjusts the skip_char to the start of the nearest complete sentence following the skip_char,
        considering a buffer around the skip_char for efficient processing.
        """
        if skip_char == 0:
            return 0  # Start from the beginning if no skip is required
        buffer_size = 1000  # Define a buffer size for contextual processing

        # Determine the range of text to analyze with spaCy
        end_index = min(len(text), skip_char + buffer_size)  # Ensure end index doesn't exceed text length

        doc = self.nlp(text[:end_index])  # Process only the relevant part of the text

        # Find the first sentence starting after skip_char within the buffered range
        boundary = next((sent.end_char for sent in doc.sents if sent.start_char >= skip_char), skip_char)
        return max(0, boundary)  # Adjust boundary relative to the full text
    
    def split_text(self, text):
        """ Public method to initiate the text splitting process after skipping initial characters and chunks. """
        start_index = self._find_sentence_boundary(text, self.skip_char)
        text=text[start_index:]
        chunks = self._recursive_text_splitter(text, self.chunk_size)
        return chunks[self.skip_chunk:]    
    
    #Original - without overlap
    def _recursive_text_splitter(self, text, chunk_size):
        if len(text) <= chunk_size:
            return [text]

        #buffer_size = int(0.1*chunk_size)  # Buffer to ensure sentence completeness
        buffer_size = 1000
        safe_end = min(chunk_size + buffer_size, len(text))
        doc = self.nlp(text[:safe_end])
        boundary_idx = chunk_size

        found=False
        for sent in doc.sents:
            if sent.end_char >= chunk_size and found:
                # If the sentence boundary is found after the chunk_size, that means the sentence is too long.
                # That is why we cannot break too early.
                break
            boundary_idx = sent.end_char
            found=True

        first_part = text[:boundary_idx].strip()
        if self.chunk_overlap > 0:
            if self.chunk_overlap > 1:
                first_part_size_with_overlap = len(first_part)+self.chunk_overlap
            elif self.chunk_overlap < 1:
                first_part_size_with_overlap = len(first_part) + int((self.chunk_overlap)*chunk_size)
            first_part_size_with_overlap = min(first_part_size_with_overlap, len(text))
            first_part = text[:first_part_size_with_overlap].strip()

        rest = text[boundary_idx:].strip()

        # Handle the remaining text by checking if it's smaller than chunk_size but not empty
        if len(rest) <= chunk_size and rest:
            return [first_part, rest]
        else:
            return [first_part] + self._recursive_text_splitter(rest, chunk_size)    

    # Modified - with overlap                
    # def _recursive_text_splitter(self, text, chunk_size):
    #     if len(text) <= chunk_size:
    #         return [text]

    #     buffer_size = 1000  # Buffer to ensure sentence completeness
    #     safe_end = min(chunk_size + buffer_size, len(text))
    #     doc = self.nlp(text[:safe_end])
    #     boundary_idx = chunk_size

    #     for sent in doc.sents:
    #         if sent.end_char > chunk_size:
    #             break
    #         boundary_idx = sent.end_char

    #     first_part = text[:boundary_idx].strip()
        
    #     # if self.chunk_overlap != 0:
        
    #     #     if self.chunk_overlap > 0:
    #     #         first_part_size_with_overlap = len(first_part)+self.chunk_overlap
    #     #     elif self.chunk_overlap < 0:
    #     #         first_part_size_with_overlap = len(first_part) + (self.chunk_overlap)*chunk_size
    #     #     first_part_size_with_overlap = min(first_part_size_with_overlap, len(text))
    #     #     first_part = text[:first_part_size_with_overlap].strip()
        
    #     rest = text[boundary_idx:].strip()
    #     return [first_part] + self._recursive_text_splitter(rest, chunk_size)     
