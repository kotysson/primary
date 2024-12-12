import torch
import pprint
from torchtext.datasets import CoNLL2000Chunking
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence # для выравнивания длины батчей

torch.manual_seed(1)

# готовим датасет
training_data = []
word_to_ix = {}
tag_to_ix = {}
words_train = []
tags_train = []

# возьмем тренировочные данные
for sentence in CoNLL2000Chunking(split='train'): 
    for word in sentence[0]:
        words_train.append(word)
        if word not in word_to_ix:
            word_to_ix[word] = len(word_to_ix)
    for pos in sentence[1]:
        tags_train.append(pos)
        if pos not in tag_to_ix:
            tag_to_ix[pos] = len(tag_to_ix)

training_data.append((words_train, tags_train))

EMBEDDING_DIM = 6 
HIDDEN_DIM = 8
VOCAB_SIZE = len(word_to_ix)
TAGSET_SIZE = len(tag_to_ix)

def prepare_sequence(seq, to_ix):
    return torch.tensor([to_ix[word] for word in seq], dtype=torch.long)

# для подготовки данных к загрузке в DataLoader
def collate_fn(batch):
    sentences, tags = zip(*batch)
    sentence_tensors = [prepare_sequence(sentence, word_to_ix) for sentence in sentences]
    tag_tensors = [prepare_sequence(tag, tag_to_ix) for tag in tags]
    return pad_sequence(sentence_tensors, batch_first=True), pad_sequence(tag_tensors, batch_first=True)

data_loader = DataLoader(training_data, batch_size=32, shuffle=True, collate_fn=collate_fn)

class LSTMTagger(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, tagset_size):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, embedding_dim)
        self.lstm = torch.nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = torch.nn.Linear(hidden_dim, tagset_size)

    def forward(self, sentences, lengths):
        embeds = self.embedding(sentences)
        packed_embeds = torch.nn.utils.rnn.pack_padded_sequence(embeds, lengths, batch_first=True, enforce_sorted=False)
        packed_output, _ = self.lstm(packed_embeds)
        output, _ = torch.nn.utils.rnn.pad_packed_sequence(packed_output, batch_first=True)
        logits = self.fc(output)
        return logits

model = LSTMTagger(VOCAB_SIZE, EMBEDDING_DIM, HIDDEN_DIM, TAGSET_SIZE)

loss_function = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

num_epochs = 5
for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    for sentences, tags in data_loader:
        lengths = torch.tensor([len(s) for s in sentences])
        sentences = sentences.to(torch.int64)
        tags = tags.to(torch.int64)

        optimizer.zero_grad()

        logits = model(sentences, lengths)

        logits = logits.view(-1, TAGSET_SIZE)
        tags = tags.view(-1)
        loss = loss_function(logits, tags)
        total_loss += loss.item()

        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {total_loss:.4f}")
