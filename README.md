# Gemini-Pro

# Invoice Reader using Google Gemini AI and Streamlit

A specialized invoice analysis tool built with Google's Gemini AI and Streamlit, designed to extract and analyze information from invoice images through natural language queries.


## Features

- Invoice Analysis: Processes and analyzes invoice images for accurate information extraction
- Interactive Q&A: Ask questions about invoice contents in natural language
- Image Processing: Handles multiple image formats (JPG, JPEG, PNG)
- Web Interface: Streamlit-based interface for easy interaction


## Tech Stack

**LLM**: Google Gemini AI
**Web Framework**: Streamlit
**API Integration**: Google GenerativeAI


## Project Structure

```bash
gemini-invoice-reader/
├── app.py
├── setup.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── helper.py
├── sample_images/
│   └── [invoice images]
```


## Installation

```bash
git clone https://github.com/yourusername/gemini-invoice-reader.git
cd Invoice-Reader_Gemini-Pro
pip install -r requirements.txt
streamlit run app.py
```
