# Secret shop

Secret shop is a simple script to re-roll the shop in E7, you might have to adjust the coordinates according to your screen size.
<br />
<br />

## Dependencies
<br />

### PyAutoGui

This package is the core of this script, but before installing it you need python installed. If you're not used to using Python and the terminal, there's a bunch of guides on the internet. Here's their website: [link](https://www.python.org/downloads)
<br />
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

Remember to replace the `[YOUR-USER]` with your actual user and the `[SOME-WEIRD-HASH]` with the hash that the python folder has in your computer. Just one thing though, I installed python with microsoft store, so your the steps that you need to take might be different.

<br />

```
pip install opencv-python
```

## How to use

Oh that's simple, just open a terminal and change the folder to the one containing the script and do the following. Let's say mine is inside the `Downloads` folder

```
cd Downloads/secret-shop
```

Then run the following and click on the game window with the shop open

```
python automate.py
```

