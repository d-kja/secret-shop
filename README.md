# Secret shop

Secret shop is a simple script to re-roll the shop in E7, you might have to adjust the coordinates according to your screen size.
<br />
<br />

## Dependencies

### PyAutoGui

This package is the core of this script, but before installing it you need python installed. If you're not used to using Python and the terminal, there's a bunch of guides on the internet. Here's their website: [link](https://www.python.org/downloads)
<br />

```
# Update Python's default package manager
python3 -m pip install --upgrade pip

# Install Pillow
pip install --upgrade Pillow

# Install PyAutoGui
pip install pyautogui
```
<br />

### OpenCV

During the installation of `opencv-python`, you might see a **warning** saying that the scripts folder isn't in your path, copy the path inside the parenthesis and save it somewhere temporarily. Depending on your OS, you might have to take different steps. Usually I'd like to think that Linux users might be able to figure that out by themselves, because they're more tech savvy than Windows or Mac users cof- cof...

So, for windows users it might look like the following path:

Path: `C:\Users\[YOUR-USER]\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_[SOME-WEIRD-HASH]\LocalCache\local-packages\Python312\Scripts`

Remember to replace the `[YOUR-USER]` with your actual user and the `[SOME-WEIRD-HASH]` with the hash that the python folder has in your computer. Just one thing though, I installed python with microsoft store, so the steps that you need to take to achieve the same result might be different.

<br />

```
pip install opencv-python
```
<br />

## How to use

Open a terminal and change the folder to the one containing the script that ends with `.py` and do the following. Let's say mine is inside the `Downloads` folder

Small reminder, the game needs to be open and **visible** with the Secret shop open as well, as I'm using OpenCV with Pillow it takes screenshots of your screen to find the elements in the sauce folder. You aren't going to be able to use your mouse for a while, so it's something that you start and leave it running while you do some chores. You can change the amount of loops/runs that the script does by changing the `limit` variable/field in the `automate.py` file

```
cd Downloads/secret-shop
```
<br />

Then run the following and click on the game window with the shop open

```
python automate.py
```

