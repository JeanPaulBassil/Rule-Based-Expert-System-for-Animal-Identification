# Animal Identification Expert System

## Project Overview
This project is an implementation of an expert system designed for identifying animals based on their characteristics. It utilizes the backward chaining method, starting with a potential conclusion (identifying an animal) and working backward to collect evidence to support that conclusion.

## Key Components
1. **Ask Class (`ask.py`)**: Handles user interactions, presenting questions with predefined choices and capturing responses.
2. **Content Classes (`content.py`)**: Defines logical conditions (`If`, `And`, `Or`) used to determine animal characteristics.
3. **KnowledgeBase Class (`knowledge_base.py`)**: Stores and manages the rules for decision-making, using user responses to navigate through the rules.
4. **Rules Definition (`rules_definition.py`)**: Contains the set of rules guiding the system in identifying animals.
5. **Main Script (`main.py`)**: Entry point for the expert system, initiating the rule-based query and outputting the result.

## Setup
1. Ensure Python is installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.

## How to Run
Execute the script `main.py` in the project's root directory:
```bash
python main.py
```
Follow the on-screen prompts to input characteristics and receive animal identification results.

## System Flow
- The user interacts with the system through a series of questions.
- Responses guide the system through a logical path of rules.
- The system concludes on the animal's identity based on the answers.

## Contributing
Contributions, issues, and feature requests are welcome. 