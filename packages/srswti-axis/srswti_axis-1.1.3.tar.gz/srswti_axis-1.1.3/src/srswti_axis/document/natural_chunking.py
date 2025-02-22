from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass
import nltk
from nltk import RegexpParser, Tree
from nltk.chunk import ne_chunk
import json
from collections import defaultdict

import json

@dataclass
class SRSWTIChunk:
    """Data class for chunk information"""
    text: str
    type: str
    level: int
    start: int
    end: int
    sub_chunks: List['SRSWTIChunk']
    grammatical_role: Optional[str] = None

    def to_dict(self):
        """Convert chunk to a dictionary for JSON serialization"""
        return {
            'text': self.text,
            'type': self.type,
            'level': self.level,
            'start': self.start,
            'end': self.end,
            'sub_chunks': [chunk.to_dict() for chunk in self.sub_chunks],
            'grammatical_role': self.grammatical_role
        }

@dataclass
class SRSWTIPhrase:
    """Data class for phrase information"""
    text: str
    type: str
    head_word: str
    modifiers: List[str]
    dependencies: List[str]

class SRSWTIChunkAnalyzer:
    """Advanced chunking and phrase analysis using NLTK"""
    
    def __init__(self):
        # Enhanced grammar patterns
        self.grammar = r"""
            # Noun phrase patterns
            NP:
                {<DT|PRP\$>?<JJ.*>*<NN.*>+}  # Basic NP
                {<NNP>+}                      # Proper nouns
                {<PRP>}                       # Pronouns
                
            # Verb phrase patterns
            VP:
                {<MD>?<VB.*><NP|PP>*}        # Verb with optional object
                {<VBG><NP>}                   # Gerund phrases
                
            # Prepositional phrase
            PP:
                {<IN><NP>}                    # Basic PP
                {<TO><NP>}                    # To-phrases
                
            # Adjective phrase
            ADJP:
                {<RB.*>?<JJ.*>}              # Adjectives with optional adverbs
                {<JJR><IN>}                   # Comparative
                
            # Adverb phrase
            ADVP:
                {<RB.*>+}                     # Multiple adverbs
                
            # Clause patterns
            CLAUSE:
                {<NP><VP>}                    # Basic clause
        """
        self.chunk_parser = RegexpParser(self.grammar)
    @staticmethod
    def print_pos_tag_legend():
        """
        Print a formatted legend of Part-of-Speech tags
        """
        print("\n=== POS TAG LEGEND ===")
        legend = SRSWTIChunkAnalyzer.get_pos_tag_legend()
        
        # Sort tags for better readability
        sorted_tags = sorted(legend.items())
        
        for tag, description in sorted_tags:
            print(f"{tag:<5} : {description}")

    @staticmethod
    def get_grammar_pattern_legend() -> Dict[str, str]:
        """
        Generate a legend explaining the chunking grammar patterns
        
        Returns:
            Dictionary of grammar patterns with their descriptions
        """
        return {
            # Noun Phrase (NP) Patterns
            'NP Pattern 1': '{<DT|PRP$>?<JJ.*>*<NN.*>+} - Basic Noun Phrase\n'
                            '  - Optional determiner or possessive pronoun\n'
                            '  - Zero or more adjectives\n'
                            '  - One or more nouns',
            
            'NP Pattern 2': '{<NNP>+} - Proper Noun Phrase\n'
                            '  - One or more proper nouns',
            
            'NP Pattern 3': '{<PRP>} - Pronoun Phrase\n'
                            '  - Single personal pronoun',
            
            # Verb Phrase (VP) Patterns
            'VP Pattern 1': '{<MD>?<VB.*><NP|PP>*} - Verb Phrase with Optional Object\n'
                            '  - Optional modal verb\n'
                            '  - Any verb form\n'
                            '  - Optional noun or prepositional phrases',
            
            'VP Pattern 2': '{<VBG><NP>} - Gerund Phrase\n'
                            '  - Gerund verb\n'
                            '  - Followed by a noun phrase',
            
            # Prepositional Phrase (PP) Patterns
            'PP Pattern 1': '{<IN><NP>} - Basic Prepositional Phrase\n'
                            '  - Preposition\n'
                            '  - Followed by a noun phrase',
            
            'PP Pattern 2': '{<TO><NP>} - To-Phrase\n'
                            '  - "to" preposition\n'
                            '  - Followed by a noun phrase',
            
            # Adjective Phrase (ADJP) Patterns
            'ADJP Pattern 1': '{<RB.*>?<JJ.*>} - Adjective Phrase\n'
                            '  - Optional adverb\n'
                            '  - Adjective',
            
            'ADJP Pattern 2': '{<JJR><IN>} - Comparative Adjective Phrase\n'
                            '  - Comparative adjective\n'
                            '  - Followed by a preposition',
            
            # Adverb Phrase (ADVP) Pattern
            'ADVP Pattern': '{<RB.*>+} - Adverb Phrase\n'
                            '  - One or more adverbs',
            
            # Clause Pattern
            'Clause Pattern': '{<NP><VP>} - Basic Clause\n'
                            '  - Noun phrase (subject)\n'
                            '  - Verb phrase (predicate)'
        }

    def print_grammar_legend(self):
        """
        Print a formatted legend of grammar patterns
        """
        print("\n=== GRAMMAR PATTERN LEGEND ===")
        legend = self.get_grammar_pattern_legend()
        
        # Sort patterns for better readability
        sorted_patterns = sorted(legend.items())
        
        for pattern, description in sorted_patterns:
            print(f"\n{pattern}:")
            print(description)

    @staticmethod
    def get_pos_tag_legend() -> Dict[str, str]:
        """
        Generate a comprehensive legend of Part-of-Speech (POS) tags
        
        Returns:
            Dictionary of POS tags with their descriptions
        """
        return {
            # Determiners and Pronouns
            'DT': 'Determiner (e.g., the, a, an, these)',
            'PRP': 'Personal Pronoun (e.g., I, you, he, she, it)',
            'PRP$': 'Possessive Pronoun (e.g., my, your, his, her)',
            
            # Nouns
            'NN': 'Noun, singular or mass (e.g., dog, cat, tree)',
            'NNS': 'Noun, plural (e.g., dogs, cats, trees)',
            'NNP': 'Proper Noun, singular (e.g., John, London, NASA)',
            'NNPS': 'Proper Noun, plural (e.g., Americans, Andes)',
            
            # Verbs
            'VB': 'Verb, base form (e.g., eat, go, take)',
            'VBD': 'Verb, past tense (e.g., ate, went, took)',
            'VBG': 'Verb, gerund/present participle (e.g., eating, going)',
            'VBN': 'Verb, past participle (e.g., eaten, gone)',
            'VBP': 'Verb, non-3rd person singular present (e.g., am, are, eat)',
            'VBZ': 'Verb, 3rd person singular present (e.g., is, has, eats)',
            'MD': 'Modal verb (e.g., can, could, will, would)',
            
            # Adjectives
            'JJ': 'Adjective (e.g., big, old, green)',
            'JJR': 'Adjective, comparative (e.g., bigger, older)',
            'JJS': 'Adjective, superlative (e.g., biggest, oldest)',
            
            # Adverbs
            'RB': 'Adverb (e.g., quickly, very, always)',
            'RBR': 'Adverb, comparative (e.g., faster, more quickly)',
            'RBS': 'Adverb, superlative (e.g., fastest, most quickly)',
            
            # Prepositions and Conjunctions
            'IN': 'Preposition or Subordinating Conjunction (e.g., in, of, like, after, while)',
            'TO': 'to (preposition/infinitive marker)',
            
            # Punctuation
            ',': 'Comma',
            '.': 'Period',
        }

    def visualize_tree(self, tree: Tree, indent: str = '', last: bool = True) -> str:
        """
        Create ASCII visualization of parse tree
        
        Args:
            tree: NLTK Tree object
            indent: Current indentation
            last: Whether this is the last child
            
        Returns:
            String representation of ASCII tree
        """
        tree_str = ''
        
        # Add node connector
        if indent:
            tree_str += indent[:-3] + ('└── ' if last else '├── ')
        
        # Add node content
        if isinstance(tree, Tree):
            tree_str += str(tree.label()) + '\n'
            
            # Calculate indentation for children
            child_indent = indent + ('    ' if last else '│   ')
            
            # Process children
            children = list(tree)
            for i, child in enumerate(children):
                tree_str += self.visualize_tree(
                    child,
                    child_indent,
                    i == len(children) - 1
                )
        else:
            tree_str += str(tree) + '\n'
        
        return tree_str

        
    def analyze_text(self, text: str, use_rich: bool = False) -> Dict:
        """
        Perform comprehensive chunking analysis
        
        Args:
            text: Input text to analyze
            use_rich: Whether to use rich library for visualization
            
        Returns:
            Dict containing structured chunk analysis
        """
        # Sentence tokenization
        sentences = nltk.sent_tokenize(text)
        
        if use_rich:
            try:
                from rich import print as rprint
                from rich.tree import Tree as RichTree
                
                print("\nRich Tree Visualization:")
                for sentence in sentences:
                    tokens = nltk.word_tokenize(sentence)
                    tagged = nltk.pos_tag(tokens)
                    chunked = self.chunk_parser.parse(tagged)
                    rich_tree = self._create_rich_tree(chunked)
                    print(f"\nSentence: {sentence.strip()}")
                    rprint(rich_tree)
                return {}  # Return empty dict when just visualizing
            except ImportError:
                print("Please install rich library: pip install rich")
                return {}
        
        analysis_results = {
            'overall_stats': {
                'sentence_count': len(sentences),
                'total_chunks': 0,
                'chunk_distribution': defaultdict(int)
            },
            'sentence_analysis': [],
            'phrase_patterns': defaultdict(list),
            'hierarchical_structure': [],
            'tree_visualizations': []
        }
        
        # Analyze each sentence
        for sentence in sentences:
            sentence_analysis = self._analyze_sentence(sentence)
            analysis_results['sentence_analysis'].append(sentence_analysis)
            
            # Update overall statistics
            analysis_results['overall_stats']['total_chunks'] += \
                sentence_analysis['chunk_count']
            
            for chunk_type, count in sentence_analysis['chunk_distribution'].items():
                analysis_results['overall_stats']['chunk_distribution'][chunk_type] += count
            
            # Collect phrase patterns
            for pattern in sentence_analysis['patterns']:
                analysis_results['phrase_patterns'][pattern['type']].append(pattern)
            
            # Add hierarchical structure
            analysis_results['hierarchical_structure'].append({
                'sentence': sentence,
                'tree': sentence_analysis['tree_structure']
            })
            
            # Add ASCII tree visualization
            tokens = nltk.word_tokenize(sentence)
            tagged = nltk.pos_tag(tokens)
            chunked = self.chunk_parser.parse(tagged)
            tree_viz = {
                'sentence': sentence,
                'ascii_tree': self.visualize_tree(chunked)
            }
            analysis_results['tree_visualizations'].append(tree_viz)
        
        # Add summary
        analysis_results['summary'] = self._generate_summary(analysis_results)
        
        return analysis_results

    def _create_rich_tree(self, nltk_tree: Tree) -> 'RichTree':
        """Create a rich tree visualization"""
        from rich.tree import Tree as RichTree
        
        if isinstance(nltk_tree, Tree):
            # Create node with phrase type label
            rich_tree = RichTree(f"[bold blue]{nltk_tree.label()}[/]")
            
            # Add all children
            for child in nltk_tree:
                rich_tree.add(self._create_rich_tree(child))
            
            return rich_tree
        else:
            # Create leaf node with word and its POS tag
            return RichTree(f"[green]{nltk_tree[0]}[/] [yellow]({nltk_tree[1]})[/]")
    
    def _analyze_sentence(self, sentence: str) -> Dict:
        """Analyze individual sentence structure"""
        # Tokenize and tag
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        
        # Get chunks
        chunked = self.chunk_parser.parse(tagged)
        named_entities = ne_chunk(tagged)
        
        # Extract chunks and patterns
        chunks = self._extract_chunks(chunked)
        patterns = self._extract_patterns(chunked)
        
        # Count chunk types
        chunk_distribution = defaultdict(int)
        for chunk in chunks:
            chunk_distribution[chunk.type] += 1
        
        return {
            'sentence': sentence,
            'chunks': [chunk.__dict__ for chunk in chunks],
            'patterns': patterns,
            'chunk_count': len(chunks),
            'chunk_distribution': dict(chunk_distribution),
            'tree_structure': self._tree_to_dict(chunked),
            'named_entities': self._extract_named_entities(named_entities)
        }
    
    def _extract_chunks(self, tree: Tree) -> List[SRSWTIChunk]:
        """Extract chunks from parse tree"""
        chunks = []
        
        for subtree in tree.subtrees():
            if isinstance(subtree, Tree):  # Only process Tree instances
                # Extract chunk text
                chunk_text = ' '.join(word for word, tag in subtree.leaves())
                
                # Get chunk position
                start = 0  # Would calculate actual position
                end = len(chunk_text)
                
                # Create sub-chunks recursively
                sub_chunks = []
                for child in subtree:
                    if isinstance(child, Tree):
                        sub_chunk_text = ' '.join(word for word, tag in child.leaves())
                        sub_chunks.append(SRSWTIChunk(
                            text=sub_chunk_text,
                            type=child.label(),
                            level=subtree.height() - 1,
                            start=0,  # Would calculate actual position
                            end=len(sub_chunk_text),
                            sub_chunks=[],
                            grammatical_role=self._determine_grammatical_role(child)
                        ))
                
                chunks.append(SRSWTIChunk(
                    text=chunk_text,
                    type=subtree.label(),
                    level=subtree.height(),
                    start=start,
                    end=end,
                    sub_chunks=sub_chunks,
                    grammatical_role=self._determine_grammatical_role(subtree)
                ))
        
        return chunks
    
    def _extract_patterns(self, tree: Tree) -> List[Dict]:
        """Extract recurring patterns from parse tree"""
        patterns = []
        
        for subtree in tree.subtrees():
            if isinstance(subtree, Tree):
                pattern = {
                    'type': subtree.label(),
                    'structure': ' '.join(tag for word, tag in subtree.leaves()),
                    'text': ' '.join(word for word, tag in subtree.leaves()),
                    'length': len(subtree.leaves())
                }
                patterns.append(pattern)
        
        return patterns
    
    def _determine_grammatical_role(self, tree: Tree) -> Optional[str]:
        """Determine grammatical role of chunk"""
        if not isinstance(tree, Tree):
            return None
            
        label = tree.label()
        parent = tree.parent() if hasattr(tree, 'parent') else None
        
        if label == 'NP':
            if parent and parent.label() == 'S':
                return 'subject'
            elif parent and parent.label() == 'VP':
                return 'object'
        elif label == 'VP':
            return 'predicate'
        elif label == 'PP':
            return 'modifier'
            
        return None
    
    def _extract_named_entities(self, ne_tree: Tree) -> List[Dict]:
        """Extract named entities from NE chunk tree"""
        named_entities = []
        
        for chunk in ne_tree:
            if isinstance(chunk, Tree):
                entity_text = ' '.join(word for word, tag in chunk.leaves())
                named_entities.append({
                    'text': entity_text,
                    'type': chunk.label(),
                    'confidence': 0.85  # Example confidence score
                })
        
        return named_entities
    
    def _tree_to_dict(self, tree: Tree) -> Dict:
        """Convert NLTK tree to dictionary representation"""
        if not isinstance(tree, Tree):
            return str(tree)
            
        return {
            'node': tree.label(),
            'children': [self._tree_to_dict(child) for child in tree]
        }
    
    def _generate_summary(self, results: Dict) -> str:
        """Generate natural language summary of analysis"""
        total_chunks = results['overall_stats']['total_chunks']
        sentence_count = results['overall_stats']['sentence_count']
        chunk_dist = results['overall_stats']['chunk_distribution']
        
        # Calculate most common chunk type
        most_common = max(chunk_dist.items(), key=lambda x: x[1])
        
        summary = (
            f"Analysis found {total_chunks} chunks across {sentence_count} sentences. "
            f"The most common chunk type is {most_common[0]} with {most_common[1]} occurrences. "
            f"Average chunks per sentence: {total_chunks/sentence_count:.1f}."
        )
        
        return summary
    
    

