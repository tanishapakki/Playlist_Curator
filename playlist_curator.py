def tokenize(content):
    tokens = content.split()
    return tokens

def author(tokens,author_req):
    x=0
    start=0
    end=0
    for i,token in enumerate(tokens):
        if token=='!!' and x==0:            
            if i + 1 < len(tokens):
                if tokens[i+1] == author_req:
                    start=i+2
                    x=1
        elif token=='!!' and x==1:
            end=i-1
    mood_req=input("Mood of choice? ")
    print(mood(tokens,start,end,mood_req))
 
def mood(tokens, start, end,mood_req):
    happy=['smile','sunshine','daylight','happy']
    sad=['problems','hurt','cry']
    happy_c=0
    sad_c=0
    moods=['happy','sad']
    for token in tokens[start:end]:
        if token in happy:
            happy_c+=1
        elif token in sad:
            sad_c+=1
    moods_c=[happy_c,sad_c]
    max_mood=moods_c[0]

    for i in moods_c:
         if i> max_mood:
             max_mood=i
    mood_song= moods[moods_c.index(max_mood)]
    if mood_song==mood_req:
        return mood_song
    else:
        return 'not matching'

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
            author(tokens,author_req)
            

    except FileNotFoundError:
        print("File not found.")

def main():
    songs = "songs"
    read_file(songs)

if __name__ == "__main__":
    main()