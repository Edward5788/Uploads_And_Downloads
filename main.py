from titleUnderliner import titleUnderliner
import time


def GigsToTime():

    titleName = "Gigabytes and Mb/s To Time Converter"  # Outputting the title
    titleUnderlineObject = "-"
    titleUnderliner(titleName, titleUnderlineObject)

    totalGigsInputComplete = False  # Getting amount of gigs
    while totalGigsInputComplete == False:

        try:
            amountOfGB = float(
                input("Enter total gigs the download is (e.g 900): "))

            # Validating if they've entered a password length graeter than 0
            if float(amountOfGB) >= 1:
                totalGigsInputComplete = True

            else:  # IF the input is not greater than 0
                print(
                    "Invalid input, please enter a number greater than 0")
                # Waits a short amount of time to add smoothness to the program
                time.sleep(0.1)

        except:  # Error code for if the program fails
            print("Invalid input, enter only a number, try again")
            time.sleep(0.1)

    megsPerSecondInputComplete = False  # Getting amount of gigs
    while megsPerSecondInputComplete == False:

        try:
            megsPerSecond = float(
                input("Enter how many megs per second your downloading it at: "))

            # Validating if they've entered a password length graeter than 0
            if float(megsPerSecond) >= 1:
                megsPerSecondInputComplete = True

            else:  # IF the input is not greater than 0
                print(
                    "Invalid input, please enter a number greater than 0")
                # Waits a short amount of time to add smoothness to the program
                time.sleep(0.1)

        except:  # Error code for if the program fails
            print("Invalid input, enter only a number, try again")
            time.sleep(0.1)

    # Convert gb to mb
    amountOfGB = amountOfGB * 1000
    # Diving to get the number of seconds it will be
    totalSeconds = amountOfGB / megsPerSecond

    totalHours = totalSeconds / 60  # Converting to hours

    totalMinutes = totalHours / 60  # Converting to minutes

    print("\n\nIt wil take " +
          str("{:,}".format(round(totalSeconds))) + " seconds to download it")
    print("\nOr it will take " +
          str("{:,}".format(round(totalHours))) + " minutes to download it")
    print("\nOr it will take " +
          str("{:,}".format(round(totalMinutes))) + " hours to download it")

    print("\n\n\n")
    GigsToTime()  # Starts program again


GigsToTime()  # Calling main program
