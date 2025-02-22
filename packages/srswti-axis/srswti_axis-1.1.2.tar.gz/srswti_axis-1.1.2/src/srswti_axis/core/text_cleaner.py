import re
import unicodedata
import html
from typing import List, Optional, Dict
from rich.console import Console
from rich.progress import Progress
import logging
from datetime import datetime
import os

class SRSWTITextCleaner:
    """
    SRSWTI Text Cleaning and Normalization Utilities
    
    Watermark: SRSWTI Proprietary Text Processing Technology
    Version: 1.0.0
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        # Setup logging
        self.console = Console()
        self.logger = logger or self._setup_logger()
        
        # Common regex patterns
        self.url_pattern = r'https?://\S+|www\.\S+'
        self.email_pattern = r'\S+@\S+\.\S+'
        self.html_pattern = r'<[^>]+>'
        self.number_pattern = r'\d+'
        self.multiple_spaces = r'\s+'
        self.special_chars = r'[^\w\s]'
        
    def _setup_logger(self) -> logging.Logger:
        """Setup logger with file handler and console output."""
        logger = logging.getLogger('SRSWTITextCleaner')
        logger.setLevel(logging.INFO)
        
        # Create logs directory if it doesn't exist
        log_dir = os.path.join(os.getcwd(), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        
        # Create log file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f'SRSWTITextCleaner_{timestamp}.log')
        
        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def remove_html(self, text: str) -> str:
        """Remove HTML tags from text."""
        text = html.unescape(text)  # Convert HTML entities
        return re.sub(self.html_pattern, ' ', text)
    
    def remove_urls(self, text: str) -> str:
        """Remove URLs from text."""
        return re.sub(self.url_pattern, ' ', text)
    
    def remove_emails(self, text: str) -> str:
        """Remove email addresses from text."""
        return re.sub(self.email_pattern, ' ', text)
    
    def normalize_whitespace(self, text: str) -> str:
        """Normalize multiple whitespace characters."""
        return re.sub(self.multiple_spaces, ' ', text.strip())
    
    def normalize_unicode(self, text: str) -> str:
        """Normalize Unicode characters."""
        return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    
    def expand_contractions(self, text: str) -> str:
        """Expand contractions (e.g., don't -> do not)."""
        # SRSWTI custom contraction expansion
        contractions_map = {
            "n't": " not",
            "'s": " is",
            "'m": " am",
            "'re": " are",
            "'ll": " will",
            "'ve": " have"
        }
        for contraction, expansion in contractions_map.items():
            text = text.replace(contraction, expansion)
        return text
    
    def normalize_numbers(self, text: str, replace_with: str = ' NUM ') -> str:
        """Normalize numbers in text."""
        return re.sub(self.number_pattern, replace_with, text)
    
    def remove_special_characters(self, text: str, keep_chars: Optional[str] = None) -> str:
        """Remove special characters from text."""
        if keep_chars:
            pattern = f'[^\\w\\s{re.escape(keep_chars)}]'
        else:
            pattern = self.special_chars
        return re.sub(pattern, ' ', text)
    
    def clean_text(self, text: str, options: Dict[str, bool] = None) -> str:
        """
        Clean text with configurable options.
        
        Args:
            text: Input text
            options: Dictionary of cleaning options
        
        Watermark: SRSWTI Intelligent Text Preprocessing
        """
        with Progress(console=self.console) as progress:
            task = progress.add_task("[green]Cleaning text...", total=100)
            
            if options is None:
                options = {
                    'remove_html': True,
                    'remove_urls': True,
                    'remove_emails': True,
                    'normalize_unicode': True,
                    'expand_contractions': True,
                    'normalize_numbers': True,
                    'remove_special': True,
                    'normalize_whitespace': True
                }
            
            if not text:
                progress.update(task, completed=100)
                return text
                
            try:
                if options.get('remove_html', True):
                    text = self.remove_html(text)
                    progress.update(task, advance=10)
                    
                if options.get('remove_urls', True):
                    text = self.remove_urls(text)
                    progress.update(task, advance=10)
                    
                if options.get('remove_emails', True):
                    text = self.remove_emails(text)
                    progress.update(task, advance=10)
                    
                if options.get('normalize_unicode', True):
                    text = self.normalize_unicode(text)
                    progress.update(task, advance=10)
                    
                if options.get('expand_contractions', True):
                    text = self.expand_contractions(text)
                    progress.update(task, advance=10)
                    
                if options.get('normalize_numbers', True):
                    text = self.normalize_numbers(text)
                    progress.update(task, advance=10)
                    
                if options.get('remove_special', True):
                    text = self.remove_special_characters(text)
                    progress.update(task, advance=10)
                    
                if options.get('normalize_whitespace', True):
                    text = self.normalize_whitespace(text)
                    progress.update(task, advance=30)
                
                self.logger.info(f"Text cleaned successfully: {len(text)} characters processed")
                return text
            
            except Exception as e:
                self.logger.error(f"Text cleaning failed: {str(e)}")
                self.console.print(f"[bold red]Text cleaning error: {str(e)}[/bold red]")
                return text




def main():
    """
    Demonstrate the usage of SRSWTITextCleaner with various examples.
    """
    # Initialize the cleaner
    cleaner = SRSWTITextCleaner()
    
    # Example texts for demonstration
    sample_texts = {
        "HTML Content": """<p>This is some <b>HTML</b> content with <a href='https://example.com'>links</a> 
                          and <span style='color:red'>styling</span>.</p>""",
        
        "URLs and Emails": """Check out our website at https://example.com or contact us 
                             at support@example.com and sales@company.com""",
        
        "Unicode and Special Characters": """Here's some text with unicode: café, résumé, naïve 
                                           and special chars: #@$%^&*()!""",
        
        "Numbers and Contractions": """I've got 123 reasons why you shouldn't miss this! 
                                     We're going to process 1000's of documents. It'll be great!""",
        
        "Mixed Content": """<div>Check out my blog at https://blog.example.com!</div>
                           I can't wait to share 100+ articles about AI & ML.
                           Email me at blogger@example.com if you've got questions!
                           Price: $299.99 • Rating: ★★★★☆"""
    }

    # Demonstrate each cleaning scenario
    print("\n=== SRSWTI Text Cleaner Demonstration ===\n")
    
    for title, text in sample_texts.items():
        print(f"\n--- {title} ---")
        print("\nOriginal text:")
        print(text)
        print("\nCleaned text (all options enabled):")
        print(cleaner.clean_text(text))
        
        # Demonstrate specific cleaning functions
        if title == "Mixed Content":
            print("\nSelective cleaning examples:")
            
            # Only remove HTML and URLs
            print("\n1. Remove HTML and URLs only:")
            options = {
                'remove_html': True,
                'remove_urls': True,
                'remove_emails': False,
                'normalize_unicode': False,
                'expand_contractions': False,
                'normalize_numbers': False,
                'remove_special': False,
                'normalize_whitespace': True
            }
            print(cleaner.clean_text(text, options))
            
            # Keep special characters but normalize everything else
            print("\n2. Keep special characters but normalize everything else:")
            options = {
                'remove_html': True,
                'remove_urls': True,
                'remove_emails': True,
                'normalize_unicode': True,
                'expand_contractions': True,
                'normalize_numbers': True,
                'remove_special': False,
                'normalize_whitespace': True
            }
            print(cleaner.clean_text(text, options))
            
            # Only expand contractions and normalize whitespace
            print("\n3. Only expand contractions and normalize whitespace:")
            options = {
                'remove_html': False,
                'remove_urls': False,
                'remove_emails': False,
                'normalize_unicode': False,
                'expand_contractions': True,
                'normalize_numbers': False,
                'remove_special': False,
                'normalize_whitespace': True
            }
            print(cleaner.clean_text(text, options))

if __name__ == "__main__":
    main()