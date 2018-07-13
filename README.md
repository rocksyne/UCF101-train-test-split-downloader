# UCF101-train-test-split-downloader
Download UCF101 videos (dataset) according train/test split


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

I wrote this small scrit to take care of a pressing need. I downloaded the entire UCF101 video dataset from [4] hoping to use 
one of the train-test splits specified in many research works. However, I soon found out that some videos from the train-test 
split 1 list downloaded from [1] did not exist.

I have written this script therefore to help me download all videos as they apply to the train-test split downloaded from [1]


REFERENCES
1. The Train/Test Splits for Action Recognition. http://crcv.ucf.edu/data/UCF101/UCF101TrainTestSplits-RecognitionTask.zip
2. The Train/Test Splits for Action Detection. http://crcv.ucf.edu/data/UCF101/UCF101TrainTestSplits-DetectionTask.zip
3. Index of /THUMOS14/UCF101/UCF101.  http://crcv.ucf.edu/THUMOS14/UCF101/UCF101/
4. UCF101 - Action Recognition Data Set. http://crcv.ucf.edu/data/UCF101/UCF101.rar


HOW TO USE
1. Download the train- test split from [1] or [2] (depending on what you are doing) as a text file
2. Modify the parameters of this scrip in the *** modify section **** below and run
