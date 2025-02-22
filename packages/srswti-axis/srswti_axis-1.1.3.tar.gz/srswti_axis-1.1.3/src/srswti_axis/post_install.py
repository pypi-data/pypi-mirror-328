import subprocess
import sys
import platform
from datetime import datetime

import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def print_banner():
    banner = """
    ███████╗██████╗ ███████╗██╗    ██╗████████╗██╗    █████╗ ██╗  ██╗██╗███████╗
    ██╔════╝██╔══██╗██╔════╝██║    ██║╚══██╔══╝██║   ██╔══██╗╚██╗██╔╝██║██╔════╝
    ███████╗██████╔╝███████╗██║ █╗ ██║   ██║   ██║   ███████║ ╚███╔╝ ██║███████╗
    ╚════██║██╔══██╗╚════██║██║███╗██║   ██║   ██║   ██╔══██║ ██╔██╗ ██║╚════██║
    ███████║██║  ██║███████║╚███╔███╔╝   ██║   ██║   ██║  ██║██╔╝ ██╗██║███████║
    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝    ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
    """
    print(banner)
    # New ASCII art
    srswti_art = """
                               ,R▒▒▒╦╦╓_        _╓╔╦▒▒▒╠╖
                              ╔▒▒▒▒▒▒▒▒▒╠╦_  _╔R▒Ü▒▒Ü▒ÜÜ░▒
                             [▒▒▒▒▒▒▒▒▒▒▒╠^,,'╠Ü▒Ü▒Ü▒▒▒ÜÜÜ╠
                            j▒▒▒▒▒▒▒▒▒▒▒╩ j▒▒▒ ╚▒Ü▒ÜÜÜÜÜÜÜ░H
                            ╚▒▒▒▒▒▒▒▒Ü▒╩ ╩▒▒ÜÜ╠ ╚ÜÜ░ÜÜ░▒▒░░▒
                      ,╓╔╦╦ ╔╦╔╓_`²╚▒░▒ j▒ÜÜÜÜ░▒ ÜÜ▒╩╙^_,╓╔╔ ╔╔╓,_
                  ╓╦╠▒▒▒▒▒▒_j▒▒▒▒▒▒╔,'╙ ▒▒ÜÜÜÜ░░ ╙`,╔RÜÜÜÜÜÜ ÜÜ▒▒Ü░▒╦_
                j╠▒▒▒▒▒▒▒▒▒╠ ╠▒▒▒▒▒▒Ü╠r ╙░░ÜÜÜ░╙ ╔╠░Ü░░ÜÜÜ▒ [Ü▒Ü▒ÜÜ▒▒▒╠╔
                 ▒▒▒▒▒▒▒▒▒▒▒╦ ╠▒▒▒▒▒ÜÜ▒ ╓`╠▒Ü╩ ╔ ╚ÜÜÜ░ÜÜ▒╠ ╔ÜÜÜ░ÜÜ▒▒▒▒▒H
                 ╚▒▒▒▒▒▒▒▒▒▒▒▒_╙▒▒▒▒ÜÜ▒ j¼ ╚╩ ╚H╒░░░░ÜÜÜ╙ j░Ü▒▒ÜÜÜ▒Ü▒▒▒
                  ╚▒▒▒▒▒▒╝╙^`_,._ ,_'²╚╩ ╚U  ╚H_Ü╚²^`_  _`'^²╚▒▒▒▒Ü▒Ü╠
                   '╠╠╙_╓╦R▒▒▒▒▒Ü▒╓`²╚╦╔_ ²  ` ,╔▒R^ ╓╦ÜÜÜ░░▒╦╔_'╚▒▒╩
                    ² %▒Ü▒ÜÜÜÜÜÜÜÜ░ÜR² _,.    ,_ ¬«▒░Ü▒ÜÜ▒▒▒▒▒▒▒╠⌐
                  ╓╠Ü╠╦,`²╚╠░░ÜÜ╠²_╓╦R╙^  ╔ j_ `²╚╦╓_²╠▒Ü▒▒▒▒╝^`╓╦╠R_
                 ╔ÜÜ▒Ü░ÜÜ▒K╔╓╓. _,╓╓╔╦▒╙ ╚`, ╠_'▒╦╔╓,__``_,╓╔╦R▒▒▒▒▒╠_
                j▒▒Ü▒▒▒ÜÜ▒▒░▒^,╩▒ÜÜ░░░╠ ╩^,Ü╦ ╠ ╙░Ü▒▒▒▒╠²'▒▒▒▒▒▒▒▒▒▒▒╠
                ▒ÜÜÜÜÜÜÜ░ÜÜ╠ ╔ÜÜ░Ü░Ü░ÜH! ╔Ü░Ü╦ % ÜÜÜ▒Ü▒▒▒╦ ╠▒▒▒▒▒▒▒▒▒▒▒
                ╚▒▒Ü░▒▒Ü▒▒▒ j░ÜÜ░ÜÜ░░╩ ,R░ÜÜÜÜ╠╖ ╚▒▒▒▒▒▒▒▒H ▒▒▒▒▒▒▒▒▒▒╩
                  '╚╠▒▒ÜÜ▒Ü ÜÜÜ░Ü▒╚^_╔ [ÜÜ░░Ü▒▒╩ ╦_'╚╠▒▒▒▒▒ ╚▒▒▒▒▒▒╩^
                       `"^ '^^`_╓╔▒╠░Ü╦ ▒Ü▒░ÜÜ▒ jÜÜ╠╔╔,_'^╙ '╙^^`
                           [ÜÜÜÜ▒▒ÜÜÜÜ▒_'▒Ü▒▒▒H,▒▒Ü▒▒▒▒▒▒▒╠
                            ▒░Ü▒▒ÜÜÜ░Ü▒Ü╓`╠▒╠`╓╠▒▒▒▒▒▒▒▒▒▒╠
                            '▒Ü▒▒ÜÜÜÜ▒▒▒Ü╦_" j▒▒▒▒▒▒▒▒▒▒▒▒`
                             '▒░Ü▒▒ÜÜ▒▒▒╚^   '╚▒▒▒▒▒▒▒▒▒╠`
                               ╚▒Ü╩╚²^          `"╙╚╩▒▒╙
    """
    print(srswti_art)



