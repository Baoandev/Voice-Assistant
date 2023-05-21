import tkinter as tk
import speech_recognition as sr
from gtts import gTTS
import playsound

def voice_assistant(window):

    # Tạo các widgets
    label1 = tk.Label(window, text="Nhập tên file output: ")
    label1.pack()
    filename_entry = tk.Entry(window)
    filename_entry.pack()

    label2 = tk.Label(window, text="Chọn ngôn ngữ (en hoặc vi hoặc fr): ")
    label2.pack()
    language_entry = tk.Entry(window)
    language_entry.pack()
    result_panel = tk.Text(window, height=5, width=50)
    result_panel.pack()

    def record():
        # Cập nhật ngôn ngữ và tên file từ widgets
        language = language_entry.get()
        filename = filename_entry.get()

        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)

            print("Nói đi ")
            audio_data = r.record(source, duration = 3)

            print("KẾT QUẢ_______________________")
            try:
                text = r.recognize_google(audio_data, language=language)
            except sr.UnknownValueError:
                text = "Không xác định được giọng nói"
            print("Bạn đã nói là : ",format(text))
            result_panel.insert(tk.END, "Bạn đã nói: " + text + "\n")
            result_panel.insert(tk.END, "Kết quả nhận dạng: " + text + "\n")
            speak(text, language, filename)
    
    record_button = tk.Button(window, text="Bắt đầu ghi âm", command=record, bg='pink')
    record_button.pack()

    def speak(text, language, filename):
        # Đọc chữ tiếng Việt => nói ra tiếng Việt hoặc tiếng Anh hoặc tiếng pháp
        tts = gTTS(text=text, lang=language)
        tts.save(filename + ".mp3")
        playsound.playsound(filename + ".mp3")



if __name__ == '__main__':
    window = tk.Tk()
    window.title("Voice Assistant - Thái Bảo An")
    window.geometry("500x400")
    voice_assistant(window)
    window.mainloop()