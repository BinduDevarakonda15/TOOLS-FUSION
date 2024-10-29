
import tkinter as tk
def button_click(message):
    label.config(text=message)


# Create the main windo
root = tk.Tk()
root.title("TOOL FUSION")
root.resizable(True, True)
logo_image = tk.PhotoImage(file="bgtoolfusion.png")
root.iconphoto(True, logo_image)

# Load your logo image
logo_image = tk.PhotoImage(file="bg_img_fin2.png")

# Set the background to the logo image
background_label = tk.Label(root, image=logo_image)
background_label.place(relwidth=1, relheight=1)

# Set window size to half of the screen
window_width = root.winfo_screenwidth() // 2
window_height = root.winfo_screenheight() // 2
root.geometry(f"{window_width}x{window_height}")

# Color Palette
background_color = "#FFFFFF"
text_color = "#000000"
button_color = "#3C90D8"
button_hover_color = "#539EC9"

# Label for Normal Tools
normal_tools_label = tk.Label(root, text="Tools Fusion", font=("Helvetica", 16), fg="white", bg="black")
normal_tools_label.grid(row=0, column=1, columnspan=1, pady=8, sticky='nsew')

# Buttons for Normal Tools
button_image1 = tk.PhotoImage(file="v_a.png")
button1 = tk.Button(root, text="Video to Audio Conv", command=lambda: button_click1(), bg="white", fg=text_color, padx=10,
                    pady=5, activebackground=button_hover_color, compound=tk.TOP, image=button_image1)
button1.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

# video to Audio convertor
def button_click1():
    from moviepy.editor import VideoFileClip
    import tkinter as tk
    from tkinter import filedialog

    def convert_video_to_audio():
        try:
            # Ask the user to choose the input video file
            input_video_file = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])

            # Check if a file is selected
            if not input_video_file:
                return

            # Ask the user to choose the output audio file
            output_audio_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".mp3", filetypes=[("Audio files", "*.mp3")])

            # Check if a file is selected
            if not output_audio_file:
                return

            # Convert the video to audio
            video_clip = VideoFileClip(input_video_file)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(output_audio_file, codec='mp3')

            print(f"Conversion successful.")
        except Exception as ex:
            print(f'Error: {str(ex)}')

    # Create the main GUI window
    root = tk.Tk()
    root.title("Video to Audio Converter")

    # Create "Choose File" button
    choose_file_button = tk.Button(root, text="Choose Video File", command=convert_video_to_audio)
    choose_file_button.pack(pady=20)



button_image2 = tk.PhotoImage(file="lan_trans.png")
button2 = tk.Button(root, text="Language Translator", command=lambda: button_click2(), bg="white", fg=text_color, padx=10,
                    pady=5, activebackground=button_hover_color, compound=tk.TOP, image=button_image2)
button2.grid(row=1, column=1, padx=10, pady=5, sticky='nsew')


# language translator
def button_click2():
    import tkinter as tk
    from translate import Translator

    def translate_text():
        text = input_text.get("1.0", "end-1c")
        language = language_var.get()

        translator = Translator(to_lang=language, backend='microsoft')
        translated_text = translator.translate(text)
        output_text.delete("1.0", "end")
        output_text.insert("1.0", translated_text)

    root = tk.Tk()
    root.title("Language Translator")

    input_label = tk.Label(root, text="Enter text to translate:")
    input_label.pack()

    input_text = tk.Text(root, height=5, width=50)
    input_text.pack()

    output_label = tk.Label(root, text="Translated text:")
    output_label.pack()

    output_text = tk.Text(root, height=5, width=50)
    output_text.pack()

    language_label = tk.Label(root, text="Select language to translate to:")
    language_label.pack()

    languages = ["en", "fr", "es", "de", "it", "ja", "ko", "zh"]
    language_var = tk.StringVar(root)
    language_var.set("en")

    language_menu = tk.OptionMenu(root, language_var, *languages)
    language_menu.pack()

    translate_button = tk.Button(root, text="Translate", command=translate_text)
    translate_button.pack()

    root.mainloop()

    
        
button_image3 = tk.PhotoImage(file="qrcode_gen img.png")

button3 = tk.Button(root, text="QR Code Genterator", command=lambda: button_click3(), bg="white", fg=text_color, padx=10,
                    pady=5, activebackground=button_hover_color, compound=tk.TOP, image=button_image3)
button3.grid(row=1, column=2, padx=10, pady=5, sticky='nsew')

