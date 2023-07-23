import time

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def ask_question(question, choices):
    print(question)
    for idx, choice in enumerate(choices):
        print(f"{idx + 1}. {choice}")
    while True:
        try:
            choice = int(input("请选择你的回答（输入序号）："))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def play_game():
    delay_print("欢迎来到浪漫的对话爱情游戏！")
    delay_print("在这个游戏中，你可以通过选择不同的对话选项来塑造自己的爱情故事。")

    love_meter = 0
    questions = [
        "你好，我是小红，很高兴认识你。你叫什么名字？",
        "你是个很有趣的人，你平时喜欢做什么？",
        "我也喜欢那个活动，我们可以一起去吗？",
        "时间过得好快，和你在一起总是那么开心。你愿意和我交往吗？",
        "我也很喜欢你，我们一起度过的时光都让我觉得幸福。你愿意和我在一起吗？"
    ]
    choices = [
        ["A. 你好，我叫小明。", "B. 嗨，我是小明。", "C. 我叫小明，很高兴认识你。"],
        ["A. 我喜欢阅读。", "B. 我喜欢旅行。", "C. 我喜欢看电影。"],
        ["A. 当然可以一起去。", "B. 我有点忙，下次再说吧。", "C. 我还没想好。"],
        ["A. 当然愿意。", "B. 我需要时间考虑一下。", "C. 我觉得我们可以先做朋友。"],
        ["A. 当然愿意。", "B. 我想再多了解一下你。", "C. 我们还是继续做朋友吧。"]
    ]

    for i in range(len(questions)):
        choice = ask_question(questions[i], choices[i])
        if choice == 1:
            love_meter += 10
        elif choice == 3:
            love_meter += 5
        elif choice == 5:
            love_meter += 15

    delay_print("\n游戏结束！")
    if love_meter <= 20:
        delay_print("你们的故事还在起步阶段，继续努力吧！")
    elif 20 < love_meter <= 35:
        delay_print("你们已经成为好朋友，可能需要更多的时间来发展感情。")
    else:
        delay_print("你们的故事充满了浪漫，恭喜你们找到了真爱！")

if __name__ == "__main__":
    play_game()
