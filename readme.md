
# CNN: 5 видов лягушек

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
│   # ML main algorithm
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

- [ ] [NN: Backpropagation](https://www.youtube.com/watch?v=IN2XmBhILt4)

- [ ] [NN: Cross Entropy](https://www.youtube.com/watch?v=6ArSys5qHAU)

- [x] [CNN](https://www.youtube.com/watch?v=HGwBXDKFk9)

- [ ] [CNN: practice](https://www.youtube.com/watch?v=jztwpsIzEGc)  

- [ ] [DVC: practice](https://www.youtube.com/playlist?list=PL7WG7YrwYcnDb0qdPl9-KEStsL-3oaEjg)  


## Roadmap

- [ ] https://www.gbif.org

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
- [ ] Выбор гиперпараметров
- [ ] Кросс-валидация: Сложность / Accuracy
