from torch.utils.data import Dataset, DataLoader
import pandas as pd
import torch

class TitanicDataset(Dataset):
    def __init__(self):
        self.titanic_dataframe = pd.read_csv('titanic.csv')

        for column in self.titanic_dataframe.columns:
            if self.titanic_dataframe[column].dtype == 'object':
                # заполним модой столбцы с текстовыми данными
                mode_value = self.titanic_dataframe[column].mode()[0]
                # залочим, чтобы закрепить изменения в исходном датасете, а не работать с копией
                self.titanic_dataframe.loc[self.titanic_dataframe[column].isnull(), column] = mode_value
            else:
                # заполним медианой столбцы с числовыми данными
                median_value = self.titanic_dataframe[column].median()
                self.titanic_dataframe.loc[self.titanic_dataframe[column].isnull(), column] = median_value


    def __len__(self):
        return self.titanic_dataframe.shape[0]

    def __getitem__(self, idx):
        row = self.titanic_dataframe.iloc[idx]
        survived = torch.tensor(row['Survived'], dtype=torch.float32)
        fare = torch.tensor(row['Fare'], dtype=torch.float32)
        age = torch.tensor(row['Age'], dtype=torch.float32)
        # кодируем пол нулями и единицами
        sex = torch.tensor([0.]) if row['Sex'] == 'male' else torch.tensor([1.])
        # кодируем класс с помощью ohe, так как у нас 3 категории
        pclass = row['Pclass']
        pclass_ohe = torch.tensor([1. if pclass == i else 0. for i in range(1, 4)], dtype=torch.float32)
# one-hot encoding создает вектор, элемент, присутствующий в выборке, становится 1
# остальным элементам присваивается значение 0
# у нас три категории - 1, 2 или 3, значит, размерность вектора равна трем

        # все тензоры разной размерности, приводим их к одной размерности
        # view делает из скаляра одномерный тензор с размерностью 1
        x = torch.cat((fare.view(1), age.view(1), sex, pclass_ohe), dim=0)
        y = survived

        return x, y

titanic_dataset = TitanicDataset()
dataloader = DataLoader(dataset=titanic_dataset, batch_size=32, shuffle=True)

class SurvivalPredictionModel(torch.nn.Module):
    def __init__(self, input_size: int, hidden_size: int, hidden_size1: int, hidden_size2: int, out_size: int):
        super().__init__()
        self.hidden = torch.nn.Linear(input_size, hidden_size)
        self.hidden2 = torch.nn.Linear(hidden_size, hidden_size1)
        self.hidden3 = torch.nn.Linear(hidden_size1, hidden_size2)
        self.out = torch.nn.Linear(hidden_size2, out_size)
        self.relu = torch.nn.functional.relu
        self.sigmoid = torch.nn.functional.sigmoid

    def forward(self, input):
        x = self.hidden(input)
        x = self.relu(x)
        x = self.hidden2(x)
        x = self.relu(x)
        x = self.hidden3(x)
        x = self.relu(x)
        x = self.out(x)
        x = self.sigmoid(x)

        return x

# конструктор модели
# меняем input_size (три было, еще три - это закодированный pclass)
# добавляем скрытый слой
model = SurvivalPredictionModel(input_size=6, hidden_size=128, hidden_size1=64, hidden_size2=32, out_size=1)

def loss_function(y_pred, y_actual):
    return torch.nn.functional.mse_loss(y_pred, y_actual)

optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)

for epoch in range(40):
    error = torch.tensor([0.0])
    for x, y in dataloader:
        optimizer.zero_grad()
        y_pred = model(x)
        loss = loss_function(y_pred, y)
        loss.backward()
        optimizer.step()

        error = loss + error

    print(error/len(titanic_dataset))

torch.save(model.state_dict(), 'checkpoint.pt')

model.eval()

model.load_state_dict(torch.load('checkpoint.pt'))
# x = torch.tensor(titanic_dataset[40][0])
# pred = model(x)
# pred
