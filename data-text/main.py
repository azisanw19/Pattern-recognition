import re
import math


def get_document():
    try:
        number_of_document = int(input('number of document? '))
        documents = []
        for document_number in range(number_of_document):
            document = input(f'input document {document_number} \n')
            documents.append(document)
        return documents
    except ValueError:
        print('failed input!')
        return


def lexical_analysis(document: str):
    # to lower case
    document = document.lower()
    # remove number & punctuation
    tokens = re.findall(r'[a-z]+', document)
    return tokens


def stoplist_removal(tokens: list, stoplist: list):
    for term in stoplist:
        try:
            tokens.remove(term)
        finally:
            continue
    return tokens


def phrase_detection(tokens: list, phrase: dict):
    length_tokens = len(tokens)
    for token_index in range(length_tokens - 1):
        for phrase_key in list(phrase.keys()):
            if tokens[token_index] == phrase_key and (token_index + 1) <= length_tokens and (tokens[token_index+1] in phrase[phrase_key]):
                tokens[token_index] = f'{tokens[token_index]} {tokens[token_index+1]}'
                tokens.pop(token_index+1)
    return tokens


def porter_algorithm(tokens: list, rule: dict):
    # issue makan -> ma
    for token_index in range(len(tokens)):
        for key in list(rule.keys()):
            try:
                tokens[token_index] = re.sub(key, rule[key], tokens[token_index])
            finally:
                continue
    return tokens


def bag_of_word(documents: list):
    words = []
    for document in documents:
        words += document
    # Remove duplicate
    return list(set(words))


def term_frequency(tokens: list, words: list):
    TF = [0 for _ in range(len(words))]
    for word_index in range(len(words)):
        for token in tokens:
            if token == words[word_index]:
                TF[word_index] += 1
    return TF


def inverse_document_frequency(total_words: list, number_of_documents: int):
    IDF = [0 for _ in range(len(total_words))]
    for word_index in range(len(total_words)):
        IDF[word_index] = 1 + math.log(number_of_documents / total_words[word_index], 10)
    return IDF


def combine_TFIDF(TF: list, IDF: list):
    TFIDF = [0. for _ in range(len(TF))]
    for TFIDF_index in range(len(TFIDF)):
        TFIDF[TFIDF_index] = TF[TFIDF_index] * IDF[TFIDF_index]
    return TFIDF


def main():
    stoplist = ['adalah', 'sudah', 'untuk', 'sang', 'si', 'yang', 'dan']
    dict_rule = {
        'kah$': '',
        'lah$': '',
        'pun$': '',
        'ku$': '',
        'mu$': '',
        'nya$': '',
        'kan$': '',
        'an$': '',
        '^me': '',
        '^ber': ''
    }
    phrase = {
        'sapu': ['tangan', 'lidi'],
        'ilmu': ['komputer'],
        'tanggung': ['jawab']
    }

    documents = get_document()
    if documents is None:
        return

    print(f'Result preprocessing')
    for document_index in range(len(documents)):
        documents[document_index] = lexical_analysis(documents[document_index])
        documents[document_index] = stoplist_removal(documents[document_index], stoplist)
        documents[document_index] = porter_algorithm(documents[document_index], dict_rule)
        documents[document_index] = phrase_detection(documents[document_index], phrase)
        print(f'document {document_index}: {documents[document_index]}')


    bow = bag_of_word(documents)
    score_TF = [list() for _ in range(len(documents))]
    for document_index in range(len(documents)):
        score_TF[document_index] = term_frequency(documents[document_index], bow)

    total_TF = [0 for _ in range(len(bow))]
    for TF in score_TF:
        for total_TF_index in range(len(total_TF)):
            total_TF[total_TF_index] += TF[total_TF_index]

    score_IDF = inverse_document_frequency(total_TF, len(documents))

    score_TFIDF = [list() for _ in range(len(score_TF))]
    for TF_index in range(len(score_TF)):
        score_TFIDF[TF_index] = combine_TFIDF(score_TF[TF_index], score_IDF)

    print(f'bag of word: {bow}')
    for score_index in range(len(score_TFIDF)):
        print(f'document {score_index}: {score_TFIDF[score_index]}')


if __name__ == '__main__':
    main()
