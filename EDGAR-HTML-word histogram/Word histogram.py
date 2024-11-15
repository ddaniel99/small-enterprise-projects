file = '/PATH/gs-20231231.htm'

# create a word dictionary from an input html file
def word_dictionary(file):
    # open the file, read and split
    with open(file , 'r', encoding='utf-8', errors='ignore',
                ) as f:
            text = f.read()
            words = text.split()
            word_count = {}
            # iterate through the words and build the word count dictionary
            for word in words:
                word = word.lower()
                word = word.strip('.,?!()')
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            return word_count

# from word_count dictionary, create a word histogram as a Dataframe and save the csv
def word_histogram(word_count):
    import pandas as pd
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_word_count:
        print(f'{word}: {count}')    
    # create a dataframe from sorted word count:
    df = pd.DataFrame(sorted_word_count, columns=['word', 'count'])
    # remove rows containing certain words that are common HTML descriptors
    df = df[~df['word'].str.contains('=|#|pt|text-align|colspan|unitref|format=|><|span|px|x:n|&amp')]
    # remove rows with a certain value in the word column
    df = df[~df['word'].isin(['lt', 'the', 'and', 'to', 'of', 'in', 'for', 'a', 'at', 'an', 'is', 'on', 'as', 'we', 'by', 'with', 'that', 'are', 'be', 'or', 'this'])]
    df.to_csv('word_histogram.csv', index=False)
    return(df)

# create a 2 and 3-word expression dictionary from an input html file
def expression_dictionary(file):
    # open the file, read and split
    with open(file , 'r', encoding='utf-8', errors='ignore',
                ) as f:
            text = f.read()
            words = text.split()
            # remove words that contain certain characters and lowercase
            words = [word for word in words if not any(char in word for char in ['=', '#', 'pt', 'text-align', 'colspan', 'unitref', 'format=', '><', 'span', 'px', 'x:n', '&amp'])]
            words = [word.strip('.,?!()') for word in words]
            words = [word for word in words if word not in ['lt', 'the', 'and', 'to', 'of', 'in', 'for', 'a', 'at', 'an', 'is', 'on', 'as', 'we', 'by', 'with', 'that', 'are', 'be', 'or', 'this']]
            words = [word.lower() for word in words]
            expression_count = {}
            # iterate through the words to build the dictionary
            for word in range(0, len(words)):
                    try:
                        if words[word] + " " + words[word + 1] in expression_count: expression_count[words[word] + " " + words[word + 1]] += 1
                        else: expression_count[words[word] + " " + words[word + 1]] = 1
                    except:
                        pass
                    try:
                        if words[word] + " " + words[word + 1] + " " + words[word + 2] in expression_count: expression_count[words[word] + " " + words[word + 1] + " " + words[word + 2]] += 1
                        else: expression_count[words[word] + " " + words[word + 1] + " " + words[word + 2]] = 1
                    except:
                        pass
            return expression_count

# build the expression histogram as a Dataframe from expression_count and save the csv
def expression_histogram(expression_count):
    import pandas as pd
    sorted_expression_count = sorted(expression_count.items(), key=lambda x: x[1], reverse=True)
    for expression, count in sorted_expression_count:
        print(f'{expression}: {count}')
    df = pd.DataFrame(sorted_expression_count, columns=['expression', 'count'])
    df.to_csv('expression_histogram.csv', index=False)
    return(df)
