import time
import tkinter as tk

from quiz_brain import QuizBrain

THEME_COLOR = '#375362'
FONT = ('Arial', 20, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.root = tk.Tk()
        self.root.title('Quizzler App')
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        # Top Section
        self.score = tk.Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        # Middle Section
        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.canvas.grid(row=1, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='Question Text',
            width=280,
            fill=THEME_COLOR,
            font=FONT,
        )

        # Bottom Section
        false_image = tk.PhotoImage(file='images/false.png')
        self.btn_false = tk.Button(
            image=false_image,
            highlightbackground=THEME_COLOR,
            command=self.false_pressed,
        )
        self.btn_false.grid(row=2, column=1)

        true_image = tk.PhotoImage(file='images/true.png')
        self.btn_true = tk.Button(
            image=true_image,
            highlightbackground=THEME_COLOR,
            command=self.true_pressed,
        )
        self.btn_true.grid(row=2, column=0)

        self.get_next_question()
        self.root.mainloop()

    def get_next_question(self) -> None:
        """Update Canvas text with latest Quizz question"""
        self.canvas.configure(bg='white')
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text='You have reached the end!'
            )
            self.btn_false.config(state='disabled')
            self.btn_true.config(state='disabled')

    def true_pressed(self) -> None:
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self) -> None:
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, player_answer) -> None:
        """Give Player visual feedback of his answer by changing Canvas background"""
        self.canvas.itemconfig(self.question_text, fill='white')
        if player_answer == True:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.score.configure(text=f'Score: {self.quiz.score}')
        self.root.after(1000, self.get_next_question)
