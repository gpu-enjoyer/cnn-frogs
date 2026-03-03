
# CNN: 5 видов лягушек

## todo
- [ ] links.json -> dataset
- [ ] create pipeline ...
```bash
dvc stage add -n download \
    -d download.py \
    -d dataset.json \
    -o images \
    python download.py
```
```
dataset.json фиксируется в dvc + git
get_links.py НЕ запускается автоматически в repro.
get_links.py позволяет получить новую версию данных при желании.
```
- [ ] cnn


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

- [ ] [DVC: practice](https://www.youtube.com/watch?v=LAFVk7yz_-E)

- [ ] [CNN: practice](https://www.youtube.com/watch?v=jztwpsIzEGc)  



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

- [ ] Кросс-валидация (разбиения)
- [ ] Выбор гиперпараметров ?
