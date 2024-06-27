def classify_model_by_f1_score(tp, fp, fn):
    # Checking if tp and fp and fn are int
    if isinstance(tp, int):
        print('tp must be int')
    if isinstance(fp, int):
        print('fp must be int')
    if isinstance(fn, int):
        print('fn must be int')
        exit()

    # Checking if tp and fp and fn are greater than zero
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        exit()

    # Classifying process
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}')
# classify_model_by_f1_score(tp =2 , fp =3 , fn =4)