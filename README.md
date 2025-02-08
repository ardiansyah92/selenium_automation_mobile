# selenium automation mobile with python

  This example automation mobile app with python
  
  If you want running this code
  
  Step 1 Running Appium
  
    appium -a 127.0.0.1 -p 4723 --allow-cors
  
  Step 2 Running Emulator 
  
    emulator -avd <yourdevices>

  Step 3 Running this code 

    python login.py

  Video
    


https://github.com/user-attachments/assets/da98cdd0-eb71-4abe-a15b-dbc75a13b866


If you want spy apk with selenium

  Step 1 Running Appium

    1.Create PATH ANDROID_HOME
    2.Set PATH platform-tools
    3.run "appium -a 127.0.0.1 -p 4723 --allow-cors"

  Step 2 Running Appium Inspector

    open appium inspector in your computer
    
  Step 3 Set Remote Host in Appium Inspector
  
    Set Remote Host same with running appium

  Step 4 Set Remote Port in Appium Inspector
    
    Set Remote Port same with running appium

  Step 5 Set Romote Path in Appium Inspector
    
    Set Remote Path "/wd/hub"

  Step 6 Set Json Representation in Appium Inspector
    
    Set JSON Representation like this
    {
    "appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:app": "location your apk .apk"
    }
    
