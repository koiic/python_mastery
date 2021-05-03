class ScoreTracker:

    def __init__(self, scores=[]):
        self.scores = scores

    def add_score(self, score):
        """
        method to append new score to score list
        :param score: the new score in integer
        :return: append score to the list of scores
        """
        return self.scores.append(score)

    def min_score(self):
        """

        :return: the min score in the scores list
        """
        return min(self.scores)

    def max_score(self):
        """

        :return: the max score in the scores list
        """

        return max(self.scores)

    def number_of_scores(self):
        """

        :return: return the sum of all score in the scores list
        """
        return sum(self.scores)

    def get_scores(self):
        """

        :return: print all score in the scores list on the screen
        """
        for score in self.scores:
            print (score)


if __name__ == '__main__':
    my_score = ScoreTracker([1,2,4,5])
    my_score.add_score(12)
    my_score.add_score(14)
    my_score.add_score(2)
    my_score.add_score(5)
    print('this is min score -> ', my_score.min_score())
    print('this is max score -> ', my_score.max_score())
    print('this is total score -> ', my_score.number_of_scores())
    print('this is list of scores -> ', my_score.get_scores())
