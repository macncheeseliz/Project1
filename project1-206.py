import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
	inFile = open(file, "r")
	lines = inFile.readlines()
	inFile.close()

	list1 = []

	for line in lines[1:]:
		fileDict = {}

		values = line.split(",")
		First = values[0]
		Last = values[1]
		Email = values[2]
		yearclass = values[3]
		dob = values[4]

		#setting up dictionary
		fileDict["First"] = First
		fileDict["Last"] = Last
		fileDict["Email"] = Email
		fileDict["Class"] = yearclass
		fileDict["DOB"] = dob
		list1.append(fileDict)

	return list1


# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows


def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	sortedList = sorted(data, key=lambda b: b[col])
	return sortedList[0]['First']+ " " + sortedList[0]['Last']



def classSizes(data):
# Create a histogram
# Input: list of dictionaries
	#use for loop to create counter
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	freshman = 0
	sophomore = 0
	junior = 0
	senior = 0

	for students in data:
		if students["Class"] == "Freshman":
			freshman += 1
		elif students["Class"] == "Sophomore":
			sophomore += 1
		elif students["Class"] == "Junior":
			junior += 1
		elif students["Class"] == "Senior":
			senior +=1

	numstudents = [('Senior', senior), ('Junior', junior), ('Freshman', freshman), ('Sophomore', sophomore)]
	return sorted(numstudents, key = lambda x: x[1], reverse = True)


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	january = 0
	february = 0
	march = 0
	april = 0
	may = 0
	june = 0
	july = 0
	august = 0
	september = 0
	october = 0
	november = 0
	december = 0


	for bday in a:
		month = bday["DOB"].split("/")[0]
		if month == "1":
			january += 1
		if month == "2":
			february += 1
		if month == "3":
			march += 1
		if month == "4":
			april += 1
		if month == "5":
			may += 1
		if month == "6":
			june += 1
		if month == "7":
			july += 1
		if month == "8":
			august += 1
		if month == "9":
			september += 1
		if month == "10":
			october += 1
		if month == "11":
			november += 1
		if month == "12":
			december += 1

	birthmonth = [('1', january), ('2', february), ('3', march), ('4', april), ('5', may), ('6', june), ('7', july), ('8', august), ('9', september), ('10', october), ('11', november), ('12', december)]
	return int(sorted(birthmonth, key = lambda x: (x[1], x[0]), reverse = True)[0][0])


def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as first,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	sortedList = sorted(a, key=lambda b: b[col])
	with open(fileName, 'w') as x:
		for data1 in sortedList:
			print(data1['First'] + ',' + data1['Last'] + ',' + data1['Email'], file = x)
			

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
