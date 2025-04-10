import os
from dotenv import load_dotenv
import google.generativeai as genai

def setup_gemini():
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')

class VideoScriptGenerator:
    def __init__(self):
        self.model = setup_gemini()
        self.storytelling_rules = {
            'hook': "Start with a compelling hook within 5 seconds",
            'structure': "Follow problem-solution-call to action format",
            'timing': "Keep total length between 30-60 seconds",
            'engagement': "Include question or challenge for viewer engagement"
        }
    
    def generate_script(self, niche, platform="youtube_shorts"):
        prompt = self._create_prompt(niche, platform)
        response = self.model.generate_content(prompt)
        return response.text
    
    def _create_prompt(self, niche, platform):
        format_length = "30-60 seconds" if platform == "youtube_shorts" else "15-30 seconds"
        return f"""
        Create a compelling short-form video script for {platform} in the {niche} niche.
        
        Requirements:
        - Duration: {format_length}
        - Include a strong hook in the first 5 seconds
        - Follow problem-solution format
        - End with a clear call to action
        - Use conversational tone
        - Make it engaging and shareable
        
        Format the output as:
        HOOK:
        [Hook text]
        
        MAIN CONTENT:
        [Main content text]
        
        CALL TO ACTION:
        [CTA text]
        """

if __name__ == "__main__":
    generator = VideoScriptGenerator()
    script = generator.generate_script("fitness motivation")
    print(script)