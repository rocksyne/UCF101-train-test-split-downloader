"""
Copyright 2018 Rockson Agyeman

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software 
is furnished to do so, subject to the following conditions:The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# I wrote this small scrit to take care of a pressing need. I downloaded the entire UCF101 video dataset from [4] hoping to use 
# one of the train-test splits specified in many research works. However, I soon found out that some videos from the train-test 
# split 1 list downloaded from [1] did not exist.

# I have written this script therefore to help me download all videos as they apply to the train-test split downloaded from [1]


# -------------------- REFERENCES ------------------------
# [1] The Train/Test Splits for Action Recognition. http://crcv.ucf.edu/data/UCF101/UCF101TrainTestSplits-RecognitionTask.zip
# [2] The Train/Test Splits for Action Detection. http://crcv.ucf.edu/data/UCF101/UCF101TrainTestSplits-DetectionTask.zip
# [3] Index of /THUMOS14/UCF101/UCF101.  http://crcv.ucf.edu/THUMOS14/UCF101/UCF101/
# [4] UCF101 - Action Recognition Data Set. http://crcv.ucf.edu/data/UCF101/UCF101.rar


# ----------- HOW TO USE -----------
# 1. Download the train- test split from [1] or [2] (depending on what you are doing) as a text file
# 2. Modify the parameters of this scrip in the *** modify section **** below and run


# Code begins
# import the important libraries
import os,sys
from tqdm import tqdm
import urllib.request


""" Video 
    Input:
        fileName: name of a text file that holds the list of all the video to be downloaded
    
    Output:
        List of videos to be downloaded
"""
def dataList(fileName=None):
    #check that a file name is provided
    if fileName is None:
        sys.exit("File name is absent: [dataList(fileName=None)]")
    
    # check that file name is valid
    if validPath(fileName) is False:
        sys.exit("Provided file does not exist: [dataList(fileName=None)]")
        
    #open the file for reading only
    txtFile = open(fileName,"r")

    # use list comprehension to get the list of all videos
    dataList = [dataList.strip("\n").split(" ")[0] for dataList in txtFile]

    # Debugging: helps you see how many records are available for reading
    print("File name:{}   Lines of data:{:,} ".format(fileName,len(dataList)))
    return dataList



""" Path validator script
    Input:
        dirName: Name of the path to be validated. Default is None. If not specified,
                 error will be flagged and system exite.
    
    Output:
        Returns true for valid path and false for invalid path
"""
def validPath(dirName=None):
    
    if dirName is None:
        sys.exit("Path is not availabe: [dirAvailabe(dirName=None)]".format())
    
    else:        
        if not os.path.exists(dirName): return False
        else: return True



""" Downloader scrip
    Input:
        vide_name: name of the video to be downloaded. The name will be added to base URL
        save_dir: location where the downloaded video will be saved.
    
    Output:
        Prints the name of a successfully downladed video
"""
def downloader(vide_name,save_dir):

    #base URL where videos can be downloaded
    baseURL = "http://crcv.ucf.edu/THUMOS14/UCF101/UCF101/"
    
    #re-naming
    dataPath = str(baseURL)+str(vide_name)
    dest = os.path.join("./"+save_dir,vide_name)
    
    # download file now
    urllib.request.urlretrieve(dataPath,dest)
    print("Downloaded {} successfully".format(vide_name))



# *** modify section ****
# --------- Apllication implementation starts here -----------------
# variable that holds the text file that holds split list of videos
textFileList = "trainlist01.txt"

# where to save teh downloaded videos
saveDestination = "./Train_Dataset"

# put the content in a variable
ls = dataList(textFileList)

#loop through the list and download each file
# use tqdm to get a nice progress bar
for _ls in tqdm(ls):
    
    # split the path into directory name and file name from the file name in the list
    nFolder,nFile = os.path.split(_ls)
    
    # reassign the variable to get the full path to where the video should be saved
    nFolder = os.path.join(saveDestination,nFolder)
    
    # if the destination directory does not exist, create it
    if not os.path.exists(nFolder):
        os.makedirs(nFolder)
    
    # download the videi (file) and save into the designated directory   
    downloader(nFile,nFolder)

