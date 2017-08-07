#
# this will work when run with ctrl-f5, but will not work when run in the interactive enviroenment because of write prics
#

# THIS WORKS
# https://www.youtube.com/watch?v=UQ7qHA_mS4c
# https://www.youtube.com/watch?v=0_FOPHT4-i0
import wget 
def files_wget():
    url = 'https://www.dropbox.com/s/15bhqbymuaqn027/this%20is%20a%20document.txt?dl=1'
    url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
    url = 'https://www.dropbox.com/s/4xnzewhp22ncbu0/data.csv?dl=1' # this is data.csv
    filename = wget.download(url)
    print(filename)

files_wget()




def files_dropboxAPI():
    #
    # READ A FILE FROM DROPBOX
    #
    # https://www.dropbox.com/s/15bhqbymuaqn027/this%20is%20a%20document.txt?dl=0
    import dropbox
    access_token = '15bhqbymuaqn027'
    dbx = dropbox.Dropbox(access_token)

    with open("Test.csv", "w") as f:
        metadata, res = dbx.files_download(path="Test.csv")
        f.write(res.content)

#files_dropbox()


def files_local():
    f = open('wasteland.txt', mode='wt', encoding='utf-8')

    #help(f)

    f.write("what are the roots that clutch, ")
    f.write("what branches grow\n")
    f.write("Out of this stony subbish? ")
    f.close()

    g = open('wasteland.txt', mode='rt', encoding='utf-8')
    g.read(32) # read 32 characters, may be different than reading 32 bytes ?
    g.read() # read till end of file

    g.seek(0) # go to the 0th location in the file
    g.readline() # get the next line
    g.readline() # get the next line

    g.seek(0) # go to the 0th location in the file
    g.readlines() # get all the lines into a list

    f.close()

    h = open('wasteland.txt', mode='at', encoding='utf-8') # append, text
    h.writelines(['\n1 2', ' 3 4', '\n5 6 7 8'])  # write everything in a list
    h.close()

    import sys

    def read_file(filename):
        f = open(filename, mode='rt', encoding='utf-8')
        for line in f:
            sys.stdout.write(line) # like print but does not add its own \n so the \n read in will do the next line
        f.close()

    read_file('wasteland.txt')


#files_local()

