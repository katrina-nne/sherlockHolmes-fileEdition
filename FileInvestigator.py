import os

class FileInvestigator:

    #dictionary 📖
    fileTypes = {"text":[".txt",".doc",".docx",".pdf"],"image":[".jpg",".jpeg",".png",".gif",".ico"],"video":[".mp4",".avi",".mov"],"audio":[".mp3",".wav",".aac"], "archive":[".zip",".rar",".tar",".gz"]}

    print("++++++++++++++++++++++++", "File Investigator", "++++++++++++++++++++++++")
    folder = input("Enter folder path: ")
    if not os.path.isdir(folder):
        print("Invalid folder path.")
        exit()

    files = []
    for f in os.listdir(folder):
        path = os.path.join(folder, f)

        if os.path.isfile(path):
            files.append(f)

    print("Files found:",len(files))
    print("Type of files:")
    print("______________________________"*3)

    txt = 0
    img = 0
    vid = 0
    aud = 0
    arc = 0

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        for key, value in fileTypes.items():
            if ext in value:
                if key == "text":
                    txt += 1
                elif key == "image":
                    img += 1
                elif key == "video":
                    vid += 1
                elif key == "audio":
                    aud += 1
                elif key == "archive":
                    arc += 1

    print("Text files:", txt)
    print("Image files:", img)
    print("Video files:", vid)
    print("Audio files:", aud)
    print("Compressed files:", arc)

    print("Large files: [bigger than 10MB]")
    print("______________________________"*3)

    bigs = []

    for file in files:
        path = os.path.join(folder, file)
        size = os.path.getsize(path)
        if size > 10000000:  # 10MB
            bigs.append((file, size))
    
    if len(bigs) == 0:
        print("No large files found.")
    else:
        for file, size in bigs:
            print(file, ":", size, "bytes")


    print("\nDone investigating files in folder:", folder)
