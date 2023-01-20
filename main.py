import os
import pandas as pd

def main():
    
    dataEntries = readData()
    
    combinedTable = writeData(dataEntries)

    combinedTable.to_csv('combined.csv', index=False) #write combined data to csv file


#Read data from ./fixtures folder and save each file and file name into an array. Each index in the array will hold the file data. Each index will look like this: [[data, file_name], ...]
def readData():
    data = [] #array to hold data
    dataFolder = './fixtures' #folder to read data from

    for file in os.listdir(dataFolder): #loop through files in folder
        if file.endswith(".csv"): #check if file is a csv
            data.append((pd.read_csv(os.path.join(dataFolder, file)), file)) #append file data and file name to array
    return data
 
#Combine data from each file into one table 
def writeData(dataEntries):
    combinedData = {'email_hash' : [], 'category' : [], 'filename' : []} #create empty dictionary to hold combined data

    for data in dataEntries: #loop through each file data 

        #append data to dictionary
        combinedData['email_hash'].extend(data[0]['email_hash']) 
        combinedData['category'].extend(data[0]['category']) 
        combinedData['filename'].extend([data[1]] * len(data[0]['email_hash'])) #made a list of the file name the length of the file data since Pandas requires all arrays to be the same length when combining dataframes

    combinedTables = pd.DataFrame(combinedData) #create dataframe from dictionary
    return combinedTables
    



if __name__ == "__main__":
    main()