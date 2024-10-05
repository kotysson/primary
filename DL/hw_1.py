import torch
from torch.optim import SGD

# мы хотим предсказать оценку, которую получили игры в жанре RPG, по выбранным признакам
# реальная оценка взята с сайта Игромании

# описываем объекты и их признаки
witcher_3 = torch.tensor([[0.9, 0.9, 0.6]]) # сюжет, вовлеченность, боевая система
mass_effect_3 = torch.tensor([[0.7, 0.9, 0.8]])
kingdom_come = torch.tensor([[0.7, 0.7, 0.9]])
dragon_age_2 = torch.tensor([[0.6, 0.7, 0.5]])
smuta = torch.tensor([[0.5, 0.4, 0.3]])

dataset = [
    (witcher_3, torch.tensor([[0.9]])), # новый тензор - оценка, которую получила игра
    (mass_effect_3, torch.tensor([[0.8]])),
    (kingdom_come, torch.tensor([[0.7]])), 
    (dragon_age_2, torch.tensor([[0.6]])),
    (smuta, torch.tensor([[0.4]]))
]

# закрепляем генерируемые рандомные значения
torch.manual_seed(42)

# расставляем веса
w0_plot = torch.rand((1, 1), requires_grad=True)
w1_involvement = torch.rand((1, 1), requires_grad=True)
w2_combat = torch.rand((1, 1), requires_grad=True)
bias = torch.tensor(torch.rand((1, 1)), requires_grad=True)

optimizer = SGD([w0_plot, w1_involvement, w2_combat, bias], lr=0.01)

def calc_rating(object: torch.Tensor) -> torch.Tensor:
    return torch.tensor([w0_plot, w1_involvement, w2_combat]) @ object.T + bias

def loss_function(y_pred, y_actual):
    return torch.nn.functional.mse_loss(y_pred, y_actual)

for epoch in range(10):
    print('New epoch')
    for item in dataset:
        optimizer.zero_grad() # обнуляем градиент
        actual_rating = item[1]
        predicted_rating = calc_rating(item[0])

        loss = loss_function(predicted_rating, actual_rating)
        loss.backward() # задаем направление градиента

        optimizer.step() # обновляем градиент

        print('Loss: ', loss)

# судя по всему, с каждой итерацией ошибка уменьшается => оптимизация работает?