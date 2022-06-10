
# Machine Learning Tanam.in

Machine Learning for detection vegetables and fruit and detection diseas leaf on tomato



## Contributing
Team Machine Learning on Tanam.in :
- Dwiweka Naratama [https://www.linkedin.com/in/dwiwekanaratama/]
- Dean Sitorus [https://www.linkedin.com/in/sj-dean-veza-sitorus-243743212/]




## Dataset
We import the dataset from kaggle.com
 - [Vegetable Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)
 - [Tomato Leaf Disease Dataset](https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf)
## Library

Library we use a lot to create the model

```bash
  tensorflow
  os
  numpy
  matplotlib
  pandas
  seaborn
```
    
## Vegetable Detection

This detection has 13 classes which is:
- 0: 'Bean' 
- 1: 'Bitter_Gourd' 
- 2: "Broccoli" 
- 3: 'Cabbage' 
- 4: 'Capsicum' 
- 5: 'Carrot'
- 6: 'Cauliflower'
- 7: 'Cucumber' 
- 8: 'Papaya' 
- 9: 'Potato' 
- 10: 'Pumpkin'
- 11: "Tomato"

We use transfer learning method [Xception](https://www.tensorflow.org/api_docs/python/tf/keras/applications/xception/Xception) on our model so it can reach high accuracy.



Here is accuracy on vegetable detection we use

![akurasi](https://user-images.githubusercontent.com/80300827/173003239-230a8328-8173-4ed5-a24e-ca53bdb64839.png)

Result predict on image

![Kol](https://user-images.githubusercontent.com/80300827/173003476-f3e55548-eca8-491a-88ee-42cacbb95689.png)

![Tomato](https://user-images.githubusercontent.com/80300827/173003549-d16fb96d-01cf-4d02-926d-8ad108fa161a.png)

