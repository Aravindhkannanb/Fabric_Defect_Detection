import pyrebase
config={
    "apiKey": "AIzaSyCiueMzBW3jvUS3rhQ2fyjUmZZIlXgdjbQ",
  "authDomain": "textile-anamoly.firebaseapp.com",
  "projectId": "textile-anamoly",
  "storageBucket": "textile-anamoly.appspot.com",
  "messagingSenderId": "997886558696",
  "appId": "1:997886558696:web:6b98d09d02251e6173645d",
  "measurementId": "G-PFY3C8NKD6",
  "databaseURL":"gs://textile-anamoly.appspot.com"
}
firebase = pyrebase.initialize_app(config)

# Use double backslashes or a raw string for the local file path on Windows
localpath = r"F:\Fabric_yolov8\annotated_screenshot.jpg"

cloudpath = "Defects/annotated_screenshot.jpg"

firebase.storage().child(cloudpath).put(localpath)