def extract_file(filename):
    with open(filename, 'r') as f:
        #print(f.read())
        data = f.readlines()
        for line in data:
            print(line.split())
        
        
extract_file("/Volumes/Macintosh HD/programming-test/text.txt")