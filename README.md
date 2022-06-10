
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

![alt text](https://ibb.co/HXrwf5K)

Result predict on image

![alt text](https://ibb.co/TrMsFSQ)

![alt text](https://ibb.co/1JrxRcg)
