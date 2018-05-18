import re

if __name__ == "__main__":
    raw = open("transcript_raw.txt", "r")
    out = open("text", "w")


    transcript = raw.read()


    transcript = transcript.replace("?", ".")
    sentences = transcript.split(".")

    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip()
    for i in range(len(sentences)):
        if i < 10:
            out.write("allende0" + str(i+1) + "-allende " + sentences[i])
        else:
            out.write("allende" + str(i+1) + "-allende " + sentences[i])
        out.write("\n")
        
    raw.close()
    out.close()
