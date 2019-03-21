import glob, os, json


CURDIR = os.path.dirname(os.path.abspath(__file__))

def read_file(fpath):
    with open(fpath) as fp:
        spayload = fp.read()
        payload = json.loads(spayload)
        fulltext = payload['responses'][0]['fullTextAnnotation']['text']
        print("repr: \n\n")
        print(repr(fulltext))
        print("on text: \n\n")
        print(fulltext)

def main():
    fpattern = 'data/*/*json'
    absfpath = os.path.join(CURDIR,fpattern)
    # print("path : ",absfpath)
    files = glob.glob(absfpath,recursive=True)
    # print(files)
    files = filter( lambda fname : "20190207_00001_001.jpg.json" in fname , files)
    for f in files:
        print("filename :", f)
        read_file(f)

if __name__ == "__main__":
    main()