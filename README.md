MCAutoFishing

# Intro

This is a simple machine learning program which automates the tedious process of
 fishing in Minecraft.

# Setup

1) Install Python 3.8.5 or higher
1) Clone or download this repo
1) Open Powershell in the program directory
1) Run `py -m pip install -r requirements.txt` and wait for it to finish

Then, in Minecraft
1) Turn subtitles on if they are not already
1) Do NOT force unicode font
1) [optional but preferred] set resolution to fullscreen windowed on
your main monitor @ 1920x1080p
1) [optional but preferred] set GUI scale to 4

# Usage

1) Open Minecraft, find a fishing spot and an angle at which you want to throw
your lure
1) Open Powershell in the program directory
1) Run `py autofish.py`
1) Switch back to your Minecraft window and unpause

# Troubleshooting
## Errors during Setup
1) Run `py --version` and make sure your PATH is pointing at Python 3.8.5
1) Make sure you're connected to the internet
1) Try Powershell in administrator mode, or use command prompt,
or command prompt in administrator mode
## Program died before it started spitting out rows of ['splashing'] or similar
### ...and complained about Joblib.load() and 'long long' and stuff like that
1) Run `py train_text_classifier.py` and try again
### ...and complained about something containing 'mc_hwnd' and 'raise'
1) Go to the config and try using the `override_resolution` flag
## Program spat out lots of rows of ['splashing'] or similar but wasn't fishing correctly
### ...and I haven't tried `override_resolution` yet
1) Go to the config and try setting the `override_resolution` to `True`
1) Go back to setup and make sure you follow all the instructions, including the
optional ones
### ...and I've tried everything else and I'm REALLY brave and know some Python
#### If you hit trouble, contact the repo author for help
1) Contact the repo author and acquire the training images and `labels.txt`
1) Put those in `<program dir>/imgs/`
1) Note the highest numbered image in the `/imgs/` directory
1) Go to line 8 of `capture_examples.py` and set `j = X`
to `j = <highest_number_plus_one>`
1) Go into Minecraft and get ready to fish
1) Run `py capture_examples.py`, quickly switch to Minecraft and start fishing
1) After approx. 60 seconds a new window will open indicating the program is
done - you should have caught at least one fish in this time, but preferably
3 or more
1) Check the new image samples in `/imgs/` - the ones containing text must be
centered vertically, with minimal/no movement up and down between samples
1) Append to `labels.txt` in the exact same manner as in the existing rows;
`n,label` where `label` is the lower-case and snake_cased text of the subtitle.
1) Delete `dataframe.csv`
1) Run `py train_text_classifier.py`, it'll probably crash but that's okay
1) Run `py train_text_classifier.py`, it should NOT crash
1) Go back to Usage and try again with your new ML model
