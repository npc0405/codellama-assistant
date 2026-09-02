from assistant import generate_code, explain_code, fix_bug, optimize_code

def read_from_cli(prompt_msg: str) -> str:
    print(prompt_msg + " (type 'END' to finish):")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    while True:
        print("\n===== CodeLlama CLI Assistant =====")
        print("1. Generate code")
        print("2. Explain code")
        print("3. Fix bug")
        print("4. Optimize code")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            description = input("Describe the code you want to generate: ")
            print("\n--- Generated Code ---")
            print(generate_code(description))

        elif choice == "2":
            code = read_from_cli("Paste the code to explain and type 'END' when done")
            print("\n--- Explanation ---")
            print(explain_code(code))

        elif choice == "3":
            code = read_from_cli("Paste the buggy code and type 'END' when done")
            error_message = input("Error message (optional, press Enter to skip): ")
            print("\n--- Fix ---")
            print(fix_bug(code, error_message))

        elif choice == "4":
            code = read_from_cli("Paste the code to optimize and type 'END' when done")
            print("\n--- Optimization ---")
            print(optimize_code(code))

        elif choice == "5":
            print("Thank you, Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()