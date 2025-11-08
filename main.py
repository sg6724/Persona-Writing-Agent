
import dspy
from src.config import Config
from src.data_preparation import DataPreparation
from src.optimizer import PersonaOptimizer
from src.generator import PostGenerator

def main():
    print("\n" + "="*70)
    print("AMAN GUPTA PERSONA-BASED LINKEDIN WRITING AGENT")
    print("="*70)
    
    # 1. Validate Configuration
    print("\nLOADING CONFIGURATION...")
    try:
        Config.validate()
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # 2. Setup DSPy with Gemini
    print("\nSETTING UP DSPy...")
    lm = dspy.LM(Config.MODEL_NAME, api_key=Config.GEMINI_API_KEY)
    dspy.configure(lm=lm)
    print(f"✓ Configured: {Config.MODEL_NAME}")
    
    # 3. Load Training Data
    print("\nLOADING TRAINING DATA...")
    data_prep = DataPreparation()
    training_data = data_prep.load_training_data(f"{Config.DATA_DIR}/training.json")
    data_prep.verify_data(training_data)
    
    # 4. Prepare DSPy Examples
    print("\nPREPARING DSPy EXAMPLES...")
    trainset = data_prep.convert_to_dspy_examples(training_data)
    print(f"✓ Prepared {len(trainset)} DSPy examples\n")
    
    # 5. Optimize with DSPy
    print("\nOPTIMIZING PERSONA ENGINE...")
    optimizer = PersonaOptimizer()
    optimized_writer = optimizer.compile(trainset)
    
    # 6. Initialize Generator
    print("\nINITIALIZING POST GENERATOR...")
    generator = PostGenerator(optimized_writer)
    print("✓ Post generator ready\n")
    
    # 7. Interactive Mode
    print("\n" + "="*70)
    print("READY TO GENERATE POSTS")
    print("="*70)
    print("\nEnter content bullets to generate a post in Aman Gupta's style.")
    print("Type 'quit' to exit, 'memory' to see saved posts.\n")
    
    while True:
        print("-" * 70)
        bullets = input("📝 Enter Persona's content bullets (or command): ").strip()
        
        if bullets.lower() == 'quit':
            print("👋 Thank you for using Aman Gupta Persona Writer!")
            break
        
        if bullets.lower() == 'memory':
            memory = generator.load_memory()
            if memory:
                print(f"\n Saved {len(memory)} posts:")
                for i, item in enumerate(memory[-5:], 1):  # Show last 5
                    print(f"  {i}. {item['bullets'][:50]}...")
            else:
                print("  (No saved posts yet)")
            continue
        
        if not bullets:
            print("⚠️  Please enter some content bullets.")
            continue
        
        print("\n⏳ Generating post...")
        try:
            post = generator.generate(bullets)
            
            print("\n" + "="*70)
            print("✨ GENERATED POST:")
            print("="*70)
            print(post)
            print("="*70)
            
            save = input("\n💾 Save to memory? (y/n): ").strip().lower()
            if save == 'y' or save == 'yes' or save == 'Y':
                generator.save_to_memory(post, bullets)
                print("✓ Post saved!")
        
        except Exception as e:
            print(f"Error generating post: {e}")

if __name__ == "__main__":
    main()
