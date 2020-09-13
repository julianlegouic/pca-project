# Principal Component Analysis

### About the project
This project is about programming the PCA algorithm with the challenge of using as less as possible any of the built-in functions available in the numpy python package that could solve any big step of the algorithm (like finding the eigen values/vectors :smirk:).

<div align="center"><img src="https://i.imgflip.com/45be7u.jpg"/></br><a href="https://i.imgflip.com/45be7u.jpg">https://i.imgflip.com/45be7u.jpg</a></div><br/>  
  
**Disclaimer:** This GitHub is not about covering PCA in its deepest meanings. This is just for me and to help any other students that might stumble upon this page and who are stuck with their own implementation of a PCA algorithm. Also, feel free to download this project and to customize (like the plots) it as you want! We'd be really curious to see how good you could improve these horrendous plots! :laughing:

<details>
  <summary><b>!!Spoiler alert!!</b></summary>
  
  We half-failed on this one because we still used numpy so.. mea culpa. :sweat_smile: But we stuck to the very basic one, so keep reading, you might find what your're looking for! :wink:)
</details>

## But what is PCA?

Simply put, PCA is a technique used to point out variation and bring to light strong patterns in a dataset. Oftenly, it is used to make data easy to explore and visualize.

## The algorithm used (here)

In this implementation, we use the [power iteration](https://en.wikipedia.org/wiki/Power_iteration) algorithm to find the new components. First, we apply the algorithm on our sample data, which allows us to find the biggest eigen value and its associated vector. This forms our first principal component. Then, by excluding one dimension (associated with the first new component) from our sample data, we apply apply the algorithm again. We repeat this process until we found all the new components (i.e. all the eigen values/vectors). This kind of procedure is called a deflation method (or at least in French, sorry for my fellow speaker of English :disappointed_relieved:).

Pretty straightforward, isn't it?

## The code

Our code lets you personalize your PCA to different degrees. First, you can use either CSV or XLS files (with only one worksheet). If you choose to go with a CSV file, you can also specify the delimiter if you're against the flow and don't use commas like everybody (no judgment). Then, you can precise the percentage of restitution you desire to have with your PCA. Depending on that, the results of our program might differ.

If 2 components are enough to be over the user's percentage, the plots will be displayed in 2D. However, if 2 components are not enough to satisfy the user's percentage, the plots will be displayed in 3D, with 3 components. Since human brains cannot understand over 3 dimensions, we don't display more than 3 components (not that we actually could :confused:).

Finally, the program lets you save the numerical results in a text file or just prompt everything in the terminal if you don't want to save.

## Requirements
Only Numpy, Matplotlib and xlrd (while not mandatory for the user) are required to run this project. Check out the [```requirements.txt```](./requirements.txt) file for no more details.

## How to

### 1. Setup the environment

It is best practice to use a virtual environment with your python project, so I encourage you to check out [virtualenv](https://virtualenv.pypa.io/en/stable/). Of course there are tons of alternatives, but this one is pretty simple to setup and to configure, as it is integrated to Python directly since version 3.3.

So after creating your virtual environment and activating it, you can run the following command:
```bash
pip install -r requirements.txt
```

### 2. Use it

Run the main script called.. ```main.py``` with Python (version >= 3.5), and simply follow the instructions in your terminal! :smile:
```bash
python main.py
```

We even furnish some sample data so don't hesitate to use our ```sample.csv```, or ```sample.xls``` files! The data are grades from 9 different sutdents in 4 subjects. The results on the data don't really make any sense, these are just to showcase what our program can do.

### 3. Enjoy the results

You have two choices before the PCA goes wild: either save the results in a text file or just prompt it in your terminal. In both cases, the results are accessible with consulting the 2 shi..nning plots we have! Haha...

![2d](https://drive.google.com/uc?export=view&id=1SR5F-9f-4ir-hab7fkmahGUuxtcqi2IE)

![3d](https://drive.google.com/uc?export=view&id=1UXfn6BxYlCF7rAL-wGdWQVwuVCloHwg0)
