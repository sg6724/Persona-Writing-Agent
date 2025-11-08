
import json
from datetime import datetime
from src.config import Config
import os

class PostGenerator:
    """Generate and manage LinkedIn posts"""
    
    def __init__(self, optimized_writer):
        self.writer = optimized_writer
        self.config = Config()
        self.memory_file = f"{self.config.DATA_DIR}/memory.json"
        self._ensure_memory_file()
    
    def _ensure_memory_file(self):
        """Create memory file if it doesn't exist"""
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, 'w') as f:
                json.dump([], f)
    
    def generate(self, content_bullets: str) -> str:
        """Generate a LinkedIn post"""
        result = self.writer.forward(
            person_name=self.config.PERSON_NAME,
            person_title=self.config.PERSON_TITLE,
            company=self.config.COMPANY,
            content_bullets=content_bullets
        )
        return result.post
    
    def save_to_memory(self, post: str, bullets: str):
        """Save generated post to memory"""
        memory = self.load_memory()
        
        memory.append({
            'post': post,
            'bullets': bullets,
            'timestamp': datetime.now().isoformat()
        })
        
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(memory, f, indent=2, ensure_ascii=False)
    
    def load_memory(self):
        """Load previous posts from memory"""
        try:
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
