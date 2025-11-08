
import dspy
from dspy.teleprompt import BootstrapFewShotWithRandomSearch
from src.persona_model import PersonaWriter
from src.evaluator import PersonaEvaluator
from src.config import Config
from typing import List

class PersonaOptimizer:
    """Optimize the persona writer using DSPy"""
    
    def __init__(self):
        self.evaluator = PersonaEvaluator()
        self.config = Config()
    
    def compile(self, trainset: List) -> PersonaWriter:
        """
        Compile optimized persona writer
        
        DSPy Optimizer does:
        1. Try different combinations of few-shot examples
        2. Generate candidate prompts
        3. Evaluate each using the metric
        4. Select the best performing prompt setup
        """
        print("\n" + "="*60)
        print("🚀 Starting DSPy Optimization")
        print("="*60)
        print(f"Training set size: {len(trainset)} posts")
        print(f"Max demos per run: {self.config.MAX_BOOTSTRAPPED_DEMOS}")
        print(f"Candidate programs to try: {self.config.NUM_CANDIDATE_PROGRAMS}")
        
        # Create optimizer 
        optimizer = BootstrapFewShotWithRandomSearch(
            metric=self.evaluator.aman_gupta_style_metric,
            max_bootstrapped_demos=self.config.MAX_BOOTSTRAPPED_DEMOS,
            num_candidate_programs=self.config.NUM_CANDIDATE_PROGRAMS
        )
        
        print("\n⏳ Optimizing... (this may take a few minutes)")
        
        # Compile
        optimized_writer = optimizer.compile(
            PersonaWriter(),
            trainset=trainset
        )
        
        print("\n" + "="*60)
        print("✅ Optimization Complete!")
        print("="*60)
        
        return optimized_writer
