
# CNN: 5 видов лягушек

## Stack

- [x] notes.ipynb
- [x] contourf plot
- [x] git push
- [x] nn: backprop
- [x] nn: cross-entrory
- [x] download data
- [ ] redo: download:  
get() -> json -> observation -> img -> link -> save() -> csv
- [ ] dvc ?
- [ ] cnn: practice
- [ ] dvc:practice


## Лягушки

<table>
  <thead>
    <tr>
      <th>1. Agalychnis callidryas</th>
      <th>2. Breviceps gibbosus</th>
      <th>3. Ceratophrys cornuta</th>
      <th>4. Dendrobates tinctorius</th>
      <th>5. Hyalinobatrachium fleischmanni</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="./dataset/class1/0.jpg"></td>
      <td><img src="./dataset/class2/0.jpg"></td>
      <td><img src="./dataset/class3/0.jpg"></td>
      <td><img src="./dataset/class4/0.jpg"></td>
      <td><img src="./dataset/class5/0.jpg"></td>
  </tbody>
</table>

## Подготовка окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r req.txt

deactivate
```


## Учебные материалы 

- [x] [Softmax](https://www.pinecone.io/learn/softmax-activation/)  

- [x] [NN](https://www.youtube.com/watch?v=CqOfi41LfDw)

- [x] [NN: Backpropagation](https://www.youtube.com/watch?v=IN2XmBhILt4)

- [x] [NN: Cross Entropy](https://www.youtube.com/watch?v=6ArSys5qHAU)

- [x] [CNN](https://www.youtube.com/watch?v=HGwBXDKFk9)

- [ ] [CNN: practice](https://www.youtube.com/watch?v=jztwpsIzEGc)  

- [ ] [DVC: practice](https://www.youtube.com/playlist?list=PL7WG7YrwYcnDb0qdPl9-KEStsL-3oaEjg)


## Roadmap

- [x] get data
- [x] 240 .. 1000 img / spec
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
