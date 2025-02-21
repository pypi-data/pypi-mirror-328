from typing import Dict, Union
import logging
from datetime import datetime
from transformers import pipeline
import torch
# Define available language codes for SRSWTI Multilingual System
SRSWTI_LANGUAGE_CODES = {
    'English': 'en', 'Spanish': 'es', 'French': 'fr',
    'German': 'de', 'Italian': 'it', 'Portuguese': 'pt',
    'Russian': 'ru', 'Chinese': 'zh', 'Japanese': 'ja',
    'Korean': 'ko', 'Arabic': 'ar', 'Hindi': 'hi',
    'Dutch': 'nl', 'Polish': 'pl', 'Turkish': 'tr'
}

class SRSWTIMultilingualTranslator:
    """SRSWTI Multilingual Translation Utility"""
    
    def __init__(self, device: str = None, config=None):
        """
        Initialize SRSWTI Multilingual Translator
        
        :param device: Device to run the model on (cuda, mps, cpu)
        :param config: Optional configuration dictionary
        """
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] SRSWTI-Multilingual-Translator: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger("SRSWTI-Multilingual-Translator")
        self.logger.setLevel(logging.INFO)
        
        # Determine device
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
            
        self.logger.info(f"Initializing SRSWTI Multilingual Translator on {device}")
        self.device = device
        self.translators = {}
        
    def _get_model_name(self, src_lang: str, tgt_lang: str) -> str:
        """
        Generate a SRSWTI Multilingual model name
        
        :param src_lang: Source language code
        :param tgt_lang: Target language code
        :return: Formatted model name
        """
        return f"SRSWTI-Multilingual-{src_lang}-{tgt_lang}"
    
    def _load_translation_model(self, src_code: str, tgt_code: str):
        """
        Load and cache translation model
        
        :param src_code: Source language code
        :param tgt_code: Target language code
        :return: Translation pipeline
        """
        model_key = f"{src_code}-{tgt_code}"
        if model_key not in self.translators:
            model_name = "Helsinki-NLP/opus-mt-{src_code}-{tgt_code}".format(src_code=src_code, tgt_code=tgt_code)
            self.translators[model_key] = pipeline("translation", model=model_name, device=self.device)
        return self.translators[model_key]
    
    def translate_text(self, text: str, src_lang: str, tgt_lang: str) -> Dict[str, Union[str, Dict]]:
        """
        Translate text with comprehensive logging and structured output
        
        :param text: Text to translate
        :param src_lang: Source language name
        :param tgt_lang: Target language name
        :return: Translation result with metadata
        """
        start_time = datetime.now()
        
        try:
            # Validate language codes
            src_code = SRSWTI_LANGUAGE_CODES.get(src_lang)
            tgt_code = SRSWTI_LANGUAGE_CODES.get(tgt_lang)
            
            if not src_code or not tgt_code:
                raise ValueError(f"Invalid language selection! Available options: {list(SRSWTI_LANGUAGE_CODES.keys())}")
            
            # Get translation model and perform translation
            translator = self._load_translation_model(src_code, tgt_code)
            result = translator(text)
            translated_text = result[0]["translation_text"]
            
            processing_time = (datetime.now() - start_time).total_seconds()
            
            # Structured output with metadata
            return {
                'translation': translated_text,
                'metadata': {
                    'source_language': src_lang,
                    'target_language': tgt_lang,
                    'processing_time': round(processing_time, 4),
                    'model': self._get_model_name(src_code, tgt_code),
                    'device': self.device.upper(),
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
            }
        
        except Exception as e:
            self.logger.error(f"Translation error: {str(e)}")
            return {
                'translation': None,
                'error': str(e)
            }

def print_translation_results(result: Dict):
    """
    Pretty print translation results
    
    :param result: Translation result dictionary
    """
    if result.get('error'):
        print("\n❌ SRSWTI Multilingual Translation Error")
        print(f"Error: {result['error']}")
        return
    
    print("\n🌐 SRSWTI Multilingual Translation Results")
    print("=" * 50)
    
    metadata = result.get('metadata', {})
    print(f"• Source Language:   {metadata.get('source_language', 'N/A')}")
    print(f"• Target Language:   {metadata.get('target_language', 'N/A')}")
    print(f"• Processing Time:   {metadata.get('processing_time', 'N/A')} seconds")
    print(f"• Device:           {metadata.get('device', 'N/A')}")
    print(f"• Timestamp:         {metadata.get('timestamp', 'N/A')}")
    print(f"• Model:             {metadata.get('model', 'N/A')}")
    
    print("\nTranslation:")
    print("-" * 50)
    print(result.get('translation', 'No translation available'))

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] SRSWTI-Multilingual: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Example translations
    examples = [
        {"text": "The rapid advancement of artificial intelligence and machine learning technologies has revolutionized the way we approach complex problems in fields ranging from healthcare to environmental conservation.", 
         "from": "English", "to": "French"},
        {"text": "La inteligencia artificial está transformando nuestra sociedad de maneras fundamentales, creando nuevas oportunidades y desafíos que debemos abordar con sabiduría y previsión.", 
         "from": "Spanish", "to": "English"},
        {"text": "人工知能と機械学習の進歩は、医療からビジネス、教育まで、私たちの生活のあらゆる側面に革命的な変化をもたらしています。この技術革新は、人類の可能性を大きく広げる一方で、慎重な検討と倫理的な配慮も必要としています。",
         "from": "Japanese", "to": "English"},
        {"text": "Die Integration von künstlicher Intelligenz in unseren Alltag erfordert eine sorgfältige Abwägung zwischen technologischem Fortschritt und ethischen Überlegungen, wobei der Schutz der Privatsphäre und die gesellschaftliche Verantwortung im Vordergrund stehen müssen.",
         "from": "German", "to": "Italian"},
        {"text": "आधुनिक तकनीकी विकास ने मानव जीवन को पूरी तरह से बदल दिया है। कृत्रिम बुद्धिमत्ता और मशीन लर्निंग के क्षेत्र में हुई प्रगति ने हमारी कार्यक्षमता को कई गुना बढ़ा दिया है, लेकिन साथ ही यह महत्वपूर्ण है कि हम इन तकनीकों का उपयोग मानवता की भलाई के लिए करें।",
         "from": "Hindi", "to": "English"}
    ]

    translator = SRSWTIMultilingualTranslator()
    
    for example in examples:
        print(f"\nTranslating from {example['from']} to {example['to']}:")
        print(f"Original: {example['text']}")
        
        result = translator.translate_text(example['text'], example['from'], example['to'])
        print_translation_results(result)
