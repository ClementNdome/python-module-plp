# file_handling.py
# File Handling and Exception Handling Assignment
# This script reads a file, writes a modified version to a new file,
# and also allows the user to input a filename to read with error handling.

def file_read_write_challenge():
    try:
        # Open the original file for reading
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File has been modified and saved to output.txt")

    except FileNotFoundError:
        print("⚠️ The file 'input.txt' was not found.")
    except PermissionError:
        print("⚠️ You don’t have permission to read/write the file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


def error_handling_lab():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, "r") as file:
            print("\n📄 File Content:\n")
            print(file.read())
    except FileNotFoundError:
        print("⚠️ File not found! Please check the name and try again.")
    except PermissionError:
        print("⚠️ You do not have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("Running File Read & Write Challenge...")
    file_read_write_challenge()
    print("\nRunning Error Handling Lab...")
    error_handling_lab()
