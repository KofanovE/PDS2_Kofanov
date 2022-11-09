"""
Програма моделює кавовий автомат.
Кавовий автомат приймає лише монети.
Якщо була вкинута монета, що виключена із оберту (або в оберті і не знаходилася),
автомат, завершує програму і обнулює поточну суму прийнятих грошей.
Решту кавовий автомат не видає.
Ціна кави - 10 грн.
"""
class FalseCoin(Exception):

    def __init__(self, coin):
        self.coin = coin

    def logerror(self):
        print('Ahtung!', self.coin, 'грн не входе в дійсний перелік монет!')


def coffe_robot():
    true_money = {0.1, 0.5, 1, 2, 5, 10}
    balans = 0
    while True:
        try:
            if balans < 10:
                coin = input(f"Баланс: {balans} грн\nХочеш кави? Закидуй монету!:  ")
                if not float(coin) in true_money:
                    raise FalseCoin(coin)
                balans += float(coin)
                continue
            else:
                break
        except ValueError:
            print('В автомат винуте щось незрозуміле!')
            return -1
        except FalseCoin as exc:
            exc.logerror()
            return -1
    print("Забери свою каву!")

coffe_robot()
