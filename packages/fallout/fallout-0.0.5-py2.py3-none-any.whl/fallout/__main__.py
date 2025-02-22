from fallout import Fallout as fa
import sys

def main():
    """
    Interactive console interface for Fallout calculations.
    """

    fallout = fa()
    radioactive_substances = fallout.get_radioactive_substances()
    radioactive_substances_names = list(radioactive_substances)

    print("=" * 50)
    print("Welcome to the Fallout Simulator".center(50))
    print("=" * 50)

    while True:
        print("\nAvailable Radioactive Substances:")
        for idx, substance in enumerate(radioactive_substances_names, start=1):
            print(f"  {idx}. {substance}")
        print("  q. Quit")

        choice = input("\nEnter the number of the radioactive substance (or 'q' to quit): ").strip()
        if choice.lower() == 'q':
            print("Exiting the Fallout Simulator. Goodbye!")
            sys.exit(0)

        try:
            index = int(choice) - 1
            if index < 0 or index >= len(radioactive_substances_names):
                print("Invalid selection. Please choose a valid number from the list.")
                continue
            selected_substance = radioactive_substances_names[index]
        except ValueError:
            print("Invalid input. Please enter a number corresponding to a substance.")
            continue

        # Get gram input
        while True:
            try:
                gram_input = input(f"Enter the amount in grams for {selected_substance}: ").strip()
                gram = float(gram_input)
                if gram <= 0:
                    print("Amount must be a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for grams.")

        # Get number of half-lives
        while True:
            try:
                halflife_input = input("Enter the number of half-lives: ").strip()
                number_of_halflifes = int(halflife_input)
                if number_of_halflifes < 0:
                    print("Number of half-lives cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer value for half-lives.")

        # Computations
        remaining_gram = fallout.calculate_remaining_gram(gram, number_of_halflifes)
        risk, siverts = fallout.calculate_risk(selected_substance, remaining_gram)
        decay_time = fallout.calculate_decay_time(selected_substance, number_of_halflifes)

        # Display results
        print("\n" + "-" * 50)
        print(f"Results for {selected_substance}:")
        print(f"  Remaining mass after decay: {remaining_gram:.2f} grams")
        print(f"  Risk level: {risk}")
        print(f"  Radiation exposure (siverts): {siverts}")
        print(f"  Estimated decay time: {decay_time}")
        print("-" * 50 + "\n")

        # Ask if the user wants to perform another calculation
        retry = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if retry != 'y':
            print("Thank you for using the Fallout Simulator. Goodbye!")
            break

if __name__ == "__main__":
    main()