def main():
    # Example usage
    analyzer = SRSWTIChunkAnalyzer()
    
    # Print POS tag legend
    SRSWTIChunkAnalyzer.print_pos_tag_legend()
    
    # Print grammar pattern legend
    analyzer.print_grammar_legend()
    
    text = """
    The experienced data scientist RohIT Tiwari quickly analyzed the complex dataset. 
    She discovered several interesting patterns in the neural network's behavior. 
    The advanced AI model, despite its limitations, performed exceptionally well on the test cases.
    """
    
    results = analyzer.analyze_text(text)
    
    # Convert chunks to dictionaries
    for sentence_analysis in results['sentence_analysis']:
        sentence_analysis['chunks'] = [chunk.to_dict() for chunk in 
            [SRSWTIChunk(**chunk) for chunk in sentence_analysis['chunks']]]
    
    # Print structured analysis
    print("\n=== STRUCTURED ANALYSIS ===")
    print(json.dumps(results, indent=2))
    
    # Print tree visualizations
    print("\n=== PARSE TREES ===")
    for viz in results['tree_visualizations']:
        print("\nSentence:", viz['sentence'].strip())
        print("-" * 80)
        print(viz['ascii_tree'])
        print("-" * 80)
    
    # Optional: Print colorful trees if rich is installed
    try:
        from rich import print as rprint
        print("\n=== COLORFUL PARSE TREES ===")
        analyzer.analyze_text(text, use_rich=True)
    except ImportError:
        print("\nInstall 'rich' package for colorful tree visualization:")
        print("pip install rich")

if __name__ == "__main__":
    main()