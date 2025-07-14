def handle(command):
    command = command.lower()
    if 'text' in command or 'message' in command:
        print("Aakash: Simulating sending a text message: 'Hello from Aakash!'")
    elif 'voice' in command:
        print("Aakash: Simulating sending a voice message.")
    elif 'image' in command:
        print("Aakash: Simulating sending an image message.")
    elif 'video' in command:
        print("Aakash: Simulating sending a video message.")
    elif 'call' in command and 'answer' in command:
        print("Aakash: Simulating answering the call.")
    elif 'call' in command and 'reject' in command:
        print("Aakash: Simulating rejecting the call.")
    else:
        print("Aakash: Please specify if you want to send a text, voice, image, or video message, or answer/reject a call.")