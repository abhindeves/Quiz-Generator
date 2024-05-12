import os
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# create the client object wit client(api_key)

class TestGenerator():
    
    def __init__(self,topic, num_of_questions, num_of_possible_answers):
        self.topic = topic
        self.num_of_questions = num_of_questions
        self.num_of_possible_answers = num_of_possible_answers
        
        if self.num_of_questions > 15:
            raise ValueError("More than 15 Questions is Not possible at thes moment!!")
        
        
        
    def create_test_prompt(self):
        
        prompt = f"""Create a multiple-choice quiz on the topic of {self.topic}. The quizz should contain {self.num_of_questions} questions. 
    Each question should have {self.num_of_possible_answers} as options. Include the Correct answer after every question.
    Only Include question which are based on Actual Facts. Questions should be PHD Level.
    Explore many different subtopics from the {self.topic}.
    
    
                    
    Example: 1

    1. Which of the following statements about quantum entanglement is true?
    a) Entanglement can be explained solely through classical mechanics.
    b) Entanglement is a phenomenon only observed at the macroscopic level.
    c) Entanglement violates the principle of locality.
    d) Entanglement occurs only between particles with opposite spin.
    
    
    Answer: c) Entanglement violates the principle of locality.
    
    
    Example: 2
    
    2. What is the primary function of microRNAs (miRNAs) in gene expression regulation?
    a) Promote translation of mRNA into protein.
    b) Inhibit transcription of DNA into mRNA.
    c) Degrade mRNA molecules.
    d) Inhibit translation of mRNA into protein.
    
    
    Answer: d) Inhibit translation of mRNA into protein.
    
    
    Example: 3
    
    3. Computer Science:In the context of machine learning, what does the term "overfitting" refer to?
    a) The model's inability to capture the underlying trend in the data.
    b) The model performing well on the training data but poorly on unseen data.
    c) The model's underestimation of the complexity of the data.
    d) The model's tendency to generalize well to unseen data.


    Answer: b) The model performing well on the training data but poorly on unseen data.
    
    
    """
        return prompt
    
        
    def generate_quizz(self,prompt):
        response = client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages=[
                {
                    "role":"system","content":"""You're an experienced quizmaster tasked with crafting questions and answers 
                    tailored to the user's specifications.
                    """,
                    "role":"user","content":f"{prompt}"
                }
            ],
            temperature = 0.8
            
        )
        return response.choices[0].message.content
    
    def run(self):
        p = self.create_test_prompt()
        r = self.generate_quizz(p)
        return r
        
        
# if __name__ == '__main__':
#     gen = TestGenerator("Python",5,1)
#     response = gen.run()
#     print(response)
    