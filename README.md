### Mute That Annoying Math Software! (I swear this is useful)

This is a simple script to mute and unmute TT Math's Algebra 1 math program (or technically any program with the right know how)

![showcase](https://user-images.githubusercontent.com/101545981/233142054-2027ea67-bec8-4842-9cfa-846aee3197b7.gif)
### **Why does this exist?**

When I'm doing math, I like to be at peace, and on the lectures and math problems in Teaching Textbooks, the audio CONSTANTLY plays the instructor reading out the problem. This wouldn't be an issue normally, however when they were recording the audio for this curriculum, they managed an engineering feat, they managed to use TIN CANS as microphones to record all the audio for the program. My first instinct is to just mute the program all together, well, I do need to watch the lectures, to understand what they are teaching, and when I get a problem wrong I like to watch the explanation to see where I went wrong. However, there is no mute button, ANYWHERE.



![whynomute](https://user-images.githubusercontent.com/101545981/233144573-1e46bda0-869a-4311-8901-d3205c695783.gif)




Due to how windows 11 works, this requires me opening and closing the settings, going to sound, and then going to mixer, every time I want to mute and unmute the program, thus, I created this.  

### **"Can I use this to mute X?"**

Yes, yes you can.

- First, Clone this Repo


```python
git clone https://github.com/ezratweaver/shutupttmath
```

-  You also need to install PyGame (For the Mixer), and PyCaw


```python
pip3 install pygame
pip3 install pycaw
```
    

- Then simply change the variable APPLICATION_TARGET to the process name your trying to mute

```python
APPLICATION_TARGET = "AppWithoutMuteButton.exe"
```

- Then your done! If you have the know how you can compile it into an exe you can do that also.

The way this application is made, it is very easy to change the GUI without messing any of the code, or hell, you take the code and make your own app muter. So go! and enjoy your peace and quiet!
