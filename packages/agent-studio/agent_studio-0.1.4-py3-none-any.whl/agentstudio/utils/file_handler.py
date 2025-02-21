import os
import json
from typing import Any, Dict
import streamlit as st
from typing import List, Dict, Any, Optional
import tempfile
import chardet
from PyPDF2 import PdfReader
import shutil

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text content from PDF file"""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")

def handle_file_upload(uploaded_files: List[Any], agent_config: Dict[str, Any]) -> Optional[str]:
    """Handle file uploads for RAG tool configuration"""
    if not uploaded_files:
        return None

    # Create temp directory for document storage
    temp_dir = tempfile.mkdtemp()

    # Save uploaded files
    saved_files = []
    for uploaded_file in uploaded_files:
        file_path = os.path.join(temp_dir, uploaded_file.name)
        try:
            # Save the uploaded file in binary mode
            with open(file_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())

            # Process based on file type
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension == '.pdf':
                # Extract text from PDF
                text_content = extract_text_from_pdf(file_path)
                # Save extracted text to a new file
                text_file_path = os.path.splitext(file_path)[0] + '.txt'
                with open(text_file_path, 'w', encoding='utf-8') as f:
                    f.write(text_content)
                saved_files.append(text_file_path)
                # Remove original PDF file
                os.remove(file_path)
                st.success(f"Successfully processed PDF: {uploaded_file.name}")
            else:
                # Handle text files with encoding detection
                with open(file_path, 'rb') as f:
                    raw_data = f.read()
                    detected = chardet.detect(raw_data)
                    encoding = detected['encoding'] or 'utf-8'

                # Rewrite with detected encoding
                with open(file_path, 'w', encoding='utf-8') as f:
                    content = raw_data.decode(encoding)
                    f.write(content)
                saved_files.append(file_path)
                st.success(f"Successfully processed: {uploaded_file.name}")

        except Exception as e:
            st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
            try:
                # Clean up the failed file
                if os.path.exists(file_path):
                    os.remove(file_path)
            except:
                pass

    if not saved_files:
        cleanup_files(temp_dir)
        return None

    return temp_dir

def cleanup_files(temp_dir: str) -> None:
    """Clean up temporary files"""
    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            st.success("Cleaned up temporary files")
    except Exception as e:
        st.warning(f"Error cleaning up temporary files: {str(e)}")

def save_json(file_path: str, data: Dict[str, Any]) -> None:
    """Save data to a JSON file"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        st.success(f"Successfully saved to {file_path}")
    except Exception as e:
        st.error(f"Error saving file: {str(e)}")
        raise

def load_json(file_path: str) -> Dict[str, Any]:
    """Load data from a JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        raise