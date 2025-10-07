def word_counter(file_path):
    try:
        # Open and read file
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()

        # Split into words
        words = content.split()
        word_count = len(words)

        print(f"✅ The file '{file_path}' contains {word_count} words.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


if __name__ == "__main__":
    # Ask user for file input
    file_path = input("Enter the file path: ")
    word_counter(file_path)
