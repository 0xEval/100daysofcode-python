class QuizBrain:
    def __init__(self, q_list) -> None:
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def next_question(self) -> str:
        """Returns the user's answer to the next question in the list."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return input(f'Q{self.question_number}: {current_question.text} ')

    def still_has_question(self) -> bool:
        """Returns `True` if there are questions left in the list."""
        return self.question_number < len(self.question_list)

    def check_answer(self, ans) -> bool:
        """Returns `True` if the user answered the question correctly, `False` otherwise."""
        if (
            ans.lower()
            == self.question_list[self.question_number - 1].answer.lower()
        ):
            self.score += 1
            print('You got it right!')
            return True
        else:
            print('That is wrong!')
            print(
                f'The correct answer was {self.question_list[self.question_number].answer}'
            )
        print(f'Your current score is: {self.score}/{self.question_number}.')
        return False
