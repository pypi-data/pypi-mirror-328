import random

from terminaltexteffects.effects.effect_slide import Slide
from terminaltexteffects.effects.effect_print import Print

def slide_animated_prompt(prompt_text: str) -> str:
    effect = Slide(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
    return input()

def animated_print(text):
    """애니메이션 효과를 적용하여 텍스트 출력"""
    effect = Print(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def googoodan_game():
    """구구단 CLI 게임"""
    while True:
        a, b = random.randint(2, 9), random.randint(2, 9)

        answer = "initial value"
        while not answer.isnumeric() and answer != "":
            answer = slide_animated_prompt(f"{a} x {b} = ")
        if answer == "":
            break
        
        if int(answer) == a * b:
            animated_print("😁 정답입니다! 🎉 ")
        else:
            animated_print(f"😭 오답! 정답은 {a * b} 입니다. 💦 ")


if __name__ == "__main__":
    googoodan_game()
