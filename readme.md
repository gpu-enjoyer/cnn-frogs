
# CNN: 5 видов лягушек

## Stack

- [x] notes.ipynb
- [x] contourf plot
- [x] git push
- [x] nn: backprop
- [x] nn: cross-entrory
- [ ] download data
- [ ] cnn: practice
- [ ] dvc:practice


## Лягушки

<table>
  <thead>
    <tr>
      <th>1. Agalychnis <br>callidryas</th>
      <th>2. Breviceps <br>gibbosus</th>
      <th>3. Ceratophrys <br>cornuta</th>
      <th>4. Dendrobates <br>tinctorius</th>
      <th>5. Hyalinobatrachium <br>fleischmanni</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="./internal/readme_img/Agalychnis_callidryas.jpg"></td>
      <td><img src="./internal/readme_img/Breviceps_gibbosus.jpg"></td>
      <td><img src="./internal/readme_img/Ceratophrys_cornuta.jpg"></td>
      <td><img src="./internal/readme_img/Dendrobates_tinctorius.jpeg"></td>
      <td><img src="./internal/readme_img/Hyalinobatrachium_fleischmanni.jpg"></td>
  </tbody>
</table>


## Как использовать

### Подготовка окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r req.txt

deactivate
```

### Обучение

```bash
code cnn.ipynb
```

### Inference

```bash
# ...
```


## Структура проекта

```bash
tree -F -I ".venv|.git|readme.md"

./
├── cnn.ipynb
│   # main ML algorithm
│
├── notes.ipynb
│   # Backpropagation: part.der.
│   # RSS
│   # Activation func-s
│   # Cross Entropy
│   # ResNet
│
├── req.txt
│   # requirements for cnn.ipynb
│
├── dataset/
│   # 1/ ... 5/
│
└── internal/
```


## Учебные материалы 

- [x] [Softmax](https://www.pinecone.io/learn/softmax-activation/)  

  - Как использовать **Softmax** в качестве функции активации для последнего слоя весов в задаче классификации.
  - Как **Softmax** преобразует вектор логитов в вектор вероятностей.
  - **Softmax** как обобщение Sigmoid. Частный случай: бинарная классификация.
  - Реализация функций активации на Python.  

- [x] [NN](https://www.youtube.com/watch?v=CqOfi41LfDw)

- [x] [NN: Backpropagation](https://www.youtube.com/watch?v=IN2XmBhILt4)

  **Рассмотреть** cуществование лучшего множества весов.  

  Алгоритм SGD — это решение задачи поиска **локального минимума**.  
  Поэтому важны **начальные значения весов**.  
  Чтобы можно было воспользоваться экспертностью в определении весов, необходимо уметь интерпретировать слои NN.  
  ...

- [x] [NN: Cross Entropy](https://www.youtube.com/watch?v=6ArSys5qHAU)

  Обычная точность (Accuracy) — это просто «true/false».  
  Кросс-энтропия штрафует за сильную уверенность в неправильном ответе.  
  Это заставляет алгоритм не просто угадывать, а стремиться к максимальной уверенности в правильных ответах.
  $$\sum{y_i \log{p_i}}$$

- [x] [CNN](https://www.youtube.com/watch?v=HGwBXDKFk9)

- [ ] [CNN: practice](https://www.youtube.com/watch?v=jztwpsIzEGc)  

- [ ] [DVC: practice](https://www.youtube.com/playlist?list=PL7WG7YrwYcnDb0qdPl9-KEStsL-3oaEjg)  


## Roadmap

- [ ] get data

---

- [ ] 500 img / spec
- [ ] 80 train / 20 test
- [ ] size /= 255.0

---

- [ ] Conv - ReLU - MaxPool
- [ ] Conv - ReLU - Flatten
- [ ] Dense (?)
- [ ] SoftMax

---

- [ ] 5-10 эпох
- [ ] Accuracy

---

- [ ] predict.py
- [ ] DVC

---

- [ ] Не-лягушка
- [ ] Кросс-валидация (разбиения)
- [ ] Выбор гиперпараметров ?