#qr code generatoer
def button_click3():
    import tkinter as tk
    from tkinter import filedialog
    import qrcode

    class QRCodeGenerator:
        def __init__(self, root):
            self.root = root
            self.root.title("QR Code Generator")

            self.create_widgets()

        def create_widgets(self):
            self.label = tk.Label(self.root, text="Enter data to encode:")
            self.label.pack()

            self.entry = tk.Entry(self.root, width=40)
            self.entry.pack()

            self.generate_button = tk.Button(self.root, text="Generate QR Code", command=self.generate_qr_code)
            self.generate_button.pack()

        def generate_qr_code(self):
            data = self.entry.get()

            if data:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(data)
                qr.make(fit=True)

                img = qr.make_image(fill_color="black", back_color="white")

                file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

                if file_path:
                    img.save(file_path)
                    tk.messagebox.showinfo("QR Code Generator", f"QR code saved to {file_path}")

    if __name__ == "__main__":
        root = tk.Tk()
        app = QRCodeGenerator(root)
        root.mainloop()
        

    
button_image5 = tk.PhotoImage(file="file_convert.png")
button5 = tk.Button(root, text="File Convertor", command=lambda: button_click5(), bg="white", fg=text_color, padx=10,
                    pady=5, activebackground=button_hover_color, compound=tk.TOP, image=button_image5)
button5.grid(row=2, column=0, padx=10, pady=5, sticky='nsew')

#file convertor
def button_click5():
    import tkinter as tk
    from tkinter import filedialog
    from PIL import Image
    import pandas as pd
    import json
    import xmltodict

    def convert_img_to_pdf():
        input_file = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if input_file:
            output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if output_file:
                img = Image.open(input_file)
                img.save(output_file, "PDF", resolution=100.0)

    def convert_excel_to_csv():
        input_file = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xls;*.xlsx")])
        if input_file:
            output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if output_file:
                df = pd.read_excel(input_file)
                df.to_csv(output_file, index=False)

    def convert_json_to_csv():
        input_file = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON files", "*.json")])
        if input_file:
            output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if output_file:
                with open(input_file, 'r') as f:
                    data = json.load(f)
                df = pd.json_normalize(data)
                df.to_csv(output_file, index=False)

    def convert_xml_to_json():
        input_file = filedialog.askopenfilename(title="Select XML File", filetypes=[("XML files", "*.xml")])
        if input_file:
            output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if output_file:
                with open(input_file, 'r') as f:
                    data = xmltodict.parse(f.read())
                with open(output_file, 'w') as f:
                    json.dump(data, f, indent=4)

    def convert_jpeg_to_png():
        input_file = filedialog.askopenfilename(title="Select JPEG File", filetypes=[("JPEG files", "*.jpg;*.jpeg")])
        if input_file:
            output_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if output_file:
                img = Image.open(input_file)
                img.save(output_file, "PNG")

    root = tk.Tk()
    root.title("File Converter")

    button_img_to_pdf = tk.Button(root, text="Convert Image to PDF", command=convert_img_to_pdf)
    button_img_to_pdf.pack(pady=5)

    button_excel_to_csv = tk.Button(root, text="Convert Excel to CSV", command=convert_excel_to_csv)
    button_excel_to_csv.pack(pady=5)

    button_json_to_csv = tk.Button(root, text="Convert JSON to CSV", command=convert_json_to_csv)
    button_json_to_csv.pack(pady=5)

    button_xml_to_json = tk.Button(root, text="Convert XML to JSON", command=convert_xml_to_json)
    button_xml_to_json.pack(pady=5)

    button_jpeg_to_png = tk.Button(root, text="Convert JPEG to PNG", command=convert_jpeg_to_png)
    button_jpeg_to_png.pack(pady=5)

    root.mainloop()


button_image6 = tk.PhotoImage(file="text_to_s.png")

button6 = tk.Button(root, text="Text to Speech Generator", command=lambda: button_click6(), bg="white", fg=text_color, padx=10,
                    pady=5, activebackground=button_hover_color, compound=tk.TOP, image=button_image6)
button6.grid(row=2, column=1, padx=10, pady=5, sticky='nsew')

