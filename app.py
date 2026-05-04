import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

print("--- 1. MANUAL LOADING INITIATED ---")

model_name = "sshleifer/distilbart-cnn-12-6"

try:
    # We load the pieces individually to bypass the 'Unknown Task' error
    print("Loading Tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    print("Loading Model Brain (this may take a minute)...")
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    print("--- SUCCESS: AI Components Loaded! ---")
    status = "Ready"
except Exception as e:
    print(f"--- FAILED --- \nError: {e}")
    status = f"Error: {e}"

def ai_summarize(text):
    if "Error" in status:
        return "Model failed to load. Check terminal."
    if not text.strip():
        return "Please enter text."

    try:
        inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
        
        summary_ids = model.generate(
            inputs["input_ids"], 
            max_length=300,       # Increased from 130 (Allow more room)
            min_length=80,        # Increased from 30 (Force it to be longer)
            length_penalty=1.5,   # Encourages the model to use more words
            num_beams=4, 
            early_stopping=True
        )
        
        summary = tokenizer.decode(summary_ids, skip_special_tokens=True)
        return summary
    except Exception as e:
        return f"Processing Error: {e}"

# UI Layout
with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Manual-Load AI Summarizer")
    with gr.Row():
        input_box = gr.Textbox(label="Input Text", lines=10)
        output_box = gr.Textbox(label="AI Summary", lines=10)
    btn = gr.Button("Summarize", variant="primary")
    btn.click(ai_summarize, inputs=input_box, outputs=output_box)

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft(), debug=True)
