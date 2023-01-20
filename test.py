import unittest
import main
import pandas as pd


class TestCombined(unittest.TestCase):
    def setUp(self):
        self.data = main.readData()
        self.combinedTable = main.writeData(self.data)
        self.lenghOfTable = len(self.combinedTable.index) - 1 #length of combined table

    
        self.accessoryFile = pd.read_csv('./fixtures/accessories.csv')
        self.clothingFile = pd.read_csv('./fixtures/clothing.csv')
        self.householdCleanersFile = pd.read_csv('./fixtures/household_cleaners.csv')

        self.dic = {'accessories.csv': self.accessoryFile, 'clothing.csv': self.clothingFile, 'household_cleaners.csv': self.householdCleanersFile} #dictionary to hold data from each file
    
    #Testing to make sure the readData function is reading the correct number of files and the correct file names
    def test_readData(self):
        self.assertEqual(len(self.data), 3)
        self.assertEqual(self.data[0][1], 'accessories.csv')
        self.assertEqual(self.data[1][1], 'clothing.csv')
        self.assertEqual(self.data[2][1], 'household_cleaners.csv')


    ###For boundary value analysis testing I have a minimum, minimum plus one, nominal, maximum minus one, and maximum value for each category of data. 
    ###I then make sure that each value is tagged with the correct file name it came from, ensuring the joining of tables worked correctly

    #Testing using boundary value analysis for email values
    def test_writeDataEmail(self):


        minimum = [self.combinedTable.values[0][0], self.combinedTable.values[0][2]]   #[[first value is the row, second value is the column], this value is the file name]]]
        minimumPlusOne = [self.combinedTable.values[1][0], self.combinedTable.values[1][2]]
        nominal = [self.combinedTable.values[self.lenghOfTable // 2][0], self.combinedTable.values[self.lenghOfTable // 2][2]]
        maximumMinusOne = [self.combinedTable.values[self.lenghOfTable - 1][0], self.combinedTable.values[self.lenghOfTable - 1][2]]
        maximum = [self.combinedTable.values[self.lenghOfTable][0], self.combinedTable.values[self.lenghOfTable][2]]

        self.assertIn(minimum[0], self.dic[minimum[1]]['email_hash'].values)
        self.assertIn(minimumPlusOne[0], self.dic[minimumPlusOne[1]]['email_hash'].values)
        self.assertIn(nominal[0], self.dic[nominal[1]]['email_hash'].values)
        self.assertIn(maximumMinusOne[0], self.dic[maximumMinusOne[1]]['email_hash'].values)
        self.assertIn(maximum[0], self.dic[maximum[1]]['email_hash'].values)


    #Testing using boundary value analysis for category values
    def test_writeDataCategory(self):
        minimum = [self.combinedTable.values[0][1], self.combinedTable.values[0][2]]
        minimumPlusOne = [self.combinedTable.values[1][1], self.combinedTable.values[1][2]]
        nominal = [self.combinedTable.values[self.lenghOfTable // 2][1], self.combinedTable.values[self.lenghOfTable // 2][2]]
        maximumMinusOne = [self.combinedTable.values[self.lenghOfTable - 1][1], self.combinedTable.values[self.lenghOfTable - 1][2]]
        maximum = [self.combinedTable.values[self.lenghOfTable][1], self.combinedTable.values[self.lenghOfTable][2]]

        self.assertIn(minimum[0], self.dic[minimum[1]]['category'].values)
        self.assertIn(minimumPlusOne[0], self.dic[minimumPlusOne[1]]['category'].values)
        self.assertIn(nominal[0], self.dic[nominal[1]]['category'].values)
        self.assertIn(maximumMinusOne[0], self.dic[maximumMinusOne[1]]['category'].values)
        self.assertIn(maximum[0], self.dic[maximum[1]]['category'].values)

    

if __name__ == '__main__':
    unittest.main()