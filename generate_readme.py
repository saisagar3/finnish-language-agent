import os
from datetime import datetime

class ReadmeGenerator:
    def __init__(self, project_name="Finnish Language AI Agent"):
        self.project_name = project_name
        self.sections = {
            "project_title": project_name,
            "project_description": "An AI-powered conversational agent for learning Finnish language.",
            "features": [
                "Conversational Finnish language learning",
                "Context-aware dialogue generation",
                "Adaptive learning modes"
            ],
            "installation": [
                "Clone the repository",
                "Create virtual environment: `python3 -m venv venv`",
                "Activate virtual environment",
                "Install dependencies: `pip install -r requirements.txt`"
            ],
            "usage":[
                "Run the training script: `python train.py`",
                "Run the conversational agent: `python chatbot.py`",
                "Start conversing in Finnish!"
            ],
            "technologies": [
                "Python",
                "PyTorch",
                "Hugging Face Transformers",
                "Natural Language Processing"
            ],
            "roadmap":[
                "[ ] Corpus data collection",
                "[ ] Initial model training",
                "[ ] Conversational agent development",
                "[ ] Testing and validation"
            ]
        }
        
    def generate_readme(self):
        """
        Generate a comprehensive README.md file for the project.
        """
        readme_content = f"""
        # {self.sections['project_title']}

        ## Description
        {self.sections['project_description']}

        ## Features
        {self.format_list(self.sections['features'])}

        ## Installation
        {self.format_list(self.sections['installation'])}

        ## Usage
        {self.format_list(self.sections['usage'])}

        ## Technologies
        {self.format_list(self.sections['technologies'])}

        ## Project Roadmap
        {self.format_list(self.sections['roadmap'])}

        ## Contributing
        1. Fork the repository
        2. Create your feature branch: `git checkout -b feature/your-feature-name`
        3. Commit your changes: `git commit -am 'Add your commit message'`
        4. Push to the branch: `git push origin feature/your-feature-name`
        5. Submit a pull request

        ## License
        This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

        ## Contact
        Sagar Kachibatla - sagar.kachibatla@gmail.com

        Project Link: [https://github.com/sagarkachibhatla/finnish-language-ai-agent](https://github.com/sagarkachibhatla/finnish-language-ai-agent)

        ## Acknowledgements
        - [Hugging Face](https://huggingface.co/)
        - [TurkuNLP](https://turkunlp.org/)

        *Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
        """
        return readme_content
    
    def format_list(self, items):
        """
        Format a list of items as a markdown list.
        """
        return "\n".join([f"- {item}" for item in items])

    def write_readme(self, output_path="README.md"):
        """
        Write README.md to file
        """
        readme_content = self.generate_readme()
        with open(output_path, "w", encoding='utf-8') as f:
            f.write(readme_content)
        print(f"README.md generated at {output_path}")

if __name__ == "__main__":
    generator = ReadmeGenerator()
    generator.write_readme()