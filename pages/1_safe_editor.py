import streamlit as st
import json

#棒金の枚数
ROLL_COIN_COUNT = 50

#金庫読み込み
with open("safe.json", "r", encoding="utf8") as f:
    safe = json.load(f)

#safeの内容を保存する
def save_safe():
    if confirm:
        with open("safe.json", "w", encoding="utf8") as f:
            json.dump(new_safe, f, ensure_ascii=False, indent=4)
    else:
        st.warning("保存するにはチェックを入れてください。")

#string型データをint型に変換する関数
def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return 0

#クラスの定義-----
class Money:
    def __init__(self,amount,count):
        self.amount = amount #お金の価値
        self.count = count #枚数

class RollCoin:
    def __init__(self,amount,count):
        self.amount = amount #お金の価値
        self.count = count #本数
    
    #棒金をバラ硬貨へ換算して返すメソッド
    def convert_rolls_to_coins(self):
        return int(self.count * ROLL_COIN_COUNT)
    
#要素の配置-------------
st.title("金庫")

#3カラム構成の設定
col_bill,col_roll,col_coin = st.columns(3)

#入力欄の配置
with col_bill:
    input_man = st.number_input("10000円の枚数",step=1, format="%d")
    input_gosen = st.number_input("5000円の枚数",step=1, format="%d")
    input_sen = st.number_input("1000円の枚数",step=1, format="%d")

with col_roll:
    input_r_five_hundreds = st.number_input("【棒金】500円の本数",step=1, format="%d")
    input_r_hundreds = st.number_input("【棒金】100円の本数",step=1, format="%d")
    input_r_fifty = st.number_input("【棒金】50円の本数",step=1, format="%d")
    input_r_ten = st.number_input("【棒金】10円の本数",step=1, format="%d")
    input_r_five = st.number_input("【棒金】5円の本数",step=1, format="%d")
    input_r_one = st.number_input("【棒金】1円の本数",step=1, format="%d")

with col_coin:
    input_five_hundreds = st.number_input("500円の枚数",step=1, format="%d")
    input_hundreds = st.number_input("100円の枚数",step=1, format="%d")
    input_fifty = st.number_input("50円の枚数",step=1, format="%d")
    input_ten = st.number_input("10円の枚数",step=1, format="%d")
    input_five = st.number_input("5円の枚数",step=1, format="%d")
    input_one = st.number_input("1円の枚数",step=1, format="%d")

#JSON更新チェック/ボタン
confirm = st.checkbox("金庫を更新する")
st.button("金庫更新",on_click=save_safe)

#メイン処理------------
#取得した枚数を使ってインスタンスを生成
man_yen = Money(10000,input_man)
gosen_yen = Money(5000,input_gosen)
sen_yen = Money(1000,input_sen)

r_five_hundreds_yen = RollCoin(500,input_r_five_hundreds)
r_hundreds_yen = RollCoin(100,input_r_hundreds)
r_fifty_yen = RollCoin(50,input_r_fifty)
r_ten_yen = RollCoin(10,input_r_ten)
r_five_yen = RollCoin(5,input_r_five)
r_one_yen = RollCoin(1,input_r_one)

five_hundreds_yen = Money(500,input_five_hundreds)
hundred_yen = Money(100,input_hundreds)
fifty_yen = Money(50,input_fifty)
ten_yen = Money(10,input_ten)
five_yen = Money(5,input_five)
one_yen = Money(1,input_one)


#金庫のお金の枚数辞書作成
new_safe = {
    "10000円": man_yen.count,
    "5000円": gosen_yen.count,
    "1000円": sen_yen.count,
    "500円": five_hundreds_yen.count + r_five_hundreds_yen.convert_rolls_to_coins(),
    "100円": hundred_yen.count + r_hundreds_yen.convert_rolls_to_coins(),
    "50円": fifty_yen.count + r_fifty_yen.convert_rolls_to_coins(),
    "10円": ten_yen.count + r_ten_yen.convert_rolls_to_coins(),
    "5円": five_yen.count + r_five_yen.convert_rolls_to_coins(),
    "1円": one_yen.count + r_one_yen.convert_rolls_to_coins(),
}