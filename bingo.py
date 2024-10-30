'''This is a python script to make a simple bingo card'''
from random import sample
from numpy import sqrt
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects

# Number of rows and columns for the card
NOR = 5
# Do you want to add a second list with hybrid meeting options
HYBRID = True

# List of possible fields
options = [
    "Yellow",
    "Thank you slide",
    "Font change",
    "Cut off text",
    "Screenshot pasted",
    "Skipping slides",
    "Not English",
    "I can taste the pixels",
    "Reading labels is optional",
    "Gradient background",
    "Full sentences",
    "Slide = my script",
    "TLA",
    "Tipo",
    "Wrong button",
    "Unnecessary Animation",
    "Device compatibility",
    "Overfull plot",
    "Colour = Fun",
    "Contrast is optional",
    "Time slots are guidelines",
    "Text everywhere",
    "Talking to the slide",
    "Stop word overload",
    "Comic Sans",
    "Speaking softly",
    "Equations",
    "Citations are optional",
    "4:3 is still relevant",
    "'Ofcourse I know what slide comes next'",
    "Notification!",
    "Unnecessary axes",
    "monotone =_="
]
# Additional list of options
if HYBRID:
    options = options + [
        "Muted",
        "Participant not muted",
        "Forgot to share"
    ]

# Check if there are enough options
if len(options) < NOR**2:
    NOR = int(sqrt(len(options)))

# If there is an odd number of row the centre becomes a free space
if NOR%2 != 0:
    # Sample the options
    card = sample(options,NOR**2-1)
    card.insert(int(NOR**2/2),"Free Space")
else:
    # Sample the options
    card = sample(options,NOR**2)

# Create a field of subplots
fig, ax = plt.subplots(figsize=(NOR,NOR), dpi=300,
                        nrows=NOR,ncols=NOR)
# Loop over the subplots to add the text and add decorations
for i in range(NOR**2):
    # Remove the axis ticks
    ax.flat[i].tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
    ax.flat[i].patch.set_alpha(0.7)
    # Add decorations
    if card[i] == "Comic Sans":
        # if Comic sans missing run:
        # sudo apt install msttcorefonts -qq
        # rm ~/.cache/matplotlib -rf
        txt = ax.flat[i].text(0.5, 0.5, card[i], fontsize=8, family='Comic Sans MS',
                              va="center",ha="center", wrap=True)
    elif card[i] == "Yellow":
        txt = ax.flat[i].text(0.5, 0.5, card[i], fontsize=8, color="y",
                              va="center",ha="center", wrap=True)
        txt.set_path_effects([PathEffects.withStroke(linewidth=1, foreground='k')])
        plt.draw()
    elif card[i] == "Equations":
        ax.flat[i].text(0.5, 0.5,r'$\Sigma$qu$\Delta$ti$\phi$ns', fontsize=8,
                              va="center",ha="center", wrap=True)
    elif card[i] == "Gradient background":
        ax.flat[i].imshow([[0,0],[1,1]], cmap=plt.cm.binary, interpolation='bicubic',
                  extent=plt.xlim() + plt.ylim())
        plt.draw()  
        txt = ax.flat[i].text(0.5, 0.5, card[i], fontsize=8, color="w",
                              va="center",ha="center", wrap=True)
        txt.set_path_effects([PathEffects.withStroke(linewidth=1, foreground='k')])
    elif card[i] == "Colour = Fun":
        ax.flat[i].imshow([[0,0],[1,1]], cmap=plt.cm.rainbow, interpolation='bicubic',
                  extent=plt.xlim() + plt.ylim())
        plt.draw()  
        txt = ax.flat[i].text(0.5, 0.5, card[i], fontsize=8, color="w",
                              va="center",ha="center", wrap=True)
        txt.set_path_effects([PathEffects.withStroke(linewidth=1, foreground='k')])
    elif card[i] == "Free Space":
        ax.flat[i].scatter(0.5, 0.5, s=1000, marker='*', color='gold')
        txt = ax.flat[i].text(0.5, 0.5, card[i], fontsize=8,
                              va="center",ha="center", wrap=True)
    else:
        txt = ax.flat[i].text(0.5, 0.5, card[i], fontsize=8,
                              va="center",ha="center", wrap=True)
    # Make the text fit the subplot
    txt._get_wrap_line_width = lambda :ax.flat[i].bbox.width*0.95

# Remove the spaces between the subplots
plt.subplots_adjust(wspace=0, hspace=0)

# Add a title to the card
txt = plt.suptitle("Presentaton Sin Bingo", color="w", fontsize=18)
txt.set_path_effects([PathEffects.withStroke(linewidth=3, foreground='k')])
plt.draw()

# Add a background image
try:
    image = plt.imread('background.jpg')
    background_ax = plt.axes([0, 0, 1, 1])
    background_ax.set_zorder(-1)
    background_ax.imshow(image, aspect='auto',alpha=0.75)
except Exception:
    pass

# Save the card
plt.savefig("BingoCard.png")
