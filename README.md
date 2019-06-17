# NeuralNetwork-ImageToText

Code to extract text from images

```
pip install -r requirements.txt
```


If you encounter file not found error as below:
```
FileNotFoundError: [Errno 2] No such file or directory: 'tesseract'
```

Run the following command (MACOS)
```
brew install tesseract
```
Install Anaconda (Window)

Then run the image-to-text.py as below:
```
 python image-to-text.py <input folder>

```

We observe that for clean inputs the accuracy is high. See input 2.
Noisy input may not have the same effect!