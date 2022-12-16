""" This is a more programatically complex grade calculator """

class CSC231:
    def __init__(self, quizzes, labs, assignments, test1, test2, final):

            self.quizzes = quizzes
            self.labs = labs
            self.assignments = assignments
            self.test1 = test1
            self.test2 = test2
            self.final = final

    def getGrade(self):
        total = (
              (self.quizzes * 0.15)
            + (self.labs * 0.10)
            + (self.assignments * 0.15)
            + (self.test1 * 0.20)
            + (self.test2 * 0.20)
            + (self.final * 0.20)
        )

        return total



    def __str__(self):
        return f"CSC 231: {self.getGrade()}"

csc231 = CSC231(quizzes=94.01, labs=98.71, assignments=95, test1=93, test2=97, final=90)

print(csc231)
