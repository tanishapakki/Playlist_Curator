def tokenize(content):
    tokens = content.split()
    return tokens

def reverse(song):
    s = song.split()[::-1]
    l = []
    for i in s:
        # appending reversed words to l
        l.append(i)
    return (" ".join(l))

def author(tokens,author_req,start_p,mood_req):
    x=0
    start=0
    end=0
    s=0
    i=0
    v=0
    # print(start_p)
    for i,token in enumerate(tokens[start_p::]):
        if token=='!!' and x==0:            
            if i + 1 < len(tokens):
                if tokens[i+1] == author_req:
                    start=i+2
                    x=1
        elif token=='!!' and x==1:
            end=i-1
            break
        elif i==len(tokens)-1:
            print("No data available")
    print(mood(tokens,start,end,mood_req,author_req))

def mood(tokens, start, end,mood_req,author_req):
    happy=['smile','sunshine','daylight','happy','golden','love','jokes','lover']
    sad=['problems','hurt','cry','crying','bullets']
    happy_c=0
    sad_c=0
    moods=['happy','sad']
    for token in tokens[start:end]:
        if token in happy:
            happy_c+=1
        elif token in sad:
            sad_c+=1
    moods_c=[happy_c,sad_c]
    max_mood= max(moods_c)
    song=''
    mood_song= moods[moods_c.index(max_mood)]
    if mood_song==mood_req:
        for token in tokens[start-4:0:-1]:
                if token=='#$':
                    break
                song+=token+" "
        return reverse(song)
    elif mood_song!=mood_req:
        return author(tokens[end::],author_req,0,mood_req)
    else:
        return "none found"

def read_file(songs):
    try:
        with open(songs, 'r') as file:
            content = file.read()
            # print("Content of the file:")
            # print(content)
            tokens = tokenize(content)
            # print("\nTokens:")
            # print(tokens)
            author_req=input("Author of your choice? ")
            mood_req=input("Mood of choice? ")
            author(tokens,author_req.replace(" ", ""),0,mood_req)
    except FileNotFoundError:
        print("File not found.")

def main():
    songs = "songs"
    read_file(songs)

if __name__ == "__main__":
    main()