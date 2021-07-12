from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pydrive.files
import time
import cv2

def downloadAndSave(img_name):
    while True:
        try:
            # Read a file
            fid = drive.ListFile({'q':f"title='{img_name}'"}).GetList()[0]['id']
            f = drive.CreateFile({'id': fid})
            f.FetchMetadata(fetch_all=True)  # some file types require this
            f.GetContentFile(img_name)
            break
        except:
            print(f"File {img_name} is processing... ")
            time.sleep(1)

def uploadAndPredict(img_name):
    # Read file and set it as a content of this instance.
    newFile = drive.CreateFile({'parents': [{'id': '1yvTHEjS6sCHFEtqnpbCgkvm3d8L8nwVN'}]})
    newFile.SetContentFile(img_name)
    newFile.Upload() # Upload the file.

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

# Create GoogleDrive instance with authenticated GoogleAuth instance.
drive = GoogleDrive(gauth)

gtime = time.time()

for i in range(1,10):

    start = time.time()

    tmp_in_img = "i"+str(i)+".jpg"
    tmp_out_img = "o"+str(i)+".jpg"

    # copy local test-img to i(i).img first i..input second i is counter
    cv2.imwrite(tmp_in_img, cv2.imread('in.jpg'))

    uploadAndPredict(tmp_in_img)
    download = downloadAndSave(tmp_out_img)

    end = time.time()

    print(f"Round Trip Time (Send i{ str(i) }, Receive Result) {end - start} seconds")
    

