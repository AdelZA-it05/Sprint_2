class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses
        self.t_sport = '-'
        self.k_total = 1

    def number_of_wins(self):
        return f'{self.t_sport} побед: {self.victories}'

    def number_of_draws(self):
        return f'{self.t_sport} ничьих: {self.draws}'

    def number_of_losses(self):
        return f'{self.t_sport} поражений: {self.losses}'

    def total_points(self):
        return f'Общее количество очков: {self.k_total*self.victories+self.draws}'

    @classmethod
    def change_var_sport(cls, v_sport):
        cls.t_sport = v_sport
        return cls.t_sport

    @classmethod
    def change_var_total(cls, v_total):
        cls.k_total = v_total
        return cls.k_total

class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
        self.t_sport = super().change_var_sport('Футбольных')
        self.k_total = super().change_var_total(3)

class Hockey(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
        self.t_sport = super().change_var_sport('Хоккейных')
        self.k_total = super().change_var_total(2)

football_team = Football(2,2,2)
hockey_team = Hockey(2, 2, 2)
for team in (football_team, hockey_team):
    regular_methods = [method for method in dir(team) if
                       callable(getattr(team, method)) and not method.startswith(
                           "__") and not method.startswith("ch")]
    for regular_method in regular_methods:
        print(getattr(team,regular_method)())

