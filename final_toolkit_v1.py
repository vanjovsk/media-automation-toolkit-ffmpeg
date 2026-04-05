import ffmpeg, os, requests, shutil, subprocess
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# 🎛️ THE MASTER SWITCHES
# ==========================================
USE_LOCAL_DESKTOP = True   # Set to True to save a copy on your Desktop
USE_FRAMEIO_CLOUD = False  # Change this to True when you have a Pro/Team account!
# ==========================================

def run_ffmpeg_proxy(input_file):
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f"{base_name}_PROXY.mp4"
    print(f"🎬 [FFmpeg] Processing: {input_file}...")
    (
        ffmpeg.input(input_file)
        .filter('scale', 1280, 720)
        .filter('drawtext', text=f"PROXY: {base_name}", x='w-tw-10', y='h-th-10', fontsize=24, fontcolor='white', box=1, boxcolor='black@0.5')
        .output(output_file, vcodec='libx264', crf=23, acodec='aac').overwrite_output().run(quiet=True)
    )
    return output_file

def ingest_to_desktop(file_path):
    dest = os.path.expanduser("~/Desktop/VANJA_REVIEW_FOLDER")
    if not os.path.exists(dest): os.makedirs(dest)
    shutil.copy(file_path, os.path.join(dest, os.path.basename(file_path)))
    print(f"✅ Local Ingest Success: {dest}")
    subprocess.run(["open", dest])

def upload_to_frameio(file_path):
    """The Cloud Logic (Currently blocked by 403 Forbidden)"""
    token = os.getenv("FRAMEIO_TOKEN")
    target_id = os.getenv("FRAMEIO_PROJECT_ID")
    url = f"https://api.frame.io/v2/assets/{target_id}/children"
    payload = {
        "name": os.path.basename(file_path),
        "type": "file",
        "file_size": os.path.getsize(file_path),
        "filetype": "video/mp4"
    }
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print("✨ Cloud Upload Success!")
    else:
        print(f"❌ Cloud Error {response.status_code}: {response.text}")

def main():
    input_video = "Images/test_video.mov"
    if not os.path.exists(input_video):
        print(f"⚠️ File not found: {input_video}")
        return

    # STEP 1: Always make the proxy
    proxy = run_ffmpeg_proxy(input_video)

    # STEP 2: Use the Desktop "Lens" if active
    if USE_LOCAL_DESKTOP:
        ingest_to_desktop(proxy)

    # STEP 3: Use the Cloud "Lens" if active
    if USE_FRAMEIO_CLOUD:
        upload_to_frameio(proxy)

    # Clean up the temporary file in the folder to keep it tidy
    if os.path.exists(proxy):
        os.remove(proxy)

if __name__ == "__main__":
    main()