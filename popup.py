import PySimpleGUI as sg

#ここでresultにsg.popup_yes_noの結果を入れている
result = sg.popup_yes_no("あなたにおすすめの犬種を探します。あなたが好きなのは超小型犬ですか？")

#↑でresultに入っているyes/noを判定している
if result == "Yes":
    #ここでsg.popup_yes_noを使っているが結果をresultに入れていないのでresultの内容は4行目で選んだyes/noのまま
    sg.popup_yes_no("性格は穏やかな子が好きですか？")
    #つまり正解は以下のようになる。その他のsg.popup_yes_noも全て同じ理由で正しく動作していない
    # result = を頭に入れることでresultに新たに出てきたポップアップのyes/noの結果を入れ直す。
    # result = sg.popup_yes_no("性格は穏やかな子が好きですか？")

    #ifでresultを判定するけどここのresultは4行目で選んだyes/noのままなので最初に選んだyes/noの結果にしか行かない
    if result == "Yes":
     #ここのsg.popupはyes_noではないのでただポップアップを出すだけなのでresult= をつける必要はない
     sg.popup("あなたにはマルチーズ、ヨークシャテリアがおすすめです")

    if result == "Yes":
     sg.popup("あなたにはチワワ、トイプードル、パピヨン、柴犬、ポメラニアンがおすすめです")

#以下も全く同じ理由で動作していないので、全てのsg.popup_yes_noは result = sg.popup_yes_noとする必要がある

elif result == "No":
    sg.popup_yes_no("では小型犬が好きですか？")

    if result == "Yes":
        sg.popup_yes_no("性格は穏やかな子が好きですか？")

        if result == "Yes":
            sg.popup("あなたにはキャバリア、シーズー、パグがおすすめです")

        elif result == "No":
            sg.popup("あなたには柴犬、ミニチュアシュナウザー、ミニチュアダックスフンドがおすすめです")



    elif result == "No":
        sg.popup_yes_no("では中型犬が好きですか？")

        if result == "Yes":
            sg.popup_yes_no("性格は穏やかな子が好きですか？")

            if result == "Yes":
                sg.popup("あなたにはビーグル、フレンチブルドック、ミニチュアブルテリアがおすすめです")

            elif result == "No":
                sg.popup("あなたにはピットブルテリア、コーギー、ボーダーコリーがおすすめです")



        if result == "No":
            sg.popup_yes_no("では大型犬が好きですか？")

            if result == "Yes":
                sg.popup_yes_no("性格は穏やかな子が好きですか？")

                if result == "Yes":
                    sg.popup("あなたには秋田犬、ラブラドールレトリバー、シェパードがおすすめです")

                elif result == "No":
                    sg.popup("あなたにはシベリアンハスキー、ダルメシアン、ボルゾイがおすすめです")

            elif result == "No":
                sg.popup("犬と和解せよ")