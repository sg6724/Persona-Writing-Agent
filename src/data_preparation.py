
import json
import dspy
from typing import List, Dict

class DataPreparation:
    """Load and prepare training data for DSPy"""
    
    @staticmethod
    def load_training_data(filepath: str) -> List[Dict]:
        """Load training posts from JSON file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['training_posts']
    
    @staticmethod
    def convert_to_dspy_examples(training_data: List[Dict]) -> List:
        """Convert training data to DSPy Examples"""
        trainset = []
        
        for idx, post_data in enumerate(training_data):
            example = dspy.Example(
                person_name=post_data['person_name'],
                person_title=post_data['person_title'],
                company=post_data['company'],
                content_bullets=post_data['content_bullets'],
                post=post_data['post']
            ).with_inputs('person_name', 'person_title', 'company', 'content_bullets')
            
            trainset.append(example)
            print(f"✓ Converted post {idx + 1}")
        
        return trainset
    
    @staticmethod
    def verify_data(training_data: List[Dict]) -> bool:
        """Verify training data quality"""
        print("\n📊 Data Quality Check:")
        print(f"  Total posts: {len(training_data)}")
        
        for idx, post in enumerate(training_data):
            required_fields = ['person_name', 'person_title', 'company', 
                             'content_bullets', 'post']
            
            missing = [f for f in required_fields if f not in post]
            
            if missing:
                print(f"  ❌ Post {idx+1}: Missing {missing}")
                return False
            
            post_length = len(post['post'])
            bullets_length = len(post['content_bullets'])
            
            if post_length < 50:
                print(f"  ⚠️  Post {idx+1}: Very short ({post_length} chars)")
            if bullets_length < 10:
                print(f"  ⚠️  Post {idx+1}: Vague bullets ({bullets_length} chars)")
            
            print(f"  ✓ Post {idx+1}: {post_length} chars, {post['content_bullets'][:30]}...")
        
        print("\n✓ Data quality check complete\n")
        return True
