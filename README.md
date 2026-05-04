# 🧠 AI-Powered Text Summarizer 

An end-to-end NLP (Natural Language Processing) application that uses the **DistilBART** transformer model to generate concise, human-like summaries from long-form text. Built with a modern web interface using **Gradio**.

## 🚀 Overview
This project provides a web-based tool for **Abstractive Summarization**. Unlike simple text-cropping, this application uses a deep learning model to "read" the context and rewrite the text into a shorter, coherent paragraph while retaining all key information.

## ✨ Features
- **Deep Learning Intelligence**: Utilizes the `distilbart-cnn-12-6` model for high-quality abstractive summaries.
- **Responsive Web UI**: A clean, user-friendly interface built with Gradio.
- **Customized Generation**: Engineered with specific beam search and length penalty parameters to ensure detailed and accurate outputs.
- **Performance Optimized**: Uses a distilled model to allow for fast processing even on CPU-based systems.

## 🛠️ Tech Stack
- **Language**: Python 3.11
- **Machine Learning**: Hugging Face Transformers
- **Back-end Engine**: PyTorch
- **UI Framework**: Gradio

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd ai-text-summarizer
   ```

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Access the App:**
   Open your browser and navigate to `http://127.0.0.1:7860`.

## 📝 Project Structure
- `app.py`: The main Python script containing the AI logic and Gradio interface.
- `requirements.txt`: List of dependencies required to run the project.
- `README.md`: Project documentation.

## 📊 Sample Output
<img width="960" height="435" alt="image" src="https://github.com/user-attachments/assets/1e97663f-48c4-4740-b488-f871bd5469ee" />

## ⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.

