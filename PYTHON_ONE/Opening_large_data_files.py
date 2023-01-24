# Topic: Humaan Resource system
# Download the file and save it to your computer. In VS Code, open 
# the folder that contains this file. Then, create a new python script
# in that folder

with open("life-expectancy.csv") as life_expectancy_files:

    for data in life_expectancy_files:
        data = data.strip()
        # print(data)

        parts = data.split(",")

        country = parts[0]
        code = parts[1]
        year = parts[2]
        life_expectancy = parts[3]

        print(f"Entity: {country} - Code: {code} - Year: {year} - Life Expectancy: {life_expectancy} ") 
