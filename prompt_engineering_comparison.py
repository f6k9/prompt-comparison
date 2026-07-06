import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def main():
    client = Groq()
    
    # 1. Define your 5 hardcoded prompts in a list
    esp32_prompts = [
        "Give me some cool ESP32 project ideas.",
        
        "Act as an embedded systems expert. Give me a list of 5 intermediate-level ESP32 project ideas that utilize both its Wi-Fi and Bluetooth capabilities. Include a brief description of what each project does.",
        
        "I want to build a practical hardware project using an ESP32 development board. Provide 3 comprehensive project concepts focused on home automation or IoT. For each project, please include: a descriptive title, required hardware components, software libraries needed, and potential real-world challenges.",
        
        "Imagine it's the year 2045, and the ESP32 is considered vintage tech, but a global power grid failure means we have to rely on low-power mesh networks to survive. Brainstorm 3 sci-fi, 'cyberpunk-survivalist' project ideas that a hobbyist could build using an ESP32 to help their local community. Give them gritty, creative names.",
        
        "Generate 3 ESP32 project ideas under the following strict constraints: 1. Must use a camera module or NFC/RFID module, but CANNOT use an SD card reader. 2. Must operate entirely on a local network (LAN) with no external cloud APIs. 3. Output the results in a Markdown table with columns: Project Name, Primary Sensor/Module, and Local Data Handling Method. Do not write any introductory or concluding text."
    ]
    
    print("Processing Prompts with Llama 3.1...\n")
    print("=" * 60 + "\n")
    
    # 2. Loop through each prompt
    for index, prompt in enumerate(esp32_prompts, 1):
        print(f"--- Running Prompt {index} ---")
        print(f"Prompt Sent: {prompt}\n")
        
        # Fresh history window for EACH prompt so they don't bleed into one another
        history = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
        
        # Append the specific prompt
        history.append({"role": "user", "content": prompt})
        
        # Pass to the API
        try:
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=history,
                temperature=0.7 # Bumped slightly from 0.0 to let the creative prompts shine!
            )
            
            bot_response = completion.choices[0].message.content
            print(f"Llama Response:\n{bot_response}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            
        print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    main()