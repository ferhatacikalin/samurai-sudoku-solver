import os
import pickle


def board_to_pickle(bo):
    try:
        os.remove("board.pickle")
    except:
        pass
    pickle_out = open("board.pickle", "wb")
    pickle.dump(bo, pickle_out)
    pickle_out.close()


def pickle_to_board():
    pickle_in = open("board.pickle", "rb")
    board = pickle.load(pickle_in)
    pickle_in.close()
    return board



