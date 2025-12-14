# run.py

import os
from dotenv import load_dotenv
from agent.core import SimpleAgent

# Load environment variables from .env file
load_dotenv()

def main():
    """Main function to configure and run the simple agent."""
    
    # Check for API Key
    if not os.getenv("GEMINI_API_KEY"):
        print("FATAL ERROR: GEMINI_API_KEY environment variable not found.")
        print("Please check your .env file.")
        return

    # Initialize the agent
    agent = SimpleAgent()

    # --- Test Case 1: Simple Knowledge (No Tool Needed) ---
    print("\n" + "="*70)
    response_1 = agent.run_query("What is the largest planet in our solar system?")
    print(response_1)

    # --- Test Case 2: Requires Tool Use (Current Data) ---
    print("\n" + "="*70)
    query_2 = "What were the winning team and score of the most recent Formula 1 Grand Prix?"
    response_2 = agent.run_query(query_2)
    print(response_2)
    
    print("\n" + "="*70)

if __name__ == "__main__":
    main()
