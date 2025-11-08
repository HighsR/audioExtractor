# 🎧 audioExtractor

Extract audio from any video file — fast, simple, and cross-platform.
Give it a video (e.g., `.mp4`, `.mov`, `.mkv`) and get a clean audio file (`.mp3`, `.wav`) in seconds.

> Perfect for saving soundtracks, podcasts, lectures, or voice-overs.

---

# About This Project

This project provides a simple, command-line tool to extract the audio track from any video file. It's built in Python and relies on the powerful `moviepy` library, which uses **FFmpeg** under the hood.

The goal is to be a fast, no-fuss utility that you can run from your terminal or import into your own Python projects.

---

# Features ✨

-   🗂️ **Wide Format Support:** Works with `.mp4`, `.mov`, `.mkv`, `.avi`, and more.
-   🎵 **Flexible Output:** Save your audio as `.mp3` (default), `.wav`, `.ogg`, or any format FFmpeg supports.
-   ⚡ **Fast & Efficient:** Uses FFmpeg for direct audio stream extraction, which is very fast.
-   🧰 **Dual Use:** Run it as a standalone **CLI tool** or `import` its functions into your own Python scripts.
-   🖥️ **Cross-Platform:** Works on **Windows**, **macOS**, and **Linux**.

---

# Requirements 🔧

-   **Python 3.8+**
-   **FFmpeg:** Must be installed and accessible in your system's PATH.
    -   **🪟 Windows:** [Download FFmpeg](https://ffmpeg.org/download.html) and add the `/bin` folder to your PATH.
    -   **🍎 macOS:** `brew install ffmpeg`
    -   **🐧 Linux:** `sudo apt install ffmpeg`
-   **Python Libraries:**
    ```bash
    pip install moviepy
    ```

---

# Building and Running 🚀

### 1. Clone the Repository

```bash
git clone https://github.com/HighsR/audioExtractor.git
cd audioExtractor
```
### 2. Install Dependencies
```bash
pip install moviepy
```
### 3. Run the Extractor
```bash
# Default MP3 extraction
# Saves as 'input.mp3' in the same folder
python audioExtractor.py input.mp4

# Specify an output format
python audioExtractor.py input.mp4 --format wav

# Specify a full output path
python audioExtractor.py input.mp4 --out extracted/my-audio.mp3
```
## ⚖️ License

This project was created for educational purposes based on a Udemy course.  
Certain parts of the code or structure are derived from the course material.  
Therefore, no open-source license is applied, and redistribution is not permitted.
