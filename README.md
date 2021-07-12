# ImageProcessingInCloudColab
PoC for Image processing in cloud

# How-To Start

## Local machine (or cobot who sends / receives images)

### Setup virtual enviroment
1. clone repository
2. create a virtual environement `virtualenv --python=python3.6 venv/`
3. start virtual environment `source venv/bin/activate`

### Setup connection to Google API
1. Go to APIs Console and make your own project.
2. Search for ‘Google Drive API’, select the entry, and click ‘Enable’.
3. Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.
4. Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. Once finished:
       a. Select ‘Application type’ to be Web application.
       b. Enter an appropriate name.
       c. Input http://localhost:8080 for ‘Authorized JavaScript origins’.
       e. Input http://localhost:8080/ for ‘Authorized redirect URIs’.
       f. Click ‘Save’.

5. Click ‘Download JSON’ on the right side of Client ID to download client_secret_<really long ID>.json.
6. Rename client_secret_<really long ID>.json to client_secrets.json

### Coud (Google Drive)
 1. Go to your drive and create following folders
  /drive/MyDrive/Img
  /drive/MyDrive/Img/in
  /drive/MyDrive/Img/out
  2. With this folderstructure you can easily delete the folder and control the traffic up/downloads
  

### Cloud (Google Colab)
  1. open this colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pQNFHrtMzTqWztrG8HuQAJviHJI75gZ0?usp=sharing) in your google account which corresponds to your client_secrets.json 
  2. Run all cells in colab step by step until you reach the last "Processing Loop with N=10 Imgs and exec-time calculation"
  3. No you should see "../drive/MyDrive/Img/in/i1.jpg is None" in the colab console each second. This shows that the "cloud" is waiting for receiving an image
  
  
### Run the overall application
  1. Your Colab service is running and shows "../drive/MyDrive/Img/in/i1.jpg is None" in the colab console each second.
  2. Your Drive is setup with the folder Img and subfolders in and out
  3. Your venv is sourced and all dependecies are installed
  4. Now you can execute the local client colab-test-drive.py with `python colab-test-drive.py`
  5. Now you should see the uploads and the round trip time on the client side (local machine)
  6. After some seconds you should see the in.img with bounding boxes in colab visualised in the console after "../drive/MyDrive/Img/in/i1.jpg is None"
  7. After some minutes the application is done uploading 10 x in.jpg and calulating YOLOv4 and downloading it again on the local machine.
  
  
  
