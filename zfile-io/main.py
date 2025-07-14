try:
    with open("kripa.txt", "w+") as file:
        # Read current content (will be empty due to w+)
        read = file.read()
        print("Initial content:", read)

        # Write something
        file.write("\n this is written under the +r sections")

        # Move the pointer back to the beginning
        file.seek(0)

        # Now read again
        print("Content after writing:")
        print(file.read())

except Exception as er:
    print(er)