import torch
from transformers import pipeline
from rich.console import Console
from rich.panel import Panel
from typing import List, Dict
import logging
from datetime import datetime
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] SRSWTI-LLM: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class SRSWTILanguageModel:
    """SRSWTI Advanced Language Model Interface"""
    
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        """
        Initialize the SRSWTI Language Model
        
        Args:
            model_name (str): Hugging Face model identifier
        """
        self.logger = logging.getLogger("SRSWTI-LLM")
        self.console = Console()
        
        # Chat history tracking
        self.chat_history: List[Dict[str, str]] = []
        
        # Initialize pipeline
        try:
            self.pipe = pipeline(
                "text-generation", 
                model=model_name, 
                torch_dtype=torch.bfloat16, 
                device_map="auto"
            )
            self.logger.info(f"Initialized language model: {model_name}")
        except Exception as e:
            self.logger.error(f"Model initialization failed: {e}")
            raise

    def generate_response(self, messages: List[Dict[str, str]]) -> str:
        """
        Generate a response using the language model pipeline.
        
        Args:
            messages (List[Dict[str, str]]): Conversation context
        
        Returns:
            str: Generated response
        """
        try:
            prompt = self.pipe.tokenizer.apply_chat_template(
                messages, 
                tokenize=False, 
                add_generation_prompt=True
            )
            outputs = self.pipe(
                prompt, 
                max_new_tokens=256, 
                do_sample=True, 
                temperature=0.5, 
                top_k=50, 
                top_p=0.95
            )
            return outputs[0]["generated_text"]
        except Exception as e:
            self.logger.error(f"Response generation error: {e}")
            raise

    def interactive_chat(self):
        """Start an interactive chat session with the SRSWTI Language Model."""
        # Initial system message
        messages = [
            {
                "role": "system",
                "content": "You are an advanced AI assistant developed by TEAM SRSWTI, a Knowledge and Inference Platform. Always be super concise",
            }
        ]
        
        self.console.print(Panel.fit("SRSWTI Language Model", style="bold blue"))
        
        while True:
            # Get user input
            user_input = self.console.input("[bold green]You: [/bold green]")
            
            # Check for exit
            if user_input.lower() in ['exit', 'quit', 'bye']:
                self.console.print(Panel("Ending SRSWTI Language Model session", style="bold red"))
                break
            
            # Add user message to conversation
            messages.append({"role": "user", "content": user_input})
            
            try:
                # Generate response
                full_response = self.generate_response(messages)
                
                # Extract just the assistant's response
                assistant_response = full_response.split('<|assistant|>')[-1].strip()
                
                # Print response
                self.console.print(Panel(
                    assistant_response, 
                    title="[bold blue]SRSWTI Assistant[/bold blue]", 
                    border_style="bold cyan"
                ))
                
                # Add to chat history
                self.chat_history.append({
                    "user": user_input,
                    "assistant": assistant_response
                })
                
                # Add assistant message to conversation
                messages.append({"role": "assistant", "content": assistant_response})
            
            except Exception as e:
                self.console.print(f"[bold red]Error: {e}[/bold red]")

def main():
    try:
        llm = SRSWTILanguageModel()
        llm.interactive_chat()
    except Exception as e:
        logging.error(f"Main execution error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
