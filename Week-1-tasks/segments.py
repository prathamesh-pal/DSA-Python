'''Your task is to divide a string into segments so that each segment is a repeat of the same character. 
The segments should be represented as a list of pairs containing the segments lengths and characters.

For example, 
the string (aaabbccdddd) has four segments and can be represented as the list 
[(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')].'''

def find_segments(data):
    divded = []
    times = 1
    for i in range(1,len(data)):
        if data[i] == data[i-1]:
            times += 1
        else :
            segment = ((times) ,data[i-1])
            divded.append(segment)
            times = 1
            
    divded.append((times,data[-1]))
    return (divded)


if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]
