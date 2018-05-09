from google_images_download import google_images_download
from PIL import Image
import glob

def keyword(string):
    unwanted_words = [", ",",","!","?",".","name","one","ones","had","hid","inside","outside","then","only","was","such","pounded","pounding","gradually","above","below","but","butt","thin","fat","at","first","second","third","fourth","fifth","sixth","all","wasnt","wasn't","than","agree","disagree","changed","change","sit","sits","sitting","unchanged","probably","actually","excluded","included","anyone","more","feel","need","likely","needs","feels","feeling","friend","that","will","many","got","into","out","up","down","fell","whom","are","aren't","arent","fall","never","left","right","diagonal","one","knife","stab","shoot","shot","i'll","know","now","an","going","like","so","how","wouldnt","would","shouldnt","of","alot","be","because","been","as","shouldn't","can't","cant","can","cannot","isnt","why","who","what","when","were","where","yeah","your","you","too","two","to","hello","my","the","in","and","a","i","the","or","is","not","this","on","for","from","them","his","her","if","have","havent","haven’t","they","it","their","there","they're","isn't","he","she","we","should","could","couldn't"]
    def keywords(string):
        key_words = []
        words = string.split()
        for i in words:
            if i[-1] == '.' or i[-1] == '!' or i[-1] == '?' or i[-1] == ',' or i[-1] == ';':
                i = i[0:-1]
            if i.lower() not in unwanted_words and i.lower() not in key_words:
                key_words.append(i.lower())
        return key_words
    new_string = string
    new_list = keywords(new_string)
    other_string = ""
    #print(new_list)
    for item in new_list:
        if item != new_list[-1]:
            other_string += (item + ',')
        else:
            other_string += item
            #print(other_string)
            resp = google_images_download.googleimagesdownload()
            arguments = {"keywords":other_string,"limit":1,"print_urls":True,"format":"jpg"}
            resp.download(arguments)
            for word in new_list:
                image_file = glob.glob('./downloads/'+ word +'/*.jpg')
                print(image_file)
                for i in range(len(image_file)):
                    image_file[i] = Image.open(image_file[i])
                    image_file[i].show()
