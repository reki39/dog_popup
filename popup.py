import PySimpleGUI as sg


result = sg.popup_yes_no("あなたにおすすめの犬種を探します。あなたが好きなのは超小型犬ですか？")

if result == "Yes":
    result = sg.popup_yes_no("性格は穏やかな子が好きですか？")

    if result == "Yes":
     sg.popup("あなたにはマルチーズ、ヨークシャテリアがおすすめです")

    if result == "Yes":
     sg.popup("あなたにはチワワ、トイプードル、パピヨン、柴犬、ポメラニアンがおすすめです")



elif result == "No":
    result = sg.popup_yes_no("では小型犬が好きですか？")

    if result == "Yes":
        result = sg.popup_yes_no("性格は穏やかな子が好きですか？")

        if result == "Yes":
            sg.popup("あなたにはキャバリア、シーズー、パグがおすすめです")

        elif result == "No":
            sg.popup("あなたには柴犬、ミニチュアシュナウザー、ミニチュアダックスフンドがおすすめです")



    elif result == "No":
        result = sg.popup_yes_no("では中型犬が好きですか？")

        if result == "Yes":
            result = sg.popup_yes_no("性格は穏やかな子が好きですか？")

            if result == "Yes":
                sg.popup("あなたにはビーグル、フレンチブルドック、ミニチュアブルテリアがおすすめです")

            elif result == "No":
                sg.popup("あなたにはピットブルテリア、コーギー、ボーダーコリーがおすすめです")



        if result == "No":
            result = sg.popup_yes_no("では大型犬が好きですか？")

            if result == "Yes":
                result = sg.popup_yes_no("性格は穏やかな子が好きですか？")

                if result == "Yes":
                    sg.popup("あなたには秋田犬、ラブラドールレトリバー、シェパードがおすすめです")

                elif result == "No":
                    sg.popup("あなたにはシベリアンハスキー、ダルメシアン、ボルゾイがおすすめです")

            elif result == "No":
                sg.popup("犬と和解せよ")