# Text to Speech Generator
def button_click6():
    from gtts import gTTS #gtts: goggle-text-to-speech
    import tkinter as tk
    from tkinter import filedialog

    def convert_text_to_speech():
        try:
            # Ask the user to choose the input text file
            input_text_file = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text files", "*.txt")])

            # Check if a file is selected
            if not input_text_file:
                return

            # Ask the user to choose the output audio file
            output_audio_file = filedialog.asksaveasfilename(title="Save As", defaultextension=".mp3",
                                                             filetypes=[("Audio files", "*.mp3")])

            # Check if a file is selected
            if not output_audio_file:
                return

            # Read text from the input file
            with open(input_text_file, 'r', encoding='utf-8') as file:
                text_content = file.read()

            # Convert text to speech
            tts = gTTS(text_content, lang='en')
            tts.save(output_audio_file)

            print(f"Conversion successful.")
        except Exception as ex:
            print(f'Error: {str(ex)}')

    # Create the main GUI window
    root = tk.Tk()
    root.title("Text to Speech Converter")

    # Create "Choose File" button
    choose_file_button = tk.Button(root, text="Choose Text File", command=convert_text_to_speech)
    choose_file_button.pack(pady=20)

    # Start the GUI main loop
    root.mainloop()
        
button_image7= tk.PhotoImage(file="utube_download.png")

button7 = tk.Button(root, text="YouTube Video Downloader", command=lambda: button_click7(), bg="white", fg=text_color, padx=10,
                    pady=5, activebackground=button_hover_color,compound=tk.TOP, image=button_image7)
button7.grid(row=2, column=2, padx=10, pady=5, sticky='nsew')

# youtube Video Downloader
def button_click7():
    import tkinter as tk
    from tkinter import filedialog
    from pytube import YouTube

    class YouTubeVideoDownloader:
        def __init__(self, root):
            self.root = root
            self.root.title("YouTube Video Downloader")

            self.create_widgets()

        def create_widgets(self):
            self.label = tk.Label(self.root, text="Enter YouTube Video URL:")
            self.label.pack()

            self.url_entry = tk.Entry(self.root, width=50)
            self.url_entry.pack()

            self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_location)
            self.browse_button.pack()

            self.download_button = tk.Button(self.root, text="Download Video", command=self.download_video)
            self.download_button.pack()

        def browse_location(self):
            self.download_path = filedialog.askdirectory()

        def download_video(self):
            video_url = self.url_entry.get()

            if not video_url:
                tk.messagebox.showwarning("Warning", "Please enter a valid YouTube video URL.")
                return

            try:
                youtube = YouTube(video_url)
                video = youtube.streams.filter(progressive=True, file_extension="mp4").first()

                if self.download_path:
                    video.download(self.download_path)
                    tk.messagebox.showinfo("Download Complete", f"Video downloaded to {self.download_path}")
                else:
                    tk.messagebox.showwarning("Warning", "Please choose a download location.")

            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {str(e)}")

    if __name__ == "__main__":
        root = tk.Tk()
        app = YouTubeVideoDownloader(root)
        root.mainloop()

# Buttons for AI Games
button_image12 = tk.PhotoImage(file="ping_pong.png")
button12 = tk.Button(root, text="Ping Pong Game", command=lambda: button_click12(), bg="white", fg=text_color, padx=10,
                     pady=5, activebackground=button_hover_color,  compound=tk.TOP, image=button_image12)
button12.grid(row=6, column=0, padx=10, pady=5, sticky='nsew')

