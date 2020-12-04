def main():
    #Open File
    gradesFile = {}

    try:
        gradesFile = open('Final.txt', 'r')
    except FileNotFoundError:
        print("Error: Could not find scores file, please check that it exists in the current directory")
        exit()

    tempList = [line.rstrip() for line in gradesFile]
    gradesList = [int(i) for i in tempList]

    #Number of scores
    listLength = len(gradesList)
    #Protect against ZeroDivisionError
    if listLength > 0:
        print("Number of Grades:", listLength)

        #Average
        gradesSum = sum(gradesList)
        average = gradesSum / listLength
        print(("Average Grade: {0:.2f}").format(average))

        calculate_percent_above_average(gradesList, listLength, average)
    else:
        print("Error: Scores file must not be empty.")
        exit()

def calculate_percent_above_average(gradesList, listLength, average):
    counter = 0
    for i, val in enumerate(gradesList):
        if val > average:
            counter += 1
    
    percentAbove = counter/listLength
    print(("Percent of grades above the average: {0:.2%}").format(percentAbove))

main()