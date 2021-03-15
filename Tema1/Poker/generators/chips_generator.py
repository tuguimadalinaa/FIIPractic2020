from Poker.chips import Chips


def generate_chips(chips_config):
        for key, value in chips_config.items():
            for number_of_certain_chips_value in range(chips_config[key]):
                yield Chips(int(key))
