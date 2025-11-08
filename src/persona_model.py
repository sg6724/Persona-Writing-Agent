
import dspy

class GenerateLinkedInPost(dspy.Signature):
    """Generate a LinkedIn post in Aman Gupta's specific style"""
    
    person_name = dspy.InputField(desc="Full name of the person")
    person_title = dspy.InputField(desc="Professional title/role")
    company = dspy.InputField(desc="Company name")
    content_bullets = dspy.InputField(
        desc="Key points to cover (2-3 bullet points)"
    )
    post = dspy.OutputField(
        desc="Generated LinkedIn post matching the person's authentic style, tone, and voice"
    )

class PersonaWriter(dspy.Module):
    """DSPy module for persona-based LinkedIn post generation"""
    
    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(GenerateLinkedInPost)
    
    def forward(self, person_name, person_title, company, content_bullets):
        """Generate a post given persona and content details"""
        prediction = self.generate(
            person_name=person_name,
            person_title=person_title,
            company=company,
            content_bullets=content_bullets
        )
        return dspy.Prediction(post=prediction.post)