# ping pong game
def button_click12():
    import sys
    import cv2
    import cvzone
    from cvzone.HandTrackingModule import HandDetector
    import numpy as np

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    # Importing all images
    imgBackground = cv2.imread("Background.png")
    imgGameOver = cv2.imread("gameOver.png")
    imgBall = cv2.imread("Ball.png", cv2.IMREAD_UNCHANGED)
    imgBat1 = cv2.imread("bat1.png", cv2.IMREAD_UNCHANGED)
    imgBat2 = cv2.imread("bat2.png", cv2.IMREAD_UNCHANGED)

    # Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=2)

    # Variables
    ballPos = [100, 100]
    speedX = 15
    speedY = 15
    gameOver = False
    score = [0, 0]

    while True:
        _, img = cap.read()
        img = cv2.flip(img, 1)
        imgRaw = img.copy()

        # Find the hand and its landmarks
        hands, img = detector.findHands(img, flipType=False)  # with draw

        # Overlaying the background image
        img = cv2.addWeighted(img, 0.2, imgBackground, 0.8, 0)

        # Check for hands
        if hands:
            for hand in hands:
                x, y, w, h = hand['bbox']
                h1, w1, _ = imgBat1.shape
                y1 = y - h1 // 2
                y1 = np.clip(y1, 20, 415)

                if hand['type'] == "Left":
                    img = cvzone.overlayPNG(img, imgBat1, (59, y1))
                    if 59 < ballPos[0] < 59 + w1 and y1 < ballPos[1] < y1 + h1:
                        speedX = -speedX
                        ballPos[0] += 30
                        score[0] += 1

                if hand['type'] == "Right":
                    img = cvzone.overlayPNG(img, imgBat2, (1195, y1))
                    if 1195 - 50 < ballPos[0] < 1195 and y1 < ballPos[1] < y1 + h1:
                        speedX = -speedX
                        ballPos[0] -= 30
                        score[1] += 1

        # Game Over
        if ballPos[0] < 40 or ballPos[0] > 1200:
            gameOver = True

        if gameOver:
            img = imgGameOver
            cv2.putText(img, str(score[1] + score[0]).zfill(2), (585, 360), cv2.FONT_HERSHEY_COMPLEX,
                        2.5, (200, 0, 200), 5)

        # If game not over move the ball
        else:

            # Move the Ball
            if ballPos[1] >= 500 or ballPos[1] <= 10:
                speedY = -speedY

            ballPos[0] += speedX
            ballPos[1] += speedY

            # Draw the ball
            img = cvzone.overlayPNG(img, imgBall, ballPos)

            cv2.putText(img, str(score[0]), (300, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
            cv2.putText(img, str(score[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

        img[580:700, 20:233] = cv2.resize(imgRaw, (213, 120))

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('r'):
            ballPos = [100, 100]
            speedX = 15
            speedY = 15
            gameOver = False
            score = [0, 0]
            imgGameOver = cv2.imread("gameOver.png")
        if key == ord('h'):
            sys.exit(0)

button_image13 = tk.PhotoImage(file="ballon_pop.png")

button13 = tk.Button(root, text="Ballon Popup Game", command=lambda: button_click13(), bg="white", fg=text_color, padx=10,
                     pady=5, activebackground=button_hover_color, compound=tk.TOP, image=button_image13)
button13.grid(row=6, column=1, padx=10, pady=5, sticky='nsew')

# Ballon popup
def button_click13():
    import random
    import pygame
    import cv2
    import numpy as np
    from cvzone.HandTrackingModule import HandDetector
    import time
    # Initialize
    pygame.init()

    # Create Window/Display
    width, height = 1280, 720
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Balloon Pop")

    # Initialize Clock for FPS
    fps = 30
    clock = pygame.time.Clock()

    # Webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)  # width
    cap.set(4, 720)  # height

    # Images
    imgBalloon = pygame.image.load('BalloonRed.png').convert_alpha()
    rectBalloon = imgBalloon.get_rect()
    rectBalloon.x, rectBalloon.y = 500, 300

    # Variables
    speed = 15
    score = 0
    startTime = time.time()
    totalTime = 30

    # Detector
    detector = HandDetector(detectionCon=0.8, maxHands=1)

    def resetBalloon():
        rectBalloon.x = random.randint(100, img.shape[1] - 100)
        rectBalloon.y = img.shape[0] + 50

    # Main loop
    start = True
    while start:
        # Get Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()

        # Apply Logic
        timeRemain = int(totalTime - (time.time() - startTime))
        if timeRemain < 0:
            window.fill((255, 255, 255))

            font = pygame.font.Font('Marcellus-Regular.ttf', 50)
            textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
            textTime = font.render(f'Time UP', True, (50, 50, 255))
            window.blit(textScore, (450, 350))
            window.blit(textTime, (530, 275))

        else:
            # OpenCV
            success, img = cap.read()
            img = cv2.flip(img, 1)
            hands, img = detector.findHands(img, flipType=False)

            rectBalloon.y -= speed  # Move the balloon up
            # check if balloon has reached the top without pop
            if rectBalloon.y < 0:
                resetBalloon()
                speed += 1

            if hands:
                hand = hands[0]
                x, y = hand['lmList'][8][0:2]
                if rectBalloon.collidepoint(x, y):
                    resetBalloon()
                    score += 10
                    speed += 1

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgRGB = np.rot90(imgRGB)
            frame = pygame.surfarray.make_surface(imgRGB).convert()
            frame = pygame.transform.flip(frame, True, False)
            window.blit(frame, (0, 0))
            window.blit(imgBalloon, rectBalloon)

            font = pygame.font.Font('Marcellus-Regular.ttf', 50)
            textScore = font.render(f'Score: {score}', True, (50, 50, 255))
            textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
            window.blit(textScore, (35, 35))
            window.blit(textTime, (1000, 35))

        # Update Display
        pygame.display.update()
        # Set FPS
        clock.tick(fps)

button_image14 = tk.PhotoImage(file="snake_game.png")
button14 = tk.Button(root, text="Snake Game", command=lambda: button_click14(), bg="white", fg=text_color, padx=10,
                     pady=5, activebackground=button_hover_color,  compound=tk.TOP, image=button_image14)
button14.grid(row=6, column=2, padx=10, pady=5, sticky='nsew')


# snake game
def button_click14():
    import math
    import random
    import sys
    import cvzone
    import cv2
    import numpy as np
    from cvzone.HandTrackingModule import HandDetector

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.8, maxHands=1)

    class SnakeGameClass:
        def __init__(self, pathFood):
            self.points = []  # all points of the snake
            self.lengths = []  # distance between each point
            self.currentLength = 0  # total length of the snake
            self.allowedLength = 150  # total allowed Length
            self.previousHead = 0, 0  # previous head point

            self.imgFood = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
            self.hFood, self.wFood, _ = self.imgFood.shape
            self.foodPoint = 0, 0
            self.randomFoodLocation()

            self.score = 0
            self.gameOver = False

        def randomFoodLocation(self):
            self.foodPoint = random.randint(100, 1000), random.randint(100, 600)

        def update(self, imgMain, currentHead):

            if self.gameOver:
                cvzone.putTextRect(imgMain, "Game Over", [300, 400],
                                   scale=7, thickness=5, offset=20)
                cvzone.putTextRect(imgMain, f'Your Score: {self.score}', [300, 550],
                                   scale=7, thickness=5, offset=20)
                cvzone.putTextRect(imgMain, "press r for restart the game...", [300, 600],
                                   scale=3, thickness=2, offset=10)
                cvzone.putTextRect(imgMain, "press h to exit from game...", [300, 650],
                                   scale=3, thickness=2, offset=10)
            else:
                px, py = self.previousHead
                cx, cy = currentHead

                self.points.append([cx, cy])
                distance = math.hypot(cx - px, cy - py)
                self.lengths.append(distance)
                self.currentLength += distance
                self.previousHead = cx, cy

                # Length Reduction
                if self.currentLength > self.allowedLength:
                    for i, length in enumerate(self.lengths):
                        self.currentLength -= length
                        self.lengths.pop(i)
                        self.points.pop(i)
                        if self.currentLength < self.allowedLength:
                            break

                # Check if snake ate the Food
                rx, ry = self.foodPoint
                if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and \
                        ry - self.hFood // 2 < cy < ry + self.hFood // 2:
                    self.randomFoodLocation()
                    self.allowedLength += 50
                    self.score += 1
                    print(self.score)

                # Draw Snake
                if self.points:
                    for i, point in enumerate(self.points):
                        if i != 0:
                            cv2.line(imgMain, self.points[i - 1], self.points[i], (0, 0, 255), 20)
                    cv2.circle(imgMain, self.points[-1], 20, (0, 255, 0), cv2.FILLED)

                # Draw Food
                imgMain = cvzone.overlayPNG(imgMain, self.imgFood,
                                            (rx - self.wFood // 2, ry - self.hFood // 2))

                cvzone.putTextRect(imgMain, f'Score: {self.score}', [50, 80],
                                   scale=3, thickness=3, offset=10)

                # Check for Collision
                pts = np.array(self.points[:-2], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(imgMain, [pts], False, (0, 255, 0), 3)
                minDist = cv2.pointPolygonTest(pts, (cx, cy), True)

                if -1 <= minDist <= 1:
                    print("Hit")
                    self.gameOver = True
                    self.points = []  # all points of the snake
                    self.lengths = []  # distance between each point
                    self.currentLength = 0  # total length of the snake
                    self.allowedLength = 150  # total allowed Length
                    self.previousHead = 0, 0  # previous head point
                    self.randomFoodLocation()

            return imgMain

    game = SnakeGameClass("Ratimg.png")

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)

        if hands:
            lmList = hands[0]['lmList']
            pointIndex = lmList[8][0:2]
            img = game.update(img, pointIndex)
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('r'):
            game.gameOver = False
        if key == ord('h'):
            sys.exit(1)


# Set window background color
root.configure(bg=background_color)

# Set column and row weights to make buttons center
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)



# Run the Tkinter event loop
root.mainloop()
