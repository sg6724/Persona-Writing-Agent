class PersonaEvaluator:
    """Evaluate generated posts for Aman Gupta style match (tone-aware)"""
    
    @staticmethod
    def aman_gupta_style_metric(example, pred, trace=None) -> bool:
        """
        Enhanced metric that handles all 6 tones:
        - Reflective-Inspirational
        - Celebratory-Casual
        - Professional-Factual
        - Reflective-Practical
        - Vulnerable-Inspirational
        - Professional-Strategic
        """
        text = pred.post.lower()
        
        # Core Aman markers (present in all tones)
        has_first_person = any(word in text for word in ['i ', "i'm", 'my ', 'we ', 'me '])
        reasonable_length = 50 < len(pred.post) < 1000
        
        # Tone-flexible markers
        has_energy_or_formality = any(char in pred.post for char in ['!', '?']) or \
                                 any(word in text for word in ['honored', 'strategic', 'promise'])
        
        # Emoji flexibility (not required, but valued)
        has_emoji = any(char in pred.post for char in ['🔥', '💡', '🎧', '🇮🇳', '💪', '🙏', '😊', '✨', '🤖'])
        
        # Style markers that adapt to tone
        has_authentic_voice = any(marker in pred.post for marker in [
            'i realized',      # reflective
            'big applause',    # celebratory
            'we admit',        # factual
            'no suits',        # practical
            'failure teaches', # vulnerable
            'world wants'      # strategic
        ])
        
        # Count criteria: need at least 3/5
        criteria_met = sum([
            has_first_person,
            reasonable_length,
            has_energy_or_formality,
            has_emoji,
            has_authentic_voice
        ])
        
        return criteria_met >= 3
    
    @staticmethod
    def advanced_tone_metric(example, pred, trace=None) -> float:
        """More sophisticated scoring (0-1) for fine-tuning"""
        text = pred.post
        score = 0.0
        
        # First-person perspective (0.2)
        if any(word in text.lower() for word in ['i ', "i'm", 'my ', 'we ']):
            score += 0.2
        
        # Length appropriate (0.2)
        if 100 < len(text) < 700:
            score += 0.2
        
        # Engagement markers - energy or formality (0.2)
        energy_markers = text.count('!') >= 1
        formal_markers = any(word in text.lower() for word in ['honored', 'global', 'innovation'])
        if energy_markers or formal_markers:
            score += 0.2
        
        # Authenticity - specific voice markers (0.2)
        voice_markers = any(phrase in text for phrase in [
            'i realized', 'we admit', 'no suits', 'big applause',
            'failure teaches', 'world wants', 'jai hind'
        ])
        if voice_markers:
            score += 0.2
        
        # Emoji presence (bonus 0.1, not required)
        if any(char in text for char in ['🔥', '💡', '🇮🇳', '💪', '🙏', '😊', '✨']):
            score += 0.1
        
        return min(score, 1.0)
