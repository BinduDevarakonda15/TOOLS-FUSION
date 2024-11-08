
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



# Set window background color
root.configure(bg=background_color)

# Set column and row weights to make buttons center
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)



# Run the Tkinter event loop
root.mainloop()
