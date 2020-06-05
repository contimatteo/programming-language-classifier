# /usr/bin/env python3

import dotenv
from algorithms import NaiveBayes, SVM, CNN, MG_CNN


dotenv.load_dotenv()
ENABLED_MODELS = {
    'BAYES': True,
    'SVM': True,
    'CNN': True,
    'MG_CNN': True,
}


if __name__ == "__main__":
    print('')

    #
    # BAYES
    #

    if ENABLED_MODELS['BAYES']:
        print(' > ')
        # initialization
        print(' >  [BAYES]  features initialization ...')
        naiveBayes = NaiveBayes()

        # training
        print(' >  [BAYES]  training ...')
        naiveBayes.train()

        # testing
        print(' >  [BAYES]  testing ...')
        naiveBayes.test()

    #
    # SVM
    #

    if ENABLED_MODELS['SVM']:
        print(' > ')
        # initialization
        print(' >  [SVM]  features initialization ...')
        svm = SVM()

        # training
        print(' >  [SVM]  training ...')
        svm.train()

        # testing
        print(' >  [SVM]  testing ...')
        svm.test()

    #
    # CNN
    #

    if ENABLED_MODELS['CNN']:
        print(' > ')
        # initialization
        print(' >  [CNN]  features initialization ...')
        cnn: CNN = CNN()

        # training
        print(' >  [CNN]  training ...')
        cnn.train()

        # testing
        print(' >  [CNN]  testing ...')
        cnn.test()

    #

    #
    # MG_CNN
    #

    if ENABLED_MODELS['MG_CNN']:
        print(' > ')
        # initialization
        print(' >  [MG_CNN]  features initialization ...')
        mg_cnn: CNN = MG_CNN()

        # training
        print(' >  [MG_CNN]  training ...')
        mg_cnn.train()

        # testing
        print(' >  [MG_CNN]  testing ...')
        mg_cnn.test()

    #

    if ENABLED_MODELS['BAYES'] or ENABLED_MODELS['SVM'] or ENABLED_MODELS['CNN'] or ENABLED_MODELS['MG_CNN']:
        print(' > ')

    print('')

