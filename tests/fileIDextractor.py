# Start input form user
print('Enter URL:')
fileURL = input()
urllength = len(fileURL)
right_border = fileURL.rfind('/')
left_border = fileURL.rfind('/', 0, right_border)
fileID = fileURL[left_border+1:right_border]
print('left border', left_border)
print('url length', urllength)
print('right border', right_border)
print('fileID', fileID)