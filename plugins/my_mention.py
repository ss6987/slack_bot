from slackbot.bot import respond_to
from slackbot.bot import listen_to

return_message = [
    ["かんかん", "みかん"],
    ["かーんかーん", "み！か！ん！"],
    ["ビーチスケッチ", "さくらうち！"],
    ["好きな食べ物", "サンドイッチ！"],
    ["ご機嫌いかが果南", "ダイブいい感じ～！"],
    ["ダイヤッホー", "ダイヤッホーーーーーーー！"],
    ["全速前進", "ヨーソロー！"],
    ["からのー", "敬礼！"],
    ["おはヨハネ", "おは善子ー！"],
    ["だからヨハネよ", "ぴょん！"],
    ["おはな", "マルーーー！！"],
    ["みなさーん", "シャイニー！！"],
    ["今日も一日", "頑張・・・・ルビィ～～～～！！"],
    ["にっこにっこにー", "にっこにっこにー!"],
    ["252521", "にっこにっこにー"],
    ["だれかたすけてー", "ちょっとまっててー！"],
    ["にゃんにゃんにゃー", "にゃんにゃんにゃー！"],
    ["ことりのおやつにしてやるぞー！", "ちゅんちゅん！"],
    ["かしこいかわいい", "えりーちかー！"],
    ["せーの", "ふぁいとだよっ！"],
]


@respond_to("")
def listen_func(message):
    string = message.body["text"]
    if string in "-list":
        return_string = "コール,レスポンス\n"
        for i in return_message:
            return_string = return_string + i[0] + "," + i[1] + "\n"
        message.send(return_string)
    else:
        for i in return_message:
            if i[0] in string:
                message.send(i[1])


@listen_to("")
def listen_func(message):
    string = message.body["text"]
    if string in "-list":
        return_string = "コール,レスポンス\n"
        for i in return_message:
            return_string = return_string + i[0] + "," + i[1] + "\n"
        message.send(return_string)
    else:
        for i in return_message:
            if i[0] in string:
                message.send(i[1])
