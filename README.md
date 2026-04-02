# ai_integrated_in_terminal
AI-powered terminal assistant built using API integration. This tool allows users to interact with an AI model directly from the command line to generate responses, automate tasks, and streamline developer workflows.
# AI Terminal Assistant (API Integration)

This project is an AI-powered command-line tool which have in built chat history features that allows users to interact with an AI model directly from the terminal using an API. It helps automate tasks, generate responses, and improve developer productivity without leaving the command line.

## Features

- AI integration using API
- Command-line interface (CLI)
- Real-time response generation
- Lightweight and easy to use
- Secure API key management using environment variables

## Technologies Used

- Python
- REST API
- Command Line Interface (CLI)
- Environment Variables (.env)
- Requests / HTTP libraries

## Project Structure

ai-terminal-assistant/
│
├── main.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore

## Installation

1. Clone the repository:

git clone https://github.com/your-username/ai-terminal-assistant.git

2. Navigate to the project folder:

cd ai-terminal-assistant

3. Install dependencies:

pip install -r requirements.txt

## Setup Environment Variables

Create a `.env` file in the project root directory and add your API key:

API_KEY=your_api_key_here

Note: Do not share your real API key publicly.

## Usage

Run the program from the terminal:

python main.py

Example:

python main.py "Explain Python decorators"

## Example Output

User Input:
Best places to hang out in delhi Top 5 in night

Response:
Bot: Here are the top 5 places to hang out in Delhi at night:

1. **Hauz Khas Village**: Known for its nightlife, bars, clubs, and lounge.
2. **Cyber Hub**: A popular spot with restaurants, cafes, and bars in Gurgaon.
3. **Khan Market**: A high-end shopping area with bars and clubs.
4. **Andaz Delhi**: Features a rooftop bar and lounge with great views of the city.
5. **CP (Connaught Place)**: Known for its nightlife, bars, and pubs, especially on weekend nights.

Please note that these places may change over time.
## Skills Demonstrated

- API Integration
- Python Development
- CLI Tool Development
- Environment Management
- Error Handling

## Future Improvements

- Support multiple AI models
- Add configuration file
- Improve error handling

## Author
NITIN  
Available for freelance projects in Python, APIs, and AI development.