# def install_spacy_model():
#     """Install spaCy model using spacy.cli."""
#     # First check if pip is available
#     try:
#         import pip
#     except ImportError:
#         import os
#         import sys
        
#         # Download and install pip
#         os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
#         os.system(f"{sys.executable} get-pip.py")
        
#         # Clean up
#         if os.path.exists("get-pip.py"):
#             os.remove("get-pip.py")

#     # Then proceed with spacy installation
#     try:
#         import spacy
#         try:
#             spacy.load('en_core_web_sm')
#             logger.info(" misc is already installed.")
#         except OSError:
#             logger.info("Installing misc packages...")
#             spacy.cli.download('en_core_web_sm')
#             logger.info("misc packages installed successfully.")
#     except Exception as e:
#         logger.error(f"⚠️  Error installing spaCy model: {e}")
#         logger.info("Please run 'python -m spacy download en_core_web_sm' manually")
#         return False
#     return True

def install_spacy_model():
    """Install spaCy model using spacy.cli."""
    # First check if pip is available
    try:
        import pip
    except ImportError:
        import os
        import sys
        
        # Download and install pip
        os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
        os.system(f"{sys.executable} get-pip.py")
        
        # Clean up
        if os.path.exists("get-pip.py"):
            os.remove("get-pip.py")

    # Then proceed with spacy installation
    try:
        import spacy
        try:
            spacy.load('en_core_web_sm')
            logger.info(" misc is already installed.")
        except OSError:
            logger.info("Installing misc packages...")
            os.system("uv run --with spacy python -m spacy download en_core_web_sm")
            logger.info("misc packages installed successfully.")
    except Exception as e:
        logger.error(f"⚠️  Error installing spaCy model: {e}")
        logger.info("Please run 'uv run --with spacy python -m spacy download en_core_web_sm' manually")
        return False
    return True



def post_install():
    """Post-installation guide for SRSWTI AXIS package."""
    
    
    print("\n Welcome to SRSWTI AXIS! ")
    print("=" * 50)

    # Installation info
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🖥️  System: {platform.system()} {platform.release()}")
    
    print("\n📚 SRSWTI AXIS Components:")
    print("=" * 50)
    
    # Search & Ranking
    print("\n🔍 Search & Ranking Systems")
    print("  • Neural Graph Search")
    print("    - PageRank-enhanced semantic search")
    print("    - Document graph relationships")
    print("    - Cluster-aware ranking")
    print("\n  • Hilbert Search")
    print("    - Learning to Rank system")
    print("    - Multiple ranking approaches")
    print("    - Feature-based scoring")
    print("\n  • Advanced BM25")
    print("    - Probabilistic ranking")
    print("    - Term importance weighting")
    print("    - Proximity analysis")

    # NLP Core
    print("\n🧠 Natural Language Processing")
    print("  • Sentiment Analysis")
    print("    - Aspect-based analysis")
    print("    - Domain-specific modifiers")
    print("    - Multi-component scoring")
    print("\n  • Text Summarization")
    print("    - Multiple model types (lightweight to xlarge)")
    print("    - Long document handling")
    print("    - Chunk-based processing")
    print("\n  • Multilingual Translation")
    print("    - 15+ language support")
    print("    - Model caching")
    print("    - Detailed metadata")

    # Document Processing
    print("\n📄 Document Processing")
    print("  • Topic Modeling")
    print("    - Multiple backend support")
    print("    - Custom topic extraction")
    print("    - Hierarchical analysis")
    print("\n  • Text Classification")
    print("    - Zero-shot capabilities")
    print("    - Multi-label support")
    print("    - Confidence scoring")
    print("\n  • Document Merging")
    print("    - Graph-based merging")
    print("    - Semantic coherence")
    print("    - Topic preservation")

    
    # Search Example
    print("\n1. Neural Graph Search:")
    print("""    from srswti_axis import SRSWTISearchEngine
    
    engine = SRSWTISearchEngine()
    results = engine.search("query", documents)""")
    
    # Sentiment Example
    print("\n2. Sentiment Analysis:")
    print("""    from srswti_axis import SRSWTISentimentAnalyzer
    
    analyzer = SRSWTISentimentAnalyzer()
    results = analyzer.analyze(text, aspects=['product', 'service'])""")
    
    # Translation Example
    print("\n3. Multilingual Translation:")
    print("""    from srswti_axis import SRSWTIMultilingualTranslator
    
    translator = SRSWTIMultilingualTranslator()
    result = translator.translate_text(text, "English", "French")""")
    
    # Summarization Example
    print("\n4. Text Summarization:")
    print("""    from srswti_axis import SRSWTISummarizer, SRSWTISummaryConfig
    
    config = SRSWTISummaryConfig(model_type="lightweight")
    summarizer = SRSWTISummarizer(config)
    summary = summarizer.summarize(text)""")

    print("\n📚 Resources & Support:")
    print("=" * 50)
    print("• website: https://www.srswti.com")
    print("• documentation: https://docs.srswti.com")
    print("• twitter: https://x.com/srswti_ai") 
    print("• support: team@srswti.com")
    
    print("\n Optimization Tips:")
    print("=" * 50)
    print("• Use GPU acceleration when available")
    print("• Enable model caching for repeated operations")
    print("• Batch process for better performance")
    print("• Check documentation for domain-specific tuning")
    

    print_banner()

def main():
    # Your post-install logic here
    print("Running post-install script...")
    install_spacy_model()
    post_install()

if __name__ == "__main__":
    main()
