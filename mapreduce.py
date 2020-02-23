#Charlie Juarez
import pymp
import time

#Method that opens the files
def openfiles():
    filelist = []
    file1 = open('shakespeare1.txt', 'r').read()
    file2 = open('shakespeare2.txt', 'r').read()
    file3 = open('shakespeare3.txt', 'r').read()
    file4 = open('shakespeare4.txt', 'r').read()
    file5 = open('shakespeare5.txt', 'r').read()
    file6 = open('shakespeare6.txt', 'r').read()
    file7 = open('shakespeare7.txt', 'r').read()
    file8 = open('shakespeare8.txt', 'r').read()
    filelist.extend([file1, file2, file3, file4,
                     file5, file6, file7, file8])
    return filelist

#Method that counts the total number of words through parallel
def processfiles(wordlist, filelist, numthreads):
    detectedwords = pymp.shared.array((16,), dtype='float64')

    #Number of threads to parallelize with
    with pymp.Parallel(numthreads) as p:
        #Iterate through the lines in the files
        for line in p.iterate(filelist):
            #Checks the line with the word its looking for one by one
            for index in range(len(wordlist)):
                lowercaseline = line.lower()
                count = line.count(wordlist[index])
                p.lock.acquire()
                detectedwords[index] += count
                p.lock.release()

    #Uncomment to print the wordcount done by each thread scenario
    """for number in detectedwords:
        print(number)"""


def main():
    wordlist = ['hate', 'love', 'death', 'night', 'sleep',
                'time', 'henry', 'hamlet', 'you', 'my', 'blood',
                'poison', 'macbeth', 'king', 'heart', 'honest']
    threadlist = [1, 2, 4, 8]

    starttime = time.time()
    filelist = openfiles()
    endtime = time.time() - starttime
    print('Time it took to open&read the files was ' + str(endtime) +
          ' seconds.')

    for numthreads in threadlist:
        starttime = time.time()
        processfiles(wordlist, filelist, numthreads)
        endtime = time.time() - starttime
        print('Time it took to process the files with ' + str(numthreads) +
              ' threads was ' + str(endtime) + ' seconds')

if __name__ == "__main__":
    main()
