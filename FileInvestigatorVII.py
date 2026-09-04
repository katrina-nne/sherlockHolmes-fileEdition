import os

class FileInvestigator:
    def __init__(self):
        self.fileTypes ={"text":[".txt",".doc",".docx",".pdf"],"image":[".jpg",".jpeg",".png",".gif",".ico"],"video":[".mp4",".avi",".mov"],"audio":[".mp3",".wav",".aac"], "archive":[".zip",".rar",".tar",".gz"]}
        self.folder = input("Enter folder path: ")
        self.files = []
        if not os.path.isdir(self.folder):
            print("Invalid folder path.")
            exit()

        for f in os.listdir(self.folder):
            path = os.path.join(self.folder, f)
            if os.path.isfile(path):
                self.files.append(f)

    def analyzeFiles(self):
        print("Files found:", len(self.files))
        print("\tType of files:")
        print("______________________________"*2)

        txt = 0 ;img = 0; vid = 0; aud = 0; arc = 0

        for file in self.files:
            ext = os.path.splitext(file)[1].lower()
            for key, value in self.fileTypes.items():
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

    def findLargeFiles(self):
        print("\tLarge files: [bigger than 10MB]")
        print("______________________________"*2)

        bigs = []

        for file in self.files:
            path = os.path.join(self.folder, file)
            size = os.path.getsize(path)
            if size > 1000:  # 10MB
                bigs.append((file, size))

        if len(bigs) == 0:
            print("\tNo large files found.")
        else:
            for file, size in bigs:
                print("\t", file,":",round(size/1024/1024,2), "MB") 

investigator = FileInvestigator()
investigator.analyzeFiles()
investigator.findLargeFiles()            
